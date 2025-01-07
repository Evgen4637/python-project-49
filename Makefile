setup: install make lint build package-install brain-games

install:
	uv sync

make lint:
	uv run ruff check brain_games

build:
	uv build

package-install:
	uv tool install dist/*.whl

brain-games:
	uv run brain-games