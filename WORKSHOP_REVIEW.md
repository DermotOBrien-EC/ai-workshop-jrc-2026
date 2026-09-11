# Workshop review and revision, 6 September 2026

The May talk needs revision. The evidence supports retesting a workflow when
its model or harness changes. It does **not** support a mandatory complete
rewrite of skills after every release, a universal benefit from longer
prompts, or a vendor ranking for understanding conversational intent.

The revised talk uses the discovery of the May information leak as its central
example. It distinguishes measured observations, limitations, personal
experience and proposed future practice. There are 38 main slides and 13
backup slides, retaining the existing EC/JRC theme and assets.

## Evidence and scope

- Reviewed all 88 original rendered slides, the complete source, theme,
  presentation configuration, asset/footer scripts, README and presenter map.
- Read the experiment design and results, all 83 rows of the per-run table and
  machine-readable scoring records, scoring/figure-generation logic and prior
  review qualifications. Inspected the May forecasting implementation and the
  September same-fit diagnostic directly.
- Independently recalculated all **43** headline forecasts labelled
  `recomputed`, matching timestamps against the original load series and
  checking 168 unique, consecutive hourly predictions. Every MAPE agrees
  within the source CSV's rounding (0.000501 percentage points).
- The other **17** scores are agent-reported and **23** sessions have no score.
  Eight recomputed forecasts use a week shifted one hour from UTC. The slides
  now disclose these distinctions.
- Verified all seven entries of the experiment's `runs_2026_09/pins.sha256`:
  prompts, data, workspace instructions and unattended-session suffix.
- No new experimental model runs or model fitting. The per-run leakage and
  process classifications come from the archived audit; this review does not
  claim to independently repeat the full forensic reading of all 83 session
  transcripts. It verifies the principal code examples and numerical claims.

Experiment repository at the time of review:
`/Users/doob/dev/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26`,
clean HEAD `b352093193ad927de2d6626e07c4341157f4825d`.
The slide baseline was `6840124`.

Primary numerical records:

- [results.csv](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/runs_2026_09/results.csv)
- [scoring.json](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/runs_2026_09/scoring.json)
- [DESIGN.md](https://github.com/DermotOBrien-EC/LLM_coding_practical_example_JRC_LEGENT_presentation_15_05_26/blob/b352093193ad927de2d6626e07c4341157f4825d/runs_2026_09/DESIGN.md)

These links identify the local commit reviewed; remote availability of that
commit was not separately checked. The experiment checkout was not modified.

## Findings addressed in the slides

1. **Critical, data validity:** the May L3 score was still praised as evidence
   of research quality despite a footnote admitting test inputs. In the
   experiment's `runs/L3/code/lightgbm_features.py:43`, lags come from the
   combined observed series; line 46 builds rolling features from that series,
   line 111 concatenates test observations and line 143 selects test features.
   The revised slides label 3.43% as invalid for a single-origin week-ahead
   forecast, including the backup chart. The same fitted September model's
   3.71% observed-input diagnostic versus 5.53% recursive score illustrates
   the information boundary directly.

2. **Important, unsupported inference:** slides attributed most of the
   improvement to factors other than the model and suggested specificity
   bought honesty. Several factors changed together. The revised deck states
   the association and does not estimate a causal model, harness or length
   effect. It also exposes L3's conflicting class-selection instructions.

3. **Important, evidence provenance:** the original cross-generation table
   omitted agent-reported markers and implied all scores were comparable.
   The new deck distinguishes recomputed, reported and missing scores,
   discloses shifted windows, and qualifies incomplete runs and leakage.
   The Claude review caught double rounding in this revision: direct rounding
   of full-precision values gives **5.11** for Astra L3 r2 and **3.20** for
   Fable L2 r3. The new wider-results appendix also uses **4.14** for GPT-5.5
   with-note L2 r3. Astra L1 intervals are correctly **2 of 3**.

4. **Important, intervention scope:** the 20-session suffix arm reran only
   stopped cells, without an unchanged-prompt retry control. Nineteen scores
   are not nineteen independently recomputed forecasts or nineteen clean,
   completed studies. The new slide reports **16 recomputed, 3 reported,
   1 no score**, and the notes explain the comparison's limits.

5. **Important, calibration:** having intervals and measuring their coverage
   was described as calibration. Fable L3's nominal 80% bands cover only
   **48.8–57.1%** of this week's hours. A dedicated slide now shows both
   nominal levels and observed coverage, without a general guarantee.

6. **Important, outdated framing:** the cover still said May, current-state
   slides used archived charts, technical definitions were misleading, and
   the internal model catalogue was asserted without current verification.
   The date is 11 September, definitions are corrected, selected historical
   charts are visibly labelled in backup, and internal service details defer
   to authenticated current guidance.

7. **Important, presentation usability:** the previous process slide extended
   below the canvas, other result slides intruded into the footer, and the
   presenter map described 84 slides while the rendered deck had 88. The
   main argument is now shorter, tables are editable text, slide references
   match the rendered deck, and presenter reassignment is marked as proposed.

## Upstream inconsistencies recorded, not edited

The experiment's `RESULTS.md` is useful context but not uniformly in sync with
its structured records. Section 10.1 misidentifies May's winning L1 baseline
as climatology; code and metrics identify `naive_y`. Sections 9.4 and 10.4
disagree about adopting some probe-only leakage classifications. The closing
paragraph of 10.4 denies Claude L1 validation/intervals that its own tables
record. Its 'lowest number anywhere' claim for 2.68 conflicts with the saved
Fable L2 2.30. The old slides also said 90 sessions where the counted table has
83. The revision uses structured records and inspected code rather than
repeating those claims. No upstream analysis or prose was changed.

## Public sources checked

- [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model):
  Astra sensitivity to unclear or conflicting skill instructions and autonomy.
- [Fable 5.1 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1):
  existing Fable 5 prompts should generally work, with specific behavioural
  differences and effort settings to evaluate.
- [Anthropic harness study](https://www.anthropic.com/engineering/harness-design-long-running-apps):
  removal of a context-reset workaround on a newer model.
- [Managed Agents architecture](https://www.anthropic.com/engineering/managed-agents):
  separation of model orchestration, session and execution environment.
- [Stanford HAI definition](https://hai.stanford.edu/ai-definitions/what-is-artificial-intelligence-ai)
  and [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).

Public sources motivate the practice recommendations. They do not validate
the case study's vendor comparisons. Speaker observations about Fable, Sol
and Astra are explicitly personal. The revised forecasting brief is untested.

## Verification and remaining work

Quarto rendering and browser inspection cover the source-to-slide path.
Independent numerical checks cover saved predictions, not model fitting or
every transcript audit. Authenticated Commission guidance and GPT@JRC's
current availability/model catalogue remain unverified. Confirm those links,
speaker assignments and timing before the event.

Final local checks:

- `quarto render index.qmd`, Quarto 1.10.18: passed.
- Browser inspection of all 53 slides at 1280 × 720: no JavaScript errors,
  broken images or content outside the checked bounds.
- PDF: 53 pages at 960 × 540 points, correct event date, evidence text and
  provenance labels present, speaker notes excluded. Rendered every page and
  visually inspected the deck and the affected figures after export fixes.
- A print-only rule in `ec-jrc.scss` prevents Reveal's inline dimensions from
  clipping or stretching figures. Checked all nine figures against the PDF
  content margins. The screen appearance is unchanged by that rule.
- `figures/may-l3-winner.png` is a byte-for-byte copy of the original May
  experiment plot, replacing a partially clipped screenshot in the old deck.
- `git diff --check`: passed. Experiment checkout still clean at the cited HEAD.

Changed source files: `index.qmd`, `ec-jrc.scss`, `PRESENTERS.md`, `README.md`,
this review record and `figures/may-l3-winner.png`. Generated local outputs are
`index.html`, `index_files/` and `output/pdf/workshop-2026-09-11.pdf`; the
repository ignores rendered outputs. No commit, push or publication.

## Independent Claude review

Fable 5.1 reviewed the source diff, archived per-run table and full-precision
independent re-score through the model-neutral dispatcher. It confirmed the
counts and principal numerical evidence, and returned needs-attention.

The revision addresses the substantive findings:

- Corrected double rounding from three-decimal CSV values. Direct rounding
  uses the independently recomputed values, not a second rounding of the CSV.
- Attributed Astra L1's absence of test-week scoring to the explicit per-run
  `audit_note` statements and RESULTS.md section 9.3. The `final_scoring_only`
  label alone would not establish it. Checked all three audit notes directly.
- Made the Fable title descriptive, put its CET/UTC caveat on the slide and
  added complete L1/L2 backup tables including outliers and audit qualifiers.
- Stated that two suffix-arm sessions ended early, one leaving a score.
  Sol L3 r3's summary records timeout after 10,804 seconds; its scoring note
  says the reported study existed but regeneration was running, with a
  code/transcript disagreement. The zero-turn summary is not a claim of zero
  executed work. No upstream correction is made here.
- Clarified that the proposed brief asks the agent to measure validation
  coverage and leaves target-week evaluation until after delivery.
- Added the gateway/effort caveat on the main slide, corrected the historical
  chart wording and softened the note on the conventional AI definitions.

Personal experience remains on a clearly labelled slide because the user
explicitly requested that comparison. Presenter assignments remain proposals.
Local rendering checks completed while the reviewer was running and replace
the placeholder it flagged. The later print fix and original-plot replacement
are local rendering changes, not new empirical claims.

The reviewer had no live browser or filesystem tools. This is an independent
content challenge, not a second execution of the runtime checks. The focused
recheck of the corrections timed out after 240 seconds with no verdict. Final
Claude sign-off therefore remains open; the first review's findings were
applied and checked locally, not silently treated as a peer approval.

Final local verification also checked all 41 numerical entries in the added
L1/L2 tables against full-precision recalculations or labelled agent reports.
After correcting a misplaced notes delimiter during the build, both new tables
appear as visible backup slides. HTML and PDF each contain 53 slides. The PDF
legend preserves the literal asterisk for agent-reported values.

## Verdict

Status: needs-attention

- File: WORKSHOP_REVIEW.md:192
- Category: test-gap
- Severity: important
- Description: The initial independent Claude review completed and its substantive findings were addressed, but the focused recheck timed out without a final verdict.
- Recommendation: Obtain the remaining Claude content sign-off before treating this revision as independently accepted. The checked local slides and PDF are ready for that review.

## Addendum, 10 September 2026: rewrite of the main route for a 30-minute talk

Written 2026-09-10 21:09 WEST. The main route was rewritten for the actual slot (30 minutes, a
mixed audience of scientists and civil servants, no exercise): 24 slides in plain
language telling the May-to-September story, then the practical conclusion on how
to work with an AI assistant. No number, qualifier or claim was changed; the
main-slide caveats moved into speaker notes, and every previous main slide that
carried evidence (the rerun design, evidence limits, Fable run tables, the
same-model comparison, process counts, interval coverage, stopping counts, the
Astra-with-note table, the findings, the durable-instructions and migration
material, the revised brief and the exercise) now sits verbatim in the backup
section behind the existing backup slides. Superseded main slides (agenda, the
May-lesson opener, the definitions of the task and the May results, the boundary
and same-fit slides, the L1 example, the clarification and unattended slides, the
Commission slide and the discussion outro) are replaced by plain-language
versions that carry the same figures and sources in their notes. The verdict
above (Claude content sign-off open) is unchanged by this addendum.

Later the same day the backup section was rewritten in plain language and cut
from 37 slides to 18. Removed as repeats of the other presenters' sections: the
AI/ML definitions slide, the benchmarks slide and the four historical chart
slides; promoted into the main route: the harness slide and the same-model
comparison; removed as summaries or filler: the findings, personal-experience,
correction, migration, verification, closing and exercise slides and the May L1,
L2 and documentation-composite figures. A mechanical check confirmed that every
number, symbol and qualifier in the 18 kept slides survives on the slide or in
its notes; the only digits that disappeared are the 1, 2 and 3 of the labels L1,
L2 and L3, replaced by the word counts.

Charts, 10 September: nine figures were drawn from results.csv and scoring.json
at the audited commit b352093 by figures/make_experiment_figures.py (kept in the
repository): one dot per attempt for each request length and combined, a report
card of eight audit checks per model and request length, the stop counts, and
the interval coverage. The three result tables moved into the notes of the
slides that now show the charts; no number changed. Four chart slides were
added (backup section: 22 slides).

AI-assisted review, 10 September: one Claude Opus 5 reviewer per attempt (62
attempts with a forecast) read the saved code, forecast, final message and
summary and scored code quality, method, honesty of reporting, decisions and
deliverables 1 to 3 with evidence per score, plus its own read of the peek.
Records: research/ai-review-2026-09-10.json and .md; aggregation script
research/aggregate_ai_review.py; three backup slides. Not part of this audit and
not independently verified. The reviewers found the same three headline peeks as
the audit and one more (opus5_L1_r3, observed target-week temperature as an
input, which the audit records under selection scope); on the looser
test-selection class they were more lenient (26 attempts labelled test_selected
read as clean), so the audit remains authoritative on the peek.

Backup pass, 10 September, late: a cold read of the backup section returned 43
findings; the contradictions were fixed (a caption that called every score
below 4 % a peek when two fair Astra scores are 3.9 %; "clean on every check"
for a row with 2 of 3 ranges; "3/3 down those columns" where two rows had a
no-score attempt; the review's 62 attempts against the audit's 60 with a score,
now footnoted as 60 plus two with forecast work but no final score; a Fable
attempt described as delivering only a status line although its saved forecast
scored 5.35), the three-panel overview chart and the benchmark source row were
cut as duplicates, titles now state each slide's point, the notes lead with the
sentence to say and hold the number tables as lists, and the section is in the
main route's order. Charts use the figtop class so the print export does not
crop them. Backup section: 24 slides.

V2, 11 September: five chart slides moved from the backup into the experiment
part of the main route (one scale for all three request lengths; how often the
OpenAI models stopped; what each request length bought in good practice; a
range is not evidence; a second AI's marks), each with a one-line takeaway. The
main route is 29 slides for a 30-to-40-minute slot; the earlier 24 slides are
unchanged. Backup: 14 slides. No number changed.
