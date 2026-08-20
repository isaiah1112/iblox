# AGENTS.md

## Project overview

This repository contains the `iblox` Python package for interacting with Infoblox WAPI endpoints.

- Library source: `src/iblox/`
- Tests: `test/test_iblox.py`
- Documentation sources: `docs/source/`
- Packaging metadata: `pyproject.toml`

## Required Python environment

Always use the project-local virtual environment for Python-related work.

- Preferred interpreter: `.venv/bin/python`
- Preferred test runner: `.venv/bin/python -m pytest`
- Never use a bare `python`, `pip`, or `pytest` from the system PATH when working in this repository.
- If a shell session needs activation, run: `. .venv/bin/activate`

This repository already includes a local `.venv/`; use it for all module execution, testing, linting, and dependency checks.

## Setup and validation commands

From the repository root:

```bash
# Create or refresh the repo-local environment if needed
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r docs/requirements.txt
python -m pip install pytest coverage requests-mock ruff
```

For normal validation:

```bash
. .venv/bin/activate
python -m pytest -q
python -m ruff check .
```

If you are working directly with the project environment without activating it:

```bash
./.venv/bin/python -m pytest -q
./.venv/bin/python -m ruff check .
```

## Repo-specific guidance

- Keep changes aligned with the package layout under `src/iblox/`.
- Preserve compatibility with the supported Python versions declared in `pyproject.toml`.
- Update focused tests in `test/` when changing behavior or adding features.
- Prefer small, targeted edits over broad refactors.
- If a command requires Python execution, route it through `.venv/bin/python` rather than a global interpreter.

## Notes for agents

- Treat `.venv` as the authoritative environment for this repo.
- Do not install packages globally for this project.
- If you need to run a Python module, use the local venv interpreter explicitly.
