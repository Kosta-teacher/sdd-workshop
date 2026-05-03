# Todo App

Simple CLI Todo application for managing tasks.

## Installation

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

## Usage

### Add Todo Items

```bash
# Basic item
todo add "Buy groceries"

# With priority
todo add "Fix bug #123" --priority high
```

### List Items

```bash
# All items
todo list

# Filter by status
todo list --filter done

# Filter by priority
todo list --priority high
```

### Mark as Done

```bash
todo done 1
```

### Delete Items

```bash
todo delete 2
```

## Development

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=todo_lib --cov=cli
```

## Data Storage

Data is stored in `todo.db` SQLite file in the current directory.