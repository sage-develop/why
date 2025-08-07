# Why - AI Experiments

## Development Setup

This project uses [UV](https://docs.astral.sh/uv/) for fast Python package and project management.

### Prerequisites
- Python 3.13+

### Setup Instructions

#### Step 1: Install UV

**Option 1: Using Homebrew (Recommended)**
```bash
brew install uv
```

**Option 2: Using curl**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, verify UV is working:
```bash
uv --version
```

For other installation methods, see the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/).

#### Step 2: Clone and navigate to the project
```bash
git clone https://github.com/sage-develop/why.git
cd why
```

#### Step 3: Install dependencies and create virtual environment
```bash
uv sync
```
This command will:
- Create a virtual environment in `.venv/`
- Install all dependencies from `pyproject.toml`
- Generate a `uv.lock` file for reproducible builds

#### Step 4: Activate the virtual environment (optional)
```bash
source .venv/bin/activate
```
Note: UV automatically uses the project's virtual environment, so activation is optional.

### Daily Development

For common UV commands and additional usage examples, see [docs/uv.md](docs/uv.md).

### Project Structure

- `docs/` - Documentation files
  - `uv.md` - UV commands reference
- `products/` - Product documentation and specifications
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Locked dependency versions (auto-generated)
- `questions.md` - Main project questions and tasks


### To convert pdf to txt
```bash
uv run src/pdf2txt.py <file.pdf> <file.txt>
```