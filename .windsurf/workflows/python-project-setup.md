---
description: Use this workflow to set up the python project init.
---


Follow these steps to spin up a **brand‑new Python project** managed by **uv**:

1. **Create the project directory**

   ```bash
   mkdir myproject && cd myproject
   ```

2. **Generate the project scaffold**

   ```bash
   # Create a fresh virtual environment and all boilerplate
   uv init --python 3.12 --git --readme
   ```

   This command will:

   * Download Python 3.12 (if not already cached) and create a `.venv/`
   * Generate `pyproject.toml`, `uv.lock`, `.python-version`, and `README.md`
   * Initialize a Git repository (omit with `--bare`)

3. **Activate the environment & run your first command**

   ```bash
   uv run python -m pip list
   ```

   `uv run` automatically activates the project’s virtual environment before executing the given command.

4. **Add runtime and development dependencies**

   ```bash
   uv add <package_name>
   uv add --dev pytest
   ```

5. **Lock & sync in CI**

   ```bash
   uv lock --check        # verify lock file is up‑to‑date
   uv sync --check        # ensure the environment matches uv.lock
   ```

6. **Push to GitHub**

   ```bash
   git add .
   git commit -m "Initial uv project"
   git push origin main
   ```

That’s it — your new project is reproducible, fast, and ready for development!
