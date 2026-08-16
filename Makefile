PROBE ?= configs/monitoring_probe.yaml

.PHONY: install test lint check kill-test

install:
	uv sync --extra dev --extra stats

test:
	uv run pytest

lint:
	uv run ruff check .

check: lint test

## Phase 0 — the preregistered kill-test.
## Thresholds live in the experiment's protocol.md and are fixed before the run.
kill-test:
	uv run python experiments/00_price_of_monitoring/run.py --config $(PROBE)
