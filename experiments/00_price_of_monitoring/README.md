# 00 — Is the price of continuous monitoring measurable here at all?

**Status:** preregistered, not yet run.

Two cheap questions in one evening, before anything else is built.

## Questions

1. **Calibration.** Does applying a fixed-horizon test at every step inflate the false-alarm
   rate above nominal in this harness? If it does not, the harness is broken and no later
   number means anything.
2. **Premise.** At an equal false-alarm level, does the median detection delay differ between
   an e-detector and a fixed-horizon test in at least one realistic cell?

## Why it must run first

The project claims that continuous monitoring has a measurable price on rare items. If that
price is invisible at realistic rarities and understatements, there is no map to draw, and
finding this out costs six hours instead of eighty.

Two traps this design avoids:

**Comparing speed at unequal error control.** A method with a looser guarantee detects faster
for trivial reasons. Every comparison here is made only after the empirical false-alarm rates
are matched, and the matching is shown as a number.

**Forgetting the censored streams.** Streams where nothing is detected within the horizon are
not dropped — dropping them silently makes slow methods look fast. They are reported as a
share alongside the median.

## Setup

A single item from a real published drop table. Claimed rate `p₀`; true rate `p₁ = p₀·(1−δ)`
for a small set of understatement sizes `δ`. Many independent streams, common random numbers
across methods.

Rarity levels span the realistic published range — from common items around `p₀ = 0.05` to
headline items around `p₀ = 0.005`. Horizon fixed in advance.

Under the null (`δ = 0`) the empirical false-alarm rate is measured for every method,
including the naive one. Under the alternative, detection delay is recorded.

## Preregistered pass criterion

**Blocking, both parts:**

- **A** — naive peeking exceeds the nominal false-alarm rate, with an interval excluding the
  nominal level;
- **B** — in at least one cell, the paired difference in median detection delay between the
  e-detector and the fixed-horizon test has a bootstrap interval excluding zero, at matched
  false-alarm rates.

Rarity levels, understatements, horizon, number of streams, α and the interval method go into
`protocol.md` **before** the run and are not adjusted afterwards.

## Outcomes

| Result | Action |
|---|---|
| A and B hold | Proceed to phase 1; the cell where the difference is largest tells phase 4 where to spend its grid. |
| A holds, B does not | The price is not measurable at these rarities. Reformulate to the pure detectability map — how many openings a regulator needs at all — rather than softening the comparison. |
| A fails | Stop and fix the harness. Nothing else is trustworthy until peeking demonstrably inflates the error. |

## Run

```bash
uv run python experiments/00_price_of_monitoring/run.py --config configs/monitoring_probe.yaml
```

`run.py` is written by the author once the stream simulator exists — see
[LEARNING.md](../../LEARNING.md). This README is the contract it has to satisfy.
