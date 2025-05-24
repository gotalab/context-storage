# dbt Best Practices Guide

This guide outlines the best practices enforced by the IDE rules in this repository.

## Project Structure

```
dbt_project/
├── models/
│   ├── staging/          # Raw data cleaning and standardization
│   ├── intermediate/     # Business logic transformations
│   └── marts/           # Final business-ready models
├── tests/               # Custom data tests
├── macros/              # Reusable SQL macros
├── seeds/               # Static data files
├── snapshots/           # Slowly changing dimensions
└── analyses/            # Ad-hoc analyses
```

## Naming Conventions

### Models
- **Staging models**: `stg_{source}_{table_name}.sql`
- **Intermediate models**: `int_{business_concept}.sql`
- **Mart models**: `{business_area}_{entity}.sql`

### Tests
- **Unit tests**: `test_unit_{model_name}_{test_description}`
- **Data tests**: `test_data_{model_name}_{test_description}`

## Test-Driven Development with dbt v1.8+

### 1. Unit Tests (dbt v1.8+)
Unit tests validate individual model logic with mock data:

```yaml
unit_tests:
  - name: test_unit_customer_metrics_calculation
    model: customer_metrics
    given:
      - input: ref('stg_orders')
        rows:
          - {customer_id: 1, order_amount: 100, order_date: '2023-01-01'}
          - {customer_id: 1, order_amount: 200, order_date: '2023-01-02'}
      - input: ref('stg_customers')
        rows:
          - {customer_id: 1, customer_name: 'Test Customer'}
    expect:
      rows:
        - {customer_id: 1, total_orders: 2, total_amount: 300}
```

### 2. Data Tests
Data tests validate actual data quality:

```yaml
models:
  - name: customer_metrics
    description: "Customer aggregated metrics"
    meta:
      owner: "data-team"
      tier: "gold"
    columns:
      - name: customer_id
        description: "Unique customer identifier"
        tests:
          - not_null
          - unique
      - name: total_amount
        description: "Total customer spend"
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: ">= 0"
    tests:
      - dbt_utils.unique_combination_of_columns:
          combination_of_columns: ['customer_id', 'metric_date']
```

## Required Metadata

All models must include:

```yaml
meta:
  owner: "team-name"           # Required: team responsible
  tier: "bronze|silver|gold"   # Required: data quality tier
  pii: true|false             # Optional: contains PII
  refresh_schedule: "daily"    # Optional: refresh frequency
```

## Documentation Requirements

- **Model descriptions**: Every model must have a description
- **Column descriptions**: All columns must be documented
- **Macro documentation**: All macros must have descriptions and parameter docs

## Code Quality Standards

### SQL Style
- Use trailing commas in SELECT statements
- UPPERCASE keywords (SELECT, FROM, WHERE)
- lowercase identifiers (table names, column names)
- Explicit table aliases
- Consistent indentation (2 spaces)

### dbt Patterns
- Use `ref()` for model dependencies
- Use `source()` for external tables
- Leverage macros for repeated logic
- Use variables for configurable values

## Testing Strategy

### Test-Driven Development Workflow
1. **Write unit tests first** - Define expected behavior with mock data
2. **Write model code** - Implement the transformation logic
3. **Run unit tests** - Verify logic works with test data
4. **Add data tests** - Define data quality expectations
5. **Deploy and validate** - Run data tests on real data

### Test Coverage Requirements
- **Unit tests**: Every model must have at least one unit test
- **Data tests**: Every model must have not_null and unique tests on key columns
- **Custom tests**: Business rules must be tested with custom data tests

## Performance Optimization

### Materialization Strategy
- **Views**: For simple transformations, low query frequency
- **Tables**: For complex logic, high query frequency
- **Incremental**: For large datasets with append-only patterns
- **Ephemeral**: For intermediate models used only by downstream models

### Configuration Example
```yaml
models:
  my_dbt_project:
    staging:
      +materialized: view
    intermediate:
      +materialized: ephemeral
    marts:
      +materialized: table
      +post-hook: "{{ grant_select_on_schemas(schemas, 'reporting_role') }}"
```

## Error Handling

### Common Issues and Solutions

1. **Failing unit tests**
   ```bash
   dbt test --select test_type:unit --models your_model
   ```

2. **Data quality failures**
   ```bash
   dbt test --select test_type:data --models your_model
   ```

3. **Performance issues**
   - Use `{{ this }}` for incremental models
   - Add appropriate indexes via post-hooks
   - Consider partitioning for large tables

## Continuous Integration

The CI pipeline enforces:
- SQL formatting (SQLFluff)
- Unit test existence and execution
- Data test coverage
- Documentation completeness
- Metadata requirements
- Performance checks

## Getting Started

1. **Install IDE extensions** (see `/vscode/extensions.json`)
2. **Configure pre-commit hooks** (see `/pre-commit/.pre-commit-config.yaml`)
3. **Set up CI pipeline** (see `/github-actions/dbt-ci.yml`)
4. **Follow test-driven development** workflow
5. **Run quality checks** before committing

For more information, see the individual configuration files in this repository.