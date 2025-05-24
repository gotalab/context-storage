# Setup Instructions

This guide will help you set up the dbt IDE rules in your dbt project.

## Prerequisites

- dbt v1.8+ (for unit tests support)
- Python 3.8+
- Your data warehouse credentials configured

## Quick Setup

### 1. VS Code Setup

Copy the VS Code configuration to your dbt project:

```bash
# Copy VS Code settings
mkdir -p .vscode
cp vscode/settings.json .vscode/
cp vscode/extensions.json .vscode/
cp vscode/tasks.json .vscode/
```

Install recommended extensions when prompted by VS Code.

### 2. SQLFluff Configuration

Copy the SQLFluff configuration:

```bash
cp sqlfluff/.sqlfluff .
```

Update the dialect in `.sqlfluff` to match your data warehouse:
- `bigquery` for Google BigQuery
- `snowflake` for Snowflake
- `redshift` for Amazon Redshift
- `postgres` for PostgreSQL

### 3. Pre-commit Hooks

Set up pre-commit hooks for automatic code quality checks:

```bash
# Install pre-commit
pip install pre-commit

# Copy configuration
cp pre-commit/.pre-commit-config.yaml .

# Copy validation scripts
mkdir -p scripts
cp scripts/check_unit_tests.py scripts/
cp scripts/check_data_tests.py scripts/

# Install hooks
pre-commit install
```

Update the SQLFluff dialect in `.pre-commit-config.yaml` to match your warehouse.

### 4. GitHub Actions (Optional)

For CI/CD integration:

```bash
mkdir -p .github/workflows
cp github-actions/dbt-ci.yml .github/workflows/
```

Update the dbt adapter installation in the workflow file to match your warehouse.

### 5. Install Dependencies

Install required Python packages:

```bash
pip install dbt-bigquery sqlfluff dbt-checkpoint
# Replace dbt-bigquery with your warehouse adapter:
# dbt-snowflake, dbt-redshift, dbt-postgres, etc.
```

## Configuration Customization

### SQLFluff Dialect Configuration

Edit `.sqlfluff` and update:

```ini
[sqlfluff]
dialect = your_warehouse  # bigquery, snowflake, redshift, postgres
```

### Pre-commit Warehouse Adapter

Edit `.pre-commit-config.yaml` and update:

```yaml
- repo: https://github.com/sqlfluff/sqlfluff
  rev: 3.0.7
  hooks:
    - id: sqlfluff-lint
      args: [--dialect=your_warehouse]
      additional_dependencies: ['dbt-your_warehouse', 'sqlfluff-templater-dbt']
```

### GitHub Actions Workflow

Edit `.github/workflows/dbt-ci.yml` and update:

```yaml
- name: Install dependencies
  run: |
    pip install dbt-your_warehouse sqlfluff dbt-checkpoint
```

## Testing the Setup

### 1. Test SQLFluff

```bash
sqlfluff lint models/
```

### 2. Test Pre-commit

```bash
pre-commit run --all-files
```

### 3. Test dbt Commands

```bash
dbt parse
dbt compile
dbt test --select test_type:unit
dbt test --select test_type:data
```

## Creating Your First Model with Tests

### 1. Create a Model

`models/staging/stg_customers.sql`:
```sql
SELECT
    customer_id,
    customer_name,
    email,
    created_at
FROM {{ source('raw', 'customers') }}
WHERE customer_id IS NOT NULL
```

### 2. Add Unit Tests

`models/staging/schema.yml`:
```yaml
unit_tests:
  - name: test_unit_stg_customers_filters_null_ids
    model: stg_customers
    given:
      - input: source('raw', 'customers')
        rows:
          - {customer_id: 1, customer_name: 'John', email: 'john@example.com', created_at: '2023-01-01'}
          - {customer_id: null, customer_name: 'Jane', email: 'jane@example.com', created_at: '2023-01-02'}
    expect:
      rows:
        - {customer_id: 1, customer_name: 'John', email: 'john@example.com', created_at: '2023-01-01'}
```

### 3. Add Data Tests

```yaml
models:
  - name: stg_customers
    description: "Cleaned customer data from raw source"
    meta:
      owner: "data-team"
      tier: "bronze"
    columns:
      - name: customer_id
        description: "Unique customer identifier"
        tests:
          - not_null
          - unique
      - name: customer_name
        description: "Customer full name"
        tests:
          - not_null
      - name: email
        description: "Customer email address"
        tests:
          - not_null
          - dbt_utils.expression_is_true:
              expression: "email LIKE '%@%'"
```

### 4. Run Tests

```bash
# Run unit tests first (TDD approach)
dbt test --select test_type:unit

# Run the model
dbt run --models stg_customers

# Run data tests
dbt test --select test_type:data --models stg_customers
```

## Best Practices

1. **Test-Driven Development**: Always write unit tests before implementing model logic
2. **Document Everything**: Add descriptions for all models and columns
3. **Use Meta Tags**: Include owner and tier information
4. **Run Tests Frequently**: Use pre-commit hooks and CI/CD
5. **Follow Naming Conventions**: Use consistent prefixes for different model types

## Troubleshooting

### SQLFluff Errors
- Check dialect configuration matches your warehouse
- Verify dbt profile is accessible
- Ensure proper indentation and SQL formatting

### Unit Test Failures
- Verify mock data matches expected schema
- Check model logic against test expectations
- Ensure all referenced models/sources are included in `given`

### Pre-commit Hook Failures
- Run `pre-commit run --all-files` to see all issues
- Fix formatting issues with `sqlfluff fix .`
- Add missing tests or documentation as indicated

For more detailed guidance, see the [dbt Best Practices Guide](dbt-best-practices.md).