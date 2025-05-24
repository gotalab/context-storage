# IDE Rules for dbt Projects

This repository contains IDE configurations and rules to enforce dbt best practices and test-driven development using dbt v1.8+ features.

## Overview

The rules in this repository help ensure:
- Compliance with dbt best practices
- Mandatory use of unit tests and data tests (dbt v1.8+)
- Test-driven development workflow
- Consistent code quality and documentation

## Structure

```
ide-rules/
├── vscode/           # VS Code specific configurations
├── sqlfluff/         # SQLFluff linting rules
├── pre-commit/       # Pre-commit hooks
├── github-actions/   # CI/CD workflows
└── docs/            # Documentation and examples
```

## Quick Start

1. Choose your IDE configuration from the appropriate directory
2. Copy the configuration files to your dbt project
3. Install required dependencies
4. Start developing with enforced best practices

See individual directories for detailed setup instructions.