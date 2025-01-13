setup: install make lint build package-install

test: install build package-install brain-even

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

brain-even:
	uv run brain-even