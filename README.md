# AI in the Research Workflow: one experiment, and what it taught me

Dermot O'Brien's part of the workshop **AI in the Research Workflow**, held at
the European Commission's Joint Research Centre (JRC) on **11 September 2026**.
This repository holds the slides, the numbers behind them, the exact requests
that were given to the AI assistants (the two short ones quoted, the long one
linked), and the instructions to rebuild the slides, redraw the charts or try
a similar experiment yourself.

| | |
|---|---|
| Slides, in the browser | https://dermotobrien-ec.github.io/ai-workshop-jrc-2026/ |
| Slides as a PDF (44 pages) | [output/workshop-2026-09-11.pdf](output/workshop-2026-09-11.pdf) |
| Every attempt, every file | The [experiment repository](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26), read at commit `b352093` |
| The audit behind the numbers | [WORKSHOP_REVIEW.md](WORKSHOP_REVIEW.md) |
| Set up the tools and try it yourself | [Get the tools running](#get-the-tools-running-on-your-own-computer), then [Try a similar experiment](#try-a-similar-experiment-yourself) |

The deck has 44 slides: 29 in the main route, written as a 30-to-40-minute
talk for scientists and civil servants, many of whom had never used an AI
assistant, and 15 backup slides that hold the evidence. Its one message:
**ask, then check.**

## The story, in plain language

In May 2026 I gave one forecasting task to an AI assistant in three ways. The
task: standing at midnight on 1 January 2020, predict Germany's electricity use
for every hour of the next seven days, 168 hours in all. The three requests
were 10 words; 46 words plus 7 lines of standing instructions; and 1,673 words
plus 113 lines of standing instructions. (Standing instructions are a file
placed in the folder for the assistant to read before it starts, describing
how you like work done; the records log when each attempt read it.) The long
request produced a six-method study with a written report and scored best: an
average error of 3.4%, against 5.5% and 10.8% for the two shorter requests. It
looked like proof that detail wins.

In September 2026 I ran the whole thing again: 83 attempts between 3 and 6
September, with the newest models from Anthropic and OpenAI, the May model and
its successors again for comparison, and a newer version of the software
around the model. That software is called the harness: the program that lets
the model read your files, run code and hand back results. Comparing the new
attempts with the May winner showed that the May winner had not made a fair
forecast. Its method used the electricity use exactly 24 hours earlier as an
input. On 1 January that value was known; for 2 to 7 January it had not
happened yet. A fair forecast fills those hours with its own predictions. The
May code plugged in the real numbers, so for six of the seven days the
forecast was partly copying the answers. The same method, run in September by
Claude Fable 5.1, scored 3.7% with the real numbers and 5.5% without them. The
peek was worth almost two points of error. That, not skill, is why May's 3.4%
looked so good.

Meanwhile a ten-word request to the newest Claude produced a proper forecast
with a range showing how sure it was. Its average error was 3.3%, the best of
three attempts, and the audit found no use of the answers in the forecast
itself. (The record does note that two simple reference methods were scored on
the same week beside it; the chosen method had been fixed before any test score
existed.) With my 1,673-word recipe the same assistant scored about 5%. The
recipe had fixed choices the assistant made better on its own.

OpenAI's newest model, GPT-6-Astra, read the long instructions and stopped to
ask, in short: do you want one forecast for all 168 hours made on 1 January,
or should I update my inputs as the real numbers arrive? That is the exact
ambiguity behind the May mistake. Across OpenAI's three models, 20 of 27
attempts stopped to ask a question or propose a plan instead of forecasting.
In the original September group of 12 Claude attempts (Fable 5.1 and Opus 5),
0 of 12 stopped; they got on with the work. The OpenAI models ran through a
different route with different default settings, so this compares two
set-ups, not two companies. Nobody was there to answer, so I re-ran the 20
stopped attempts with one added paragraph saying the session was unattended
and the assistant should decide for itself and state its assumptions. 0 of 20
stopped, and 19 of 20 produced a score.

What I took from it: describe the goal and what would make the result valid.
Ask the assistant how it would approach the task and what it needs from you.
Let it ask. Then check its work yourself, because its report is a claim, not
evidence. The skill has moved from writing perfect instructions to asking good
questions and judging the answers.

### The numbers, and where each one comes from

Every number on the slides, except the second AI's marks, was checked against
the run records and the attempt files on 6 September 2026; the audit is in
[WORKSHOP_REVIEW.md](WORKSHOP_REVIEW.md). The charts and the second AI's marks
were added on 10 September from the same records. "Average error" is the mean
absolute percentage error (MAPE): for each of the 168 hours, how far the
forecast was from the true value as a percentage of it, averaged over the
week. Lower is better. The slides round to one decimal.

| Number | What it is | Slide | Record |
|---|---|---|---|
| 10.8%, 5.5%, 3.4% | May 2026, one attempt per request (full precision 10.76, 5.52, 3.43) | In May, more detail looked like a better forecast | `runs/L1`, `L2`, `L3` metrics files in the experiment repository |
| 3.7% and 5.5% | One September method scored with the real numbers and with its own predictions (3.71 and 5.53; Fable 5.1, 1,673 words, attempt 3) | The same method, with and without the peek | `runs_2026_09/fable51_L3_r3/output/metrics.json` |
| 3.3% | Ten words, Fable 5.1, attempt 2 (3.284; its siblings scored 3.96 and 4.49, the third flagged for changing inputs after seeing the test score) | Ten words in September: a real 3.3% | `data/results.csv`, rows `fable51_L1_r1` to `r3` |
| 5.03%, 4.99%, 5.53% | Fable 5.1's three 1,673-word attempts. All three fed the week their own predictions (the fair way); all three also named the winner by its test-week error, as the recipe ordered | The long recipe did not give Fable the lowest errors (backup) | `data/results.csv`, rows `fable51_L3_r1` to `r3` |
| 20 of 27; 0 of 12 | OpenAI attempts that stopped to ask or propose (Astra 9 of 9, Sol 6 of 9, GPT-5.5 5 of 9); Claude attempts in the original September group (Fable 5.1 and Opus 5) that did | It asked the question that exposes the May mistake | `data/scoring.json` |
| 0 of 20; 19 of 20 | With the unattended note: attempts that stopped; attempts that produced a score (16 recomputed, 3 the assistant's own number) | One paragraph, and a different outcome | `data/results.csv`, rows tagged `astraos`, `solos`, `gpt55os` |
| 83; 43, 17, 23 | September attempts; final scores recomputed from a saved forecast, only the assistant's own number, no score at all | Of the 83 attempts, 43 have a final score checked by us (backup) | `data/results.csv`, column `source` |
| 10.8% then 3.6%, 3.3%, 7.7% | The May model (Claude Opus 4.7) on the same ten words in May and in September (the 3.3% attempt is flagged) | Same model as May, new harness, different answer | `data/results.csv`, rows `opus47_L1_r1` to `r3` |

## What is in this repository

| Path | What it is |
|---|---|
| `index.qmd` | The slides: one Markdown file, one slide per `#` or `##` heading plus the title slide, speaker notes in `::: {.notes}` blocks. Copied unchanged from the presenters' joint repository (branch `dev_dermot`, commit `a32f01b`). |
| `_quarto.yml`, `ec-jrc.scss`, `assets/` | The deck's configuration and the EC/JRC slide theme (colours, type, logos, the footer and a small script that keeps the slide software from miscounting slides). |
| `figures/` | The seven images the slides show, the companion charts, and the two scripts that draw them from the records. See [Redraw the charts](#redraw-the-charts). |
| `data/results.csv`, `data/scoring.json` | The run records: one row per attempt with the recomputed score, and the audit's per-attempt fields. Byte-identical copies of `runs_2026_09/results.csv` and `runs_2026_09/scoring.json` at commit `b352093` of the experiment repository ([data/README.md](data/README.md) has the hashes). |
| `research/` | The AI-assisted review of 10 September: the script that ran it, the 62 reviews, and the aggregation script. [research/README.md](research/README.md) explains the method. |
| `PRESENTERS.md` | The timed route through the talk, what each section should leave behind, and the questions to expect. |
| `WORKSHOP_REVIEW.md` | The 6 September audit: what was checked, what was found, what remains unverified, with dated addenda up to the day of the workshop. |
| `docs/` | The rendered slides as published on GitHub Pages, plus the PDF. Regenerated by `scripts/build.sh`. |
| `output/workshop-2026-09-11.pdf` | The slides as a 44-page PDF. |
| `scripts/` | `build.sh` renders the slides and refreshes `docs/`; `export_pdf.sh` makes the PDF. |
| `LICENSE`, `NOTES.md` | The licence notice, and the notes of the unattended session that assembled this repository. |

## The slides

The slides are a web page, made with [Quarto](https://quarto.org) and
reveal.js: free tools that turn a text file into slides that open in any
browser. Open https://dermotobrien-ec.github.io/ai-workshop-jrc-2026/ and use
the arrow keys. Useful keys: `S` opens the speaker view with the notes (the
browser must allow a pop-up), `O` shows all slides at once, `F` is full
screen, `M` opens a menu to jump to any slide, `?` lists the shortcuts. The
speaker notes hold the sources for every number and the sentences the
presenter meant to say; they are worth reading if you want the evidence
behind a slide.

The PDF has no notes. To read them without a browser, open `index.qmd` in any
text editor: the notes are the `::: {.notes}` blocks under each slide.

## Build the slides yourself

You only need [Quarto](https://quarto.org/docs/get-started/), version 1.10 or
newer. No Python or R is needed: the deck has no executable code cells, so the
build only converts text.

```bash
git clone https://github.com/DermotOBrien-EC/ai-workshop-jrc-2026.git
cd ai-workshop-jrc-2026
quarto check                 # confirms the installation
quarto render index.qmd      # writes index.html + index_files/
quarto preview index.qmd     # or: a live preview that re-renders on every save
```

Then open `index.html` in a browser. If you copy the rendered deck somewhere
else, keep `index_files/`, `assets/` and `figures/` beside `index.html`, or use
the PDF. `scripts/build.sh` does the render and refreshes `docs/` in one step.

### PDF export

reveal.js prints one slide per page when the page is opened with `?print-pdf`
on the end of the address. Two routes:

1. **In the browser.** Open `index.html?print-pdf` in Chrome or Chromium,
   print (`Ctrl-P` or `Cmd-P`), choose *Save as PDF*, set *Margins* to *None*
   and tick *Background graphics* (without it the gradient slides come out
   white). Firefox handles reveal.js printing less well.
2. **From the command line**, with Google Chrome installed:
   `bash scripts/export_pdf.sh`. It serves the folder over a local web server
   (reveal.js needs that for printing), prints with Chrome running without a
   window, and writes `output/workshop-2026-09-11.pdf`. Set
   `CHROME=/path/to/chrome` if your browser is elsewhere. Expect 44 pages.

`quarto render index.qmd --to pdf` will **not** give you slides: that switches
the document to LaTeX, which ignores the theme. Always go through `?print-pdf`.

### If something looks wrong

| Symptom | What to do |
|---|---|
| A change to `ec-jrc.scss` does not show | Quarto caches the compiled theme. Hard-reload the browser; if that is not enough, `rm -rf .quarto index_files` and render again. |
| The slide count is wrong or a slide is blank | A fenced div that starts with a heading has become a stray `<section>`. `assets/head.html` fixes this automatically; make sure `_quarto.yml` still includes it. |
| Gradient slides have a white frame | `margin: 0` is missing from `_quarto.yml`. |
| The PDF has no backgrounds or logos | In the print dialogue set *Margins: None*, tick *Background graphics*, and check the address ends in `?print-pdf`. |
| An image does not appear | Paths are relative to `index.qmd`, so `figures/name.png`. File names are case-sensitive on Linux. |

## Redraw the charts

Five charts on the slides are drawn by two small Python scripts: three from the
two record files, one from the second AI's marks in `research/`, and the
coverage chart from six hit rates copied into the script from the three Fable
`metrics.json` files in the experiment repository. Running the scripts rewrites
the PNG files in `figures/` in place; the result should be identical to what is
committed (it was, byte for byte, when this repository was assembled).

```bash
uv run --no-project --with matplotlib python figures/make_experiment_figures.py
uv run --no-project --with matplotlib python figures/make_stacked_figures.py
```

If you do not use [uv](https://docs.astral.sh/uv/), `pip install matplotlib`
and run the scripts with `python`. They use the Arial font when it is
installed and fall back to matplotlib's default with a warning when it is not.

| File in `figures/` | What it shows | On the slides |
|---|---|---|
| `exp-all-levels.png` | One dot per scored attempt (60 of 83) on one error scale, one panel per request length; the 23 attempts without a score appear as a count at the right edge. Coral: the forecast itself peeked. Gold: peeked while choosing or checking. Grey: the audit could not decide. Hollow diamond: the assistant's own number, not rechecked. | One scale for all three request lengths |
| `exp-stopped.png` | How many OpenAI attempts stopped to ask or propose, per model, and how many stopped with the note (0 of 20). | How often the OpenAI models stopped to ask |
| `exp-checks-stacked.png` | Five good practices from the audit, averaged over each model's attempts at each request length; an attempt that stopped without a forecast counts as 0 on every practice. The counts behind each bar are in `exp-checks-stacked.notes.txt`. | What each request length bought in good practice |
| `exp-review-stacked.png` | The second AI's marks on five points, rescaled 0 to 1, averaged and stacked. Not checked by a person. The means are in `exp-review-stacked.notes.txt`. | I asked a second AI to mark all 62 pieces of work |
| `exp-coverage.png` | How often Fable 5.1's 80% and 95% ranges contained the true value, in its three 1,673-word attempts (57.1, 50.6, 48.8% and 94.0, 91.7, 83.3%; from `runs_2026_09/fable51_L3_r1` to `r3`, `output/metrics.json`). | Giving a range did not make the range reliable (backup) |
| `exp-rerun-l1-fable.png` | The forecast plot that attempt `fable51_L1_r2` itself produced. A byte-identical copy of `runs_2026_09/fable51_L1_r2/output/forecast_jan2020_week1.png`; not drawn by the scripts. | Ten words in September: a real 3.3% |
| `may-l3-winner.png` | The May winner's own chart, made with the peek. A byte-identical copy of `runs/L3/figures/05_winner_with_intervals.png`; not drawn by the scripts. | The May winner's chart was made with the peek (backup) |
| `exp-every-attempt.png`, `exp-attempts-*.png`, `exp-report-card*.png` | Companion charts from the same records: the dot chart in other layouts, and a report card of eight audit checks per model and request length. | Not on the slides |

## Get the tools running on your own computer

The experiment used AI assistants that run in a terminal window, read the
files in a folder, write code and run it. Two of them are easy to install. The
commands below were correct in September 2026; the two documentation pages
carry the current versions if they change.

| | Claude Code (Anthropic; runs Claude Fable 5.1) | Codex (OpenAI; runs GPT-6-Astra) |
|---|---|---|
| Documentation | https://code.claude.com/docs | https://developers.openai.com/codex |
| Needs | Node.js 18 or newer, then `npm install -g @anthropic-ai/claude-code` | Node.js 18 or newer, then `npm install -g @openai/codex` |
| Sign in | Run `claude` once; it opens a browser to sign in with a Claude account (a Pro or Max subscription) or lets you paste an API key that has credit | Run `codex` once; sign in with a ChatGPT account (Plus, Pro, Team or Enterprise) or paste an API key |
| Pick the model | Type `/model` inside the session and choose Fable 5.1 | Type `/model` inside the session and choose GPT-6-Astra, or start it with `codex -m gpt-6-astra` |
| Cost | Included in the subscription up to its limits; a ten-word attempt like the ones here is a few cents on an API key, a long one a few euros | The same |

Then, step by step:

1. Make a new, empty folder and put the data file in it (section 1 below).
2. Open a terminal in that folder (on a Mac: open Terminal, type `cd ` and drag the folder onto the window, press Enter).
3. Type `claude` or `codex` and press Enter. The first time, follow the sign-in it opens.
4. Paste one of the requests from section 2 as your first message. If you want the assistant to work without you, add the unattended paragraph from section 3; otherwise stay and answer its questions.
5. Both tools ask before running a command or writing a file. Say yes as they come, or start with the setting that pre-approves them (`claude --permission-mode auto`, or Codex's approval setting in its documentation) once you trust what they do in that folder.
6. Keep everything the assistant leaves behind and score it yourself (section 5).

Two cautions. Whatever is in the folder can be sent to the company running the model, so use public data, as this experiment did, or the tools your organisation has approved for anything else; at the Commission that means the internal services named in the staff guidance. And the OpenAI attempts in this experiment did not use Codex itself: they ran through Claude Code and a local gateway, which is one reason the results are not a vendor ranking. If you use Codex directly you are running a cleaner comparison than we did.

## Try a similar experiment yourself

Everything below is what the September experiment did, reduced to the steps a
reader can repeat. You need a forecasting task with a known answer that the
assistant is not supposed to look at, one request, and a way to score the
result yourself. The full design, with its reasons, is
[runs_2026_09/DESIGN.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/runs_2026_09/DESIGN.md)
in the experiment repository. It was written before the runs and reviewed
twice before any attempt was launched.

### 1. Get the data

The experiment used Germany's hourly electricity load from
[Open Power System Data](https://data.open-power-system-data.org/time_series/),
which derives it from the ENTSO-E Transparency Platform: the column
`DE_load_actual_entsoe_transparency` of the 60-minute time-series package, from
1 January 2015 00:00 to 30 September 2020 23:00 UTC. That is 50,400 hourly rows
with no gaps. (UTC is the international reference time; German clocks are one
hour ahead of it in winter.) The experiment repository's
[scripts/fetch_data.py](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/scripts/fetch_data.py)
downloads exactly that file, and the copy it produced is at
[data/opsd_de_load.csv](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/data/opsd_de_load.csv)
there.

Note what the experiment did on purpose: the file the assistant received
contained the target week too. The assistant was expected not to use it. That
is the realistic case (your data usually contains what you are asking about),
and it is what makes the check in step 6 necessary.

### 2. Choose a request

The three requests, exactly as given. They are frozen in the experiment
repository under `prompts/`, with checksums (fingerprints that show a file is
unchanged) in `runs_2026_09/pins.sha256`.

**10 words**
([prompts/L1.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/prompts/L1.md)),
no standing instructions:

> Forecast first week of January 2020 German hourly electricity load.

**46 words**
([prompts/L2.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/prompts/L2.md)),
with a 7-line standing-instructions file
([runs/L2/AGENTS.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/runs/L2/AGENTS.md)):

> Build me a Python script that forecasts German hourly electricity load for
> the first week of January 2020 (the 168 hours from 2020-01-01 to 2020-01-07).
> Train on the historical data, produce the forecast, plot it against the
> actual values, and tell me how accurate it was.

**1,673 words**
([prompts/L3.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/prompts/L3.md)),
with a 113-line standing-instructions file
([runs/L3/AGENTS.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/runs/L3/AGENTS.md)).
A full brief: six named methods to compare, the inputs allowed and forbidden,
the training, validation and test periods, the metrics, eight figures, the
output files, and a list of things not to do. It asks for the "24 hours
earlier" input, and it names the winner as the method with the lowest error on
the test week while elsewhere forbidding the test week for choosing the method.
Both of those turned out to matter (see the backup slide *Long instructions
can contradict themselves without anyone noticing*).

### 3. Decide who answers questions

If you will be there, let the assistant ask; a good question can be the most
valuable thing it produces. If nobody will be there, add this paragraph. It is
the exact text used in September
([prompts/one_shot_suffix.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/prompts/one_shot_suffix.md)):

> Note from the operator: this session is unattended. Nobody can answer a
> question or approve a plan, so do not stop to ask or to propose. Make the
> most reasonable choice for anything unclear, say what you assumed in your
> final message, and finish the whole job in this session.

In September this paragraph was an experimental step, added only to the 20
attempts that had stopped. It is not blanket permission: the assistant still
worked inside a restricted folder it could not act outside of, and what it
may do without asking is something you decide for each task.

### 4. Run it

The attempts used an AI coding assistant that can read files and run code on
your computer. For Anthropic's models this was Claude Code (build 2.1.259).
OpenAI's models were reached through the same tool and a local gateway, a
small program on the same computer that passed the tool's requests on to
OpenAI's models; that is not OpenAI's own tool, and it is one reason the
results are not a vendor ranking. Any assistant that can run code will do for
your own trial; the section above says how to install the two used here.

- Put the data file alone in a fresh folder. If the request comes with
  standing instructions, save them there under the file name your tool expects;
  in the experiment that file was `AGENTS.md`, and the records log the moment
  each attempt read it.
- Start the assistant in that folder and paste the request as the first
  message. Change nothing else. The experiment sent one message and let each
  attempt run to its end with nobody at the keyboard; if you sit with yours,
  you can answer its questions instead of adding the paragraph above.
- Keep everything it leaves behind: code, forecast file, figures, write-up,
  final message, and the transcript if your tool saves one. The experiment
  kept one folder per attempt with exactly that.
- Run each request more than once. Three attempts at the same request gave
  errors from 3.3% to 4.5% in one case and 2.3% to 5.4% in another; one run
  tells you little.

### 5. Score it yourself

The rule that makes a result valid: **the forecast may use only information
that existed before 1 January 2020 00:00 UTC.** In particular, for 2 to 7
January any "yesterday" or "last hour" input (a lag: an earlier value used as
an input) must be the model's own earlier prediction, not the real value. The
method should be chosen on earlier data and fixed before the target week is
looked at. Say whether times are UTC or local: some attempts forecast a week
one hour off the others because the request did not say.

Score the saved forecast file against the real values on the 168 hours it is
stamped with, and compute the average error yourself. Do not take the
assistant's number: in September, 17 of 83 attempts reported a score with no
forecast file that could be rescored. The design said any recomputed value
more than 0.05 points from the assistant's own would be flagged and explained
(`DESIGN.md`, section 5.1). A minimal scorer follows. Rename the assistant's
columns to `timestamp` and `forecast_mw` first, or edit the two names in the
script; it accepts timestamps with or without a time zone and treats both as
UTC.

```python
import pandas as pd

actual = pd.read_csv("opsd_de_load.csv")
actual.index = pd.to_datetime(actual["utc_timestamp"], utc=True)
actual = actual["DE_load_actual_entsoe_transparency"]

forecast = pd.read_csv("forecast.csv")
forecast.index = pd.to_datetime(forecast["timestamp"], utc=True)
forecast = forecast["forecast_mw"]

hours = forecast.index.intersection(actual.index)
assert len(hours) == 168, f"only {len(hours)} hours matched: check the column names and the time zone"
mape = (abs(forecast[hours] - actual[hours]) / actual[hours]).mean() * 100
print(f"{len(hours)} hours scored, from {hours.min()} to {hours.max()}, average error {mape:.2f}%")
```

Run on two saved forecasts from the experiment repository, this script gave
the same values as `data/results.csv` (3.284% for `fable51_L1_r2`, on its
week shifted one hour from UTC, and 2.298% for `fable51_L2_r1`).

For reference, the May ten-word attempt's 10.8% is what a rule of thumb gets
(the same hour 364 days earlier); a fair forecast from a modern method scores
about 3 to 5% on this week; and the May winner's 3.4% was made with the peek.

### 6. Check where it used the data

This is the step the May experiment skipped. Read the code, not the final
message, and ask:

- Did the delivered forecast itself read values from the target week, for
  example through the "24 hours earlier" input or a rolling average computed
  over the whole series? That is the peek; the score is not a forecast.
- Were several methods or settings compared on the target week before one was
  chosen? The chosen one then looks better than it is. The audit calls this
  `test_selected` and records how many candidates were compared.
- Did anything change after the assistant saw a test score (a new input, a
  different window, a retuned setting)? Ask the assistant; then check the
  transcript.
- Did it test on earlier data that it had kept back from training before
  choosing? Did it give a range? Did it write up what it did? These do not
  make a result valid, but they make it easier to check.

### The records to compare with

All of these are in the experiment repository at commit `b352093`
([browse it](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/tree/b352093193ad927de2d6626e07c4341157f4825d)).

| Path there | What it holds |
|---|---|
| `runs_2026_09/<model>_<level>_r<n>/` | One folder per September attempt, holding among other files `final_message.md` (what the assistant said it did), `summary.json`, `output/` (its code, forecast, figures and write-up) and `session.jsonl` (the full transcript). |
| `runs_2026_09/results.csv` | One row per attempt: the recomputed error, the assistant's own number, whether the score was recomputed, and the time alignment. Copied here as `data/results.csv`. |
| `runs_2026_09/scoring.json` | The audit's per-attempt fields, described in the next section. Copied here as `data/scoring.json`. |
| `runs_2026_09/DESIGN.md`, `RESULTS.md` | The design, written before the runs, with its review record; and the write-up. |
| `runs_2026_09/pins.sha256` | Checksums of the frozen prompts, data and instruction files. |
| `runs/L1`, `runs/L2`, `runs/L3` | The May 2026 attempts, including the winner's code (`runs/L3/code/lightgbm_features.py`, where the peek is). |
| `scripts/score_runs.py` | The scorer that recomputed every error. |

## What the audit checked

For each of the 83 attempts, `data/scoring.json` records the fields below.
Each attempt was classified from its code and transcript by an independent
reader working read-only against a fixed list of fields: GPT-5.6-Sol for the
original twelve attempts, GPT-6-Astra for the 71 later ones. Every
load-bearing field was then re-checked against the files and the transcript
by the experiment's orchestrator (Claude Fable 5.1, working with the
presenter) before it entered the results (`DESIGN.md`, section 5.3). On 6
September the 43 recomputed scores were recalculated once more from the saved
forecasts; all agreed with the record within rounding.

| Field | Meaning |
|---|---|
| `model_tag`, `model_label`, `level`, `rep` | Which model, which request length (`L1` 10 words, `L2` 46 words, `L3` 1,673 words), which of the attempts. Tags ending in `os` (for the one-shot note) received the unattended paragraph. |
| `file`, `column`, `reason` | The saved forecast file and column that was scored, and why that one. |
| `headline_model` | The method the assistant put forward as its answer. |
| `headline_prespecified` | Whether that method was fixed before any test score existed. |
| `agent_reported_mape` | The error the assistant itself reported. |
| `n_models_fitted`, `n_candidates` | How many methods it fitted; how many were compared on the test week before choosing. |
| `validation` | Whether a test on earlier data, kept back from training, guided a choice (only counts if the choice depended on it). |
| `intervals` | Whether it gave a range, lower and upper bounds, for the test week. |
| `methods_doc` | Whether it wrote a methods, results or README file. The final chat message does not count. |
| `test_selection` | How the target week was used: `final_scoring_only` (only to score the finished forecast), `test_selected` (candidates compared on it and the best put forward), `leaked` (its values entered fitting, inputs or tuning), `indeterminate` (the transcript does not allow a call), or `n/a (no forecast)`. |
| `leak_scope` | Recorded for 18 of the 21 `leaked` attempts: what the target-week data touched (the delivered forecast itself, the selection stage, a labelled supplement, and so on). |
| `status_note` | How the attempt ended when it did not finish normally (time cap, ended while a job was still running). |
| `audit_note` | The auditor's account of the attempt in a few sentences. |
| Occasional fields | `selection_free_mape` (6 attempts: the error of the method a fair selection would have chosen, where it can be read from the files), `used_codex` (1: the attempt called a second AI tool), `naive_tz`, `time_col`, `surviving_forecast` (1 each: how an unusual forecast file was read). |

`data/results.csv` adds the recomputed error (`mape_pct`, with `rmse_mw` and
`mae_mw`), the `source` of the score (`recomputed` from a saved forecast,
`agent_reported` with nothing to rescore, or `none`) and the `alignment`
(scored on the UTC week, or on a week shifted one hour because the forecast
was stamped in local time).

## The second AI's marks

On 10 September a second AI, Claude Opus 5, was asked to read each of the 62
attempts that had done forecasting work (the 60 with a score, plus two with
forecast work but no final score) and give five marks, 1 to 3, with a line of
evidence each: code quality, sound method, honest reporting, good decisions,
complete deliverables. It also gave its own verdict on whether the forecast
had peeked. One reviewer per attempt, read only, no comparison between
attempts. The result is a chart on the slides and the full record in
[research/](research/).

**These marks were not checked by a person.** They are one AI's reading of
another AI's work, made after the audit and outside it; for the nine Opus 5
attempts the reviewer was the same model as the author. The reviewers found
the same three peeking forecasts the audit found and one more, and were more
lenient than the audit on attempts that had used the target week while
choosing. The audit remains the authority; the marks are a fast first check.
[research/README.md](research/README.md) has the rubric and the way the run
was made.

## What this evidence can and cannot say

- One dataset, one forecast week, and few repeats: three attempts per model
  and request length at most. It is a case study, not a benchmark.
- It is not a ranking of companies. The OpenAI models ran through a different
  route with different default settings, not OpenAI's own tool; the harness,
  its settings and the way attempts were run changed between May and
  September; and the request lengths change the instructions, the required
  outputs and the modelling choices together, so they do not isolate detail.
- The unattended-note comparison re-ran only the attempts that had stopped,
  with no control re-run without the note, so it is an observed association.
- Of 83 attempts, 43 have a score recomputed from a saved forecast, 17 have
  only the assistant's own number, and 23 have no score. Eight recomputed
  forecasts cover a week in local time, one hour off the others, and are
  scored on the week they actually predicted.
- The presenter's remarks about how he works with the newest models are
  personal experience, labelled as such on the slides; the experiment did not
  measure conversational tone or intent recognition.
- Evidence cutoff: 6 September 2026. The charts and the second AI's marks were
  added on 10 September from the same records. WORKSHOP_REVIEW.md lists what
  remains unverified.

## Credits, licence and provenance

**Presenter.** Dermot O'Brien, Joint Research Centre, European Commission.
The workshop and its slide theme were built with Andrés L. Marin and Ilyas
Tiouassiouine; their sections of the workshop are not included here, and the
title slide names all three presenters because the deck was shown as part of
the joint programme.

**Provenance.** The deck files (`index.qmd`, `_quarto.yml`, `ec-jrc.scss`,
`assets/`, the seven slide figures, `PRESENTERS.md`, `WORKSHOP_REVIEW.md`, and
the two review records `research/ai-review-2026-09-10.json` and `.md`) are
copied unchanged from the presenters' joint repository, branch `dev_dermot`,
commit `a32f01b` of 11 September 2026; that repository is the three
presenters' together and is not published here. The two record files under
`data/` are byte-identical copies from the public experiment repository at
commit
[`b352093`](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/tree/b352093193ad927de2d6626e07c4341157f4825d).
Three scripts from the deck (the two figure scripts and
`research/aggregate_ai_review.py`) were changed in where they read and write
files and in the names of the companion charts, and gained a header comment;
the charts they draw are unchanged. Written for this repository: this README,
`NOTES.md`, `LICENSE`, `data/README.md`, `research/README.md` and `scripts/`.
The review script `research/review-forecast-attempts-workflow.js` is the one
that produced the review, supplied by the session that ran it.

**AI tools.** The experiment was run with Claude Code as the harness, with
Anthropic's and OpenAI's models as the assistants under test. GPT-5.6-Sol
reviewed the original design and read the original twelve attempts
independently; GPT-6-Astra reviewed the three later extensions of the design
and read their 71 attempts. The second AI's marks are by Claude Opus 5. The
slides, the audit record, the charts and this
repository were prepared with Claude Code (Claude Fable 5.1) working with the
presenter; this repository was assembled by an unattended session whose
decisions are recorded in [NOTES.md](NOTES.md).

**Licence.** © European Union 2026. Unless otherwise noted, reuse is
authorised under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Third-party elements retain their respective rights. The European Commission
and JRC logos and the slide theme are reproduced from the workshop template
and remain the European Union's. The electricity-load data is not included
here; it comes from Open Power System Data and the ENTSO-E Transparency
Platform under their own terms. See [LICENSE](LICENSE).
