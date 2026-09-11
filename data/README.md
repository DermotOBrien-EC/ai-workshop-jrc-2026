# The run records

Two files, copied byte for byte from the experiment repository
https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26
at commit `b352093193ad927de2d6626e07c4341157f4825d` (6 September 2026), the
commit the 6 September audit read.

| File | Source path there | SHA-256 |
|---|---|---|
| `results.csv` | `runs_2026_09/results.csv` | `e5539d16e8e0d00d23a6eb02bf26a4807207e6a9368143ed8f22367fb8ef8633` |
| `scoring.json` | `runs_2026_09/scoring.json` | `20da8db219d8afe685262c64cabd2638bf377e4be86febcd6a1ec03e66a7433c` |

`results.csv` has one row per September attempt (83 rows): the model, the
request length, the method the assistant put forward, the error recomputed
from its saved forecast (`mape_pct`, with `rmse_mw` and `mae_mw`), the error
the assistant itself reported, where the score came from (`source`:
`recomputed`, `agent_reported` or `none`), the time alignment of the scored
week, and the reason that file and column were scored.

`scoring.json` holds the audit's per-attempt fields for the same 83 attempts.
The fields are described in the top-level README under "What the audit
checked"; the definitions come from `runs_2026_09/DESIGN.md`, sections 5.1 to
5.3, in the experiment repository.

The charts in `figures/` are drawn from these two files by
`figures/make_experiment_figures.py` and `figures/make_stacked_figures.py`.
