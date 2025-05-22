---
title: dbt命名規則
description: dbtプロジェクトにおける命名規則のベストプラクティス
---

# dbt命名規則ガイド

## モデル命名規則

### ソースモデル (source)
- プレフィックス: なし
- 形式: `<source_name>_<table_name>`
- 例: `stripe_payments`, `shopify_orders`

### ステージングモデル (staging)
- プレフィックス: `stg_`
- 形式: `stg_<source>_<entity>`
- 例: `stg_stripe_payments`, `stg_shopify_orders`

### 中間モデル (intermediate)
- プレフィックス: `int_`
- 形式: `int_<entity/topic>_<verb>`
- 例: `int_orders_joined`, `int_customers_aggregated`

### 集計モデル (marts)
- プレフィックス: `fct_` (ファクトテーブル), `dim_` (ディメンションテーブル)
- 形式: `fct_<entity>_<verb>`, `dim_<entity>`
- 例: `fct_orders_daily`, `dim_customers`

## カラム命名規則

### 主キー
- 形式: `<table_name>_id` または `<entity>_id`
- 例: `order_id`, `customer_id`

### 外部キー
- 形式: `<referenced_entity>_id`
- 例: `customer_id` (ordersテーブル内)

### タイムスタンプ
- 形式: `<event>_at`
- 例: `created_at`, `updated_at`, `deleted_at`

### ブール値
- 形式: `is_<condition>` または `has_<condition>`
- 例: `is_active`, `has_discount`

## ファイル構成規則

```
models/
  ├── sources/
  ├── staging/
  │   ├── <source1>/
  │   └── <source2>/
  ├── intermediate/
  │   ├── <domain1>/
  │   └── <domain2>/
  └── marts/
      ├── <domain1>/
      └── <domain2>/
```

## コメント規則

各モデルファイルの先頭には以下の情報を含めること：

```sql
/*
  モデル名: <model_name>
  説明: <簡潔な説明>
  作成者: <作成者名>
  依存関係: <依存するモデル>
  更新履歴:
    - YYYY-MM-DD: <変更内容> by <変更者>
*/
```
