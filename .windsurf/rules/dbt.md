# dbt v1.9 テスト ベストプラクティスまとめ

## はじめに

dbtでデータ品質を担保するためには、テストの仕組みを正しく設計・運用することが重要だ。ここでは、実践的なベストプラクティスに基づき、Data Tests・Unit Tests・Schema Testsの使い分けと推奨運用例をまとめる。

---

### Data Tests（データテスト）

- **目的**: モデルやテーブルのビジネスルールやデータ一貫性をSQLで検証する。
- **実装方法**:
  - `tests/` ディレクトリ配下に `.sql` ファイルを作成する。
  - クエリが1行でも結果を返した場合は「テスト失敗」と判定する。
- **例**:
    ```sql
    -- tests/no_nulls_in_id.sql
    SELECT *
    FROM {{ ref('my_model') }}
    WHERE id IS NULL
    ```
- **実行コマンド**:
  ```
  dbt test
  ```
- **ベストプラクティス**:
  - 重要なビジネスルールは必ずData Testでカバーする。
  - テストごとに目的や期待値をコメントで明記する。
  - 複雑なロジックや集計条件もData Testで積極的に検証する。

---

### Unit Tests（ユニットテスト）

- **目的**: モデルやSQLロジックの単体検証を行う。静的な入力データに対して期待される出力を検証できる。
- **公式サポート**: dbt-core v1.8以降、公式で「unit tests」機能が追加された。
- **記述方法**:
  - モデルのYAML（_properties.yml等）に`unit_tests:`キーで定義する。
  - 入力データ（given）と期待出力（expect）をYAMLで記述する。
  - fixture（入力データ）はdict/csv/sql形式で記述でき、`tests/fixtures/`などに配置可能。
- **例**:
    ```yaml
    unit_tests:
      - name: test_is_valid_email_address
        description: "Check my is_valid_email_address logic captures all known edge cases"
        model: dim_customers
        given:
          - input: ref('stg_customers')
            rows:
              - {email: cool@example.com, email_top_level_domain: example.com}
              - {email: badgmail.com, email_top_level_domain: gmail.com}
          - input: ref('top_level_email_domains')
            rows:
              - {tld: example.com}
              - {tld: gmail.com}
        expect:
          rows:
            - {email: cool@example.com, is_valid_email_address: true}
            - {email: badgmail.com, is_valid_email_address: false}
    ```
- **ベストプラクティス**:
  - テストは「model-inputs-output」構造で書く
  - テストごとに意味のあるdescriptionを付ける
  - 1つのテストで1つの振る舞いだけ検証する
  - 他のテスト（data testsやmodel contracts）と組み合わせて使う
  - fixtureはYAML, CSV, SQLいずれでもOK。`tests/fixtures/`などに整理する
  - CIやPull Request時に必ず実行する

---

### Schema Tests（スキーマテスト）

- **目的**: カラムのnot nullやunique制約など、一般的なデータ品質ルールをYAMLで簡潔に記述・検証する。
- **実装方法**:
  - モデルのYAMLファイルで `tests` キーを使い、標準テストを定義する。
- **例**:
    ```yaml
    models:
      - name: my_model
        columns:
          - name: id
            tests:
              - not_null
              - unique
    ```
- **ベストプラクティス**:
  - すべての主要カラムに対してnot_nullやuniqueテストを設定する。
  - 受け入れ可能な値（accepted_values）なども必要に応じて活用する。

---

## テスト運用のベストプラクティス

- すべてのテストはCI/CDパイプラインに組み込む。
- テストが失敗した場合は必ず原因を調査し、根本原因を解決する。
- 複雑なビジネスロジックや要件はData TestやUnit Testでカバーする。
- テストケースやテスト名は目的が一目で分かるように命名・記述する。
- Pull Request時に必ずテストが実行されるようにする。

---

## まとめ

- Data Testsはビジネスロジックや複雑な条件の検証に使う。
- Unit Testsはマクロやモデルの単体ロジック検証に使う。
- Schema Testsは標準的なデータ品質ルールの自動検証に使う。

テスト設計と運用を徹底することで、dbtプロジェクトの品質と信頼性を高めることができる。
