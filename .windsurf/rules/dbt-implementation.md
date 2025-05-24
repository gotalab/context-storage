# dbt実装ルール

dbt（Data Build Tool）プロジェクトの実装時に従うべきルールとベストプラクティス

## 基本原則

### 1. テスト駆動開発（TDD）
- **必須**: モデル実装前にユニットテストとデータテストを定義
- dbt v1.8以降のunit testsを活用
- データテストは全モデルに必須

### 2. dbt best practicesの遵守
- 公式ドキュメントに従った実装
- コード品質とメンテナビリティの確保

## 実装ルール

### 1. ユニットテスト（Unit Tests）
dbt v1.8+で導入されたunit testsを必ず使用する

```yaml
# schema.yml内での定義例
unit_tests:
  - name: test_customer_total_calculation
    model: customer_metrics
    given:
      - input: ref('customers')
        rows:
          - {customer_id: 1, status: 'active'}
          - {customer_id: 2, status: 'inactive'}
      - input: ref('orders')
        rows:
          - {customer_id: 1, amount: 100}
          - {customer_id: 1, amount: 50}
    expect:
      rows:
        - {customer_id: 1, total_amount: 150, status: 'active'}
```

**実装手順:**
1. モデルのロジック設計
2. 入力データパターンの定義
3. 期待する出力の定義
4. ユニットテストの実装
5. モデルの実装

### 2. データテスト（Data Tests）
全てのモデルに対してデータテストを実装する

**必須テスト:**
- `not_null`: 主要カラムの非NULL制約
- `unique`: 一意性制約
- `accepted_values`: 許可値の制約
- `relationships`: 参照整合性

```yaml
models:
  - name: customer_metrics
    columns:
      - name: customer_id
        tests:
          - not_null
          - unique
      - name: status
        tests:
          - accepted_values:
              values: ['active', 'inactive', 'pending']
      - name: total_amount
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: ">= 0"
```

### 3. ドキュメンテーション
全モデル・カラムに説明を記載

```yaml
models:
  - name: customer_metrics
    description: "顧客ごとの集計メトリクス。日次で更新される。"
    columns:
      - name: customer_id
        description: "顧客の一意識別子"
      - name: total_amount
        description: "顧客の総注文金額（税込み）"
```

### 4. モデル構造
**層化アーキテクチャの採用:**
- `staging`: 生データの基本的な変換・型変換
- `intermediate`: ビジネスロジックの適用
- `marts`: 最終的な分析用テーブル

```sql
-- models/staging/stg_customers.sql
select
    customer_id,
    customer_name,
    created_at::timestamp as created_at,
    status
from {{ source('raw', 'customers') }}

-- models/intermediate/int_customer_orders.sql  
select
    customer_id,
    count(*) as order_count,
    sum(amount) as total_amount
from {{ ref('stg_orders') }}
group by customer_id

-- models/marts/customer_metrics.sql
select
    c.customer_id,
    c.customer_name,
    c.status,
    coalesce(o.order_count, 0) as order_count,
    coalesce(o.total_amount, 0) as total_amount
from {{ ref('stg_customers') }} c
left join {{ ref('int_customer_orders') }} o
    on c.customer_id = o.customer_id
```

### 5. 命名規則
- **ソース**: `source_system_table_name`
- **ステージング**: `stg_table_name`
- **中間テーブル**: `int_descriptive_name`
- **マート**: `business_entity_name`

### 6. SQLスタイル
- インデントは4スペース
- カラム名は小文字のスネークケース
- キーワードは小文字
- CTEを積極的に使用

```sql
with customer_orders as (
    select
        customer_id,
        count(*) as order_count,
        sum(amount) as total_amount
    from {{ ref('stg_orders') }}
    where status = 'completed'
    group by customer_id
),

customer_metrics as (
    select
        c.customer_id,
        c.customer_name,
        co.order_count,
        co.total_amount
    from {{ ref('stg_customers') }} c
    left join customer_orders co
        on c.customer_id = co.customer_id
)

select * from customer_metrics
```

## 開発ワークフロー

### 1. 機能開発手順
1. **要件定義**: ビジネス要件の明確化
2. **テスト設計**: ユニットテスト・データテストの設計
3. **テスト実装**: schema.ymlでのテスト定義
4. **モデル実装**: SQLモデルの実装
5. **テスト実行**: `dbt test`での検証
6. **ドキュメント生成**: `dbt docs generate`

### 2. 品質確保
```bash
# 開発時の実行コマンド
dbt compile          # SQLコンパイル確認
dbt parse            # 設定ファイル解析
dbt test             # テスト実行
dbt run              # モデル実行
dbt docs generate    # ドキュメント生成
```

### 3. コードレビュー観点
- [ ] ユニットテストが適切に定義されているか
- [ ] 全モデルにデータテストが設定されているか
- [ ] ドキュメンテーションが完備されているか
- [ ] 命名規則に従っているか
- [ ] SQLスタイルガイドに準拠しているか
- [ ] 参照関係が適切に設定されているか

## 設定ファイル

### dbt_project.yml
```yaml
name: 'your_project'
version: '1.0.0'
config-version: 2

model-paths: ["models"]
analysis-paths: ["analysis"]
test-paths: ["tests"]
seed-paths: ["data"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

target-path: "target"
clean-targets:
  - "target"
  - "dbt_packages"

models:
  your_project:
    staging:
      +materialized: view
    intermediate:
      +materialized: view
    marts:
      +materialized: table
```

### packages.yml
```yaml
packages:
  - package: dbt-labs/dbt_utils
    version: 1.1.1
  - package: calogica/dbt_expectations
    version: 0.10.1
```

## チェックリスト

### モデル実装完了チェック
- [ ] ユニットテストが定義され、パスしている
- [ ] データテストが全カラムに適用されている
- [ ] モデル・カラムにドキュメントがある
- [ ] 命名規則に従っている
- [ ] SQLスタイルガイドに準拠している
- [ ] 適切な層（staging/intermediate/marts）に配置されている
- [ ] 依存関係が正しく設定されている
- [ ] `dbt run`と`dbt test`が成功する

この実装ルールに従うことで、高品質で保守性の高いdbtプロジェクトを構築できます。