setup: install make lint build package-install

t-even: install make lint build package-install brain-even

t-calc: install make lint build package-install brain-calc

t-gcd: install make lint build package-install brain-gcd

t-prog: install make lint build package-install brain-progression

t-prime: install make lint build package-install brain-prime

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

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime