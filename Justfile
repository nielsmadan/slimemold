[private]
default:
    @just --list

setup:
    @uv sync --locked --all-groups
    @lefthook install

test:
    @uv run --locked pytest -q

coverage:
    @uv run --locked pytest --cov --cov-report=term-missing -q

format:
    @uv run --locked ruff format

check-static:
    @uv run --locked ruff check
    @uv run --locked ruff format --check
    @uv run --locked mypy

check: check-static coverage
