#!/usr/bin/env python3
"""
Check that all dbt models have corresponding data tests.
This script enforces test-driven development by ensuring data tests exist.
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


def find_data_tests() -> Set[str]:
    """Find all data tests for models."""
    tested_models = set()
    
    # Check for data tests in YAML files
    for yaml_file in Path(".").rglob("*.yml"):
        try:
            with open(yaml_file, 'r') as f:
                content = yaml.safe_load(f)
                
            if not content:
                continue
                
            # Look for models with tests
            if 'models' in content:
                for model in content['models']:
                    if 'name' in model and ('tests' in model or 'columns' in model):
                        model_name = model['name']
                        
                        # Check for model-level tests
                        if 'tests' in model and model['tests']:
                            tested_models.add(model_name)
                        
                        # Check for column-level tests
                        if 'columns' in model:
                            for column in model['columns']:
                                if 'tests' in column and column['tests']:
                                    tested_models.add(model_name)
                                    break
                        
        except yaml.YAMLError:
            continue
    
    # Also check .yaml files
    for yaml_file in Path(".").rglob("*.yaml"):
        try:
            with open(yaml_file, 'r') as f:
                content = yaml.safe_load(f)
                
            if not content:
                continue
                
            if 'models' in content:
                for model in content['models']:
                    if 'name' in model and ('tests' in model or 'columns' in model):
                        model_name = model['name']
                        
                        if 'tests' in model and model['tests']:
                            tested_models.add(model_name)
                        
                        if 'columns' in model:
                            for column in model['columns']:
                                if 'tests' in column and column['tests']:
                                    tested_models.add(model_name)
                                    break
                        
        except yaml.YAMLError:
            continue
    
    # Check for standalone test files
    tests_dir = Path("tests")
    if tests_dir.exists():
        for sql_file in tests_dir.rglob("*.sql"):
            # Extract model name from test file content
            try:
                with open(sql_file, 'r') as f:
                    content = f.read().lower()
                    
                # Look for ref() calls to identify tested models
                import re
                ref_matches = re.findall(r"ref\s*\(\s*['\"]([^'\"]+)['\"]", content)
                for model_name in ref_matches:
                    tested_models.add(model_name)
                    
            except Exception:
                continue
    
    return tested_models


def get_required_tests() -> List[str]:
    """Get list of required test types from configuration."""
    return ['not_null', 'unique']  # Minimum required tests


def main():
    """Main function to check data test coverage."""
    models = find_model_files()
    tested_models = find_data_tests()
    
    missing_tests = models - tested_models
    
    if missing_tests:
        print("❌ The following models are missing data tests:")
        for model in sorted(missing_tests):
            print(f"  - {model}")
        print("\n📝 To fix this, add data tests to your model YAML files:")
        print("""
models:
  - name: {model_name}
    description: "Model description"
    columns:
      - name: id
        description: "Primary key"
        tests:
          - not_null
          - unique
      - name: other_column
        description: "Other column"
        tests:
          - not_null
    tests:
      - dbt_utils.unique_combination_of_columns:
          combination_of_columns: ['col1', 'col2']
""")
        return 1
    
    print(f"✅ All {len(models)} models have data tests!")
    return 0


if __name__ == "__main__":
    sys.exit(main())