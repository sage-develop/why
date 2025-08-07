# UV Commands Reference

This document provides a quick reference for common UV commands used in this project.

## Dependency Management

- **Add a new dependency:**
  ```bash
  uv add package-name
  ```

- **Add a development dependency:**
  ```bash
  uv add --dev package-name
  ```

- **Remove a dependency:**
  ```bash
  uv remove package-name
  ```

- **Update dependencies:**
  ```bash
  uv sync --upgrade
  ```

## Running Code

- **Run a Python script:**
  ```bash
  uv run python your_script.py
  ```

- **Run a command in the project environment:**
  ```bash
  uv run command
  ```

## Environment Management

- **Sync dependencies (install/update virtual environment):**
  ```bash
  uv sync
  ```

- **Activate the virtual environment (optional):**
  ```bash
  source .venv/bin/activate
  ```
  Note: UV automatically uses the project's virtual environment, so activation is typically optional.

## Additional Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub Repository](https://github.com/astral-sh/uv) 