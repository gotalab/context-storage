/*
Example dbt model: customer_metrics.sql
Demonstrates test-driven development with dbt v1.8+ unit tests

This model calculates customer lifetime value and related metrics.
Unit tests for this model are defined in schema.yml.
*/

{{
  config(
    materialized='table',
    meta={
      'owner': 'analytics-team',
      'tier': 'gold'
    }
  )
}}

WITH customer_orders AS (
  SELECT
    c.customer_id,
    c.customer_name,
    c.signup_date,
    COALESCE(COUNT(o.order_id), 0) AS total_orders,
    COALESCE(SUM(o.order_amount), 0) AS lifetime_value,
    MIN(o.order_date) AS first_order_date,
    MAX(o.order_date) AS last_order_date
  FROM {{ ref('stg_customers') }} c
  LEFT JOIN {{ ref('stg_orders') }} o
    ON c.customer_id = o.customer_id
    AND o.order_status = 'completed'  -- Only include completed orders
  GROUP BY 1, 2, 3
)

SELECT
  customer_id,
  customer_name,
  total_orders,
  lifetime_value,
  
  -- Calculate average order value (handle division by zero)
  CASE 
    WHEN total_orders > 0 
    THEN ROUND(lifetime_value / total_orders, 2)
    ELSE NULL 
  END AS avg_order_value,
  
  first_order_date,
  last_order_date,
  
  -- Calculate days since last order
  CASE 
    WHEN last_order_date IS NOT NULL 
    THEN DATE_DIFF(CURRENT_DATE(), last_order_date, DAY)
    ELSE NULL 
  END AS days_since_last_order,
  
  -- Customer segmentation
  CASE
    WHEN total_orders = 0 THEN 'New'
    WHEN total_orders = 1 THEN 'One-time'
    WHEN total_orders BETWEEN 2 AND 5 THEN 'Regular'
    WHEN total_orders > 5 THEN 'VIP'
  END AS customer_tier,
  
  -- Recency, Frequency, Monetary (RFM) scoring
  CASE
    WHEN last_order_date IS NULL THEN 0
    WHEN DATE_DIFF(CURRENT_DATE(), last_order_date, DAY) <= 30 THEN 5
    WHEN DATE_DIFF(CURRENT_DATE(), last_order_date, DAY) <= 90 THEN 4
    WHEN DATE_DIFF(CURRENT_DATE(), last_order_date, DAY) <= 180 THEN 3
    WHEN DATE_DIFF(CURRENT_DATE(), last_order_date, DAY) <= 365 THEN 2
    ELSE 1
  END AS recency_score,
  
  CASE
    WHEN total_orders >= 10 THEN 5
    WHEN total_orders >= 7 THEN 4
    WHEN total_orders >= 5 THEN 3
    WHEN total_orders >= 2 THEN 2
    WHEN total_orders >= 1 THEN 1
    ELSE 0
  END AS frequency_score,
  
  CASE
    WHEN lifetime_value >= 1000 THEN 5
    WHEN lifetime_value >= 500 THEN 4
    WHEN lifetime_value >= 200 THEN 3
    WHEN lifetime_value >= 50 THEN 2
    WHEN lifetime_value > 0 THEN 1
    ELSE 0
  END AS monetary_score

FROM customer_orders