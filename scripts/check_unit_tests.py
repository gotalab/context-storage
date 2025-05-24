#!/usr/bin/env python3
"""
Check that all dbt models have corresponding unit tests (dbt v1.8+).
This script enforces test-driven development by ensuring unit tests exist.
"""

import os
import sys
import yaml
from pathlib import Path
from typing import Set, List, Dict, Any


def find_model_files() -> Set[str]:
    """Find all dbt model files."""
    models = set()
    models_dir = Path("models")
    
    if not models_dir.exists():
        return models
    
    for sql_file in models_dir.rglob("*.sql"):
        # Skip files that start with underscore (private models)
        if not sql_file.stem.startswith("_"):
            models.add(sql_file.stem)
    
    return models


def find_unit_tests() -> Set[str]:
    """Find all unit tests for models."""
    unit_tests = set()
    
    # Check for unit tests in YAML files
    for yaml_file in Path(".").rglob("*.yml"):
        try:
            with open(yaml_file, 'r') as f:
                content = yaml.safe_load(f)
                
            if not content:
                continue
                
            # Look for unit_tests key (dbt v1.8+)
            if 'unit_tests' in content:
                for test in content['unit_tests']:
                    if 'model' in test:
                        unit_tests.add(test['model'])
                        
        except yaml.YAMLError:
            continue
    
    # Also check .yaml files
    for yaml_file in Path(".").rglob("*.yaml"):
        try:
            with open(yaml_file, 'r') as f:
                content = yaml.safe_load(f)
                
            if not content:
                continue
                
            if 'unit_tests' in content:
                for test in content['unit_tests']:
                    if 'model' in test:
                        unit_tests.add(test['model'])
                        
        except yaml.YAMLError:
            continue
    
    return unit_tests


def main():
    """Main function to check unit test coverage."""
    models = find_model_files()
    unit_tests = find_unit_tests()
    
    missing_tests = models - unit_tests
    
    if missing_tests:
        print("❌ The following models are missing unit tests:")
        for model in sorted(missing_tests):
            print(f"  - {model}")
        print("\n📝 To fix this, create unit tests in your YAML files using dbt v1.8+ syntax:")
        print("""
unit_tests:
  - name: test_{model_name}
    model: {model_name}
    given:
      - input: ref('source_table')
        rows:
          - {{col1: 'value1', col2: 'value2'}}
    expect:
      rows:
        - {{output_col: 'expected_value'}}
""")
        return 1
    
    print(f"✅ All {len(models)} models have unit tests!")
    return 0


if __name__ == "__main__":
    sys.exit(main())