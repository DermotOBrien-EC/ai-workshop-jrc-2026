# Notes from the session that assembled this repository

Written 2026-09-11, 01:27 WEST, by the Claude Code session (Claude Fable 5.1)
that carried out the brief `BRIEF.md` left at `~/dev/ai_seminar_jrc_public_brief`
on this machine. The owner was asleep; nothing was asked. Every decision below
was the session's, and each one names its reason so it can be reversed.

## Where things are

| | |
|---|---|
| Repository | https://github.com/DermotOBrien-EC/ai-workshop-jrc-2026 (public, default branch `main`) |
| Slides on GitHub Pages | https://dermotobrien-ec.github.io/ai-workshop-jrc-2026/ (source: branch `main`, folder `docs/`) |
| PDF on Pages | https://dermotobrien-ec.github.io/ai-workshop-jrc-2026/workshop-2026-09-11.pdf |
| PDF in the repository | `output/workshop-2026-09-11.pdf` (43 pages, 960 by 540 points, 2,165,727 bytes) |
| Local clone | `~/dev/ai-workshop-jrc-2026` on this machine, beside the deck checkout `~/dev/ai_seminar_jrc` |
| Commits | `48e7385` deck, records, scripts, licence; `6301ab4` README, review note, build scripts; `e4444e8` rendered site and PDF; all at 01:26 WEST, authored and committed as Dermot O'Brien with the session's Claude trailers |

Pages build: enabled through the API at 01:26 WEST (`POST /repos/.../pages`,
source `main`, path `/docs`); the API reported the first build `built` at
00:26:51 UTC with no error. Checked at 01:27 to 01:29 WEST: the slides
(HTTP 200, 111,370 bytes, 43 slide sections, title "AI in the Research
Workflow"), the PDF (HTTP 200, 2,165,727 bytes), a figure, a logo and the
reveal.js script all served from the Pages address.

## What was done

1. Read the brief, the deck's README, PRESENTERS.md and WORKSHOP_REVIEW.md,
   the full slide source and speaker notes, and the experiment repository's
   design, results, requests and README at commit `b352093`.
2. Copied Dermot's deck files unchanged from the checkout at `a32f01b`; copied
   the two record files from beside the brief and confirmed them byte-identical
   (SHA-256) to the experiment repository at `b352093`.
3. Repointed the two figure scripts and `research/aggregate_ai_review.py` at
   `data/`, `figures/` and `research/`; regenerated every chart and compared
   each pixel for pixel and byte for byte with the deck's: all identical.
   Confirmed the two hand-copied figures (`exp-rerun-l1-fable.png`,
   `may-l3-winner.png`) byte-identical to their sources in the experiment
   repository.
4. Rendered the deck with Quarto 1.10.18 (43 slide sections), exported the PDF
   with headless Chrome (43 pages), and assembled `docs/` for Pages.
5. Wrote README.md, research/README.md, data/README.md, LICENSE, the two build
   scripts and this file.
6. Ran three in-session verification lenses over the tree before publishing
   (see below), fixed what they found, then committed, created the
   repository, pushed, and enabled Pages through the API.

## Decisions, with reasons

1. **Repository name `ai-workshop-jrc-2026`**, the brief's suggestion. It was
   free on the account.
2. **Pages from `docs/` on `main`, not a `gh-pages` branch.** One branch is
   easier to understand and to update: `bash scripts/build.sh` regenerates
   `docs/` from the source, and a push publishes it. `docs/` carries only what
   the rendered page needs (index.html, index_files/, assets/, the seven
   slide figures, `.nojekyll`) plus a copy of the PDF so that Pages serves
   it. The PDF therefore exists twice in the tree (2.1 MB each); judged
   acceptable.
3. **Committer identity set to the owner in this repository's local git
   config** (`user.name`, `user.email`), in addition to the `--author` the
   brief asked for. Otherwise every public commit would show this machine
   account's personal name and email as the committer. The Claude trailers in
   each commit message record that the session did the work. The change is
   local to this clone and touches no global configuration.
4. **The deck is byte-identical to the checkout**, including the title slide
   naming all three presenters. The brief said to publish only Dermot's part
   and not to change the deck; the title slide is part of the deck as
   presented, and the README explains why the three names are there.
5. **Left out of the copy:** `_extras/pattern-gallery.qmd` and the 68 `sNN-*`
   images (the joint template's demo material, not used by these slides),
   seven `exp-*` figures the slides no longer reference, the deck's own
   README (replaced; its Quarto and PDF-export instructions are carried into
   the new README in substance), `talk_plan.md`, `.claude/`, and rendered
   outputs at the root (`.gitignore` excludes them; `docs/` is the one
   committed rendering). The brief listed exactly what to include.
6. **Companion charts are committed** (`exp-every-attempt.png`,
   `exp-attempts-*.png`, `exp-report-card*.png`, and two `.notes.txt` files
   with the counts behind the stacked charts), although the slides do not show
   them: the scripts produce them, so committing them keeps `git status` clean
   after a regeneration. The README's chart table says which files are on
   slides. The two notes files gained a first line stating their provenance,
   and the review one says the marks were not checked by a person.
7. **Script changes kept to paths, output names and a header comment.** The
   companion charts are named `exp-report-card-10-words.png` and so on
   instead of the scripts' former `fig-report-card-l1.png`, matching the deck's
   own naming for the files it had kept. `aggregate_ai_review.py` also accepts
   the wrapped record file as input, so it can be re-run from what is
   committed; re-running it reproduced the JSON record byte for byte and the
   Markdown record except for one trailing blank line.
8. **No GitHub release.** The brief offered "under output/ or attached as a
   release asset"; the PDF is under `output/` and on Pages, and a release is a
   further public surface the owner may prefer to make himself.
9. **LICENSE** carries the brief's notice, the copyright line and the
   logos-and-theme line. A first draft added "not covered by the CC BY 4.0
   grant and may not be used to suggest endorsement" for the logos; removed
   before publishing because the brief did not ask for it and the EU's own
   rules on the emblem are for the owner to state, not the session.
10. **The joint repository is described as "the three presenters' together and
    not published here"**, without a link: the GitHub API reported it private
    at 01:05 WEST, so a link would resolve for nobody but the presenters.
11. **The AI-review marks** are described as a second AI's reading, not checked
    by a person, in README.md, research/README.md, the notes file and the
    stacked script's docstring. research/README.md also states that for the
    nine Opus 5 attempts the reviewer was the same model as the author.
12. **Repository description, homepage and topics** were set through the
    GitHub CLI (homepage: the Pages URL; topics: jrc, european-commission,
    ai-assistants, forecasting, quarto, reveal-js, workshop, reproducibility).
    Cosmetic; change freely.

## Verification performed

- Deck files: `cmp` against the checkout for index.qmd, _quarto.yml,
  ec-jrc.scss, PRESENTERS.md, WORKSHOP_REVIEW.md, the five assets and the
  seven slide figures: identical.
- Records: SHA-256 of `data/results.csv` and `data/scoring.json` equal to the
  files served by GitHub at `b352093` (hashes in `data/README.md`).
- Charts: all 13 regenerated PNGs byte-identical to the deck's copies (the
  four report cards to the deck session's own outputs, which the deck had not
  kept). After the notes-header change, the two stacked charts were
  regenerated again and are still identical.
- Render: 43 `<section id=` in docs/index.html; every local `src`/`href` in it
  resolves inside `docs/`. PDF: 43 pages, first page the title slide, last
  page the sources slide; same size as the deck session's PDF.
- README scorer snippet: run against the real OPSD file and two saved
  forecasts from the experiment repository, it reproduced `results.csv`
  exactly (3.284% for `fable51_L1_r2` on its hour-shifted week; 2.298% for
  `fable51_L2_r1`), with and without time-zone offsets in the timestamps.
- Links: every external link in README.md, research/README.md and LICENSE
  returned HTTP 200 before publishing, except the repository's own URL and
  the Pages URL, which did not exist yet.
- Aggregation script: re-run from the committed review record; JSON
  byte-identical, Markdown identical but for a trailing blank line.
- Three in-session Claude lenses (Fable 5.1) read the tree before publishing:
  a cold read as a non-technical visitor, a mechanical audit tracing every
  number and path to its source (about 140 numbers and 85 paths, no wrong
  figure found), and a check against the brief. The Codex/GPT-6-Astra lane
  was out of quota ("try again at Sep 15th, 2026 2:25 AM"), so no
  cross-vendor review was possible; the owner's rules would normally require
  one for a deliverable like this.

## What the lenses found, and what changed

- The audit's independent reader was mis-attributed to GPT-5.6-Sol for all
  attempts; the audit notes and the design show Sol read the original twelve
  and GPT-6-Astra the 71 extension attempts (and reviewed the extension
  designs). Corrected in the README's audit and credits sections.
- "0 of 12" Claude attempts was stated without naming the group; now "the
  original September group of 12 Claude attempts (Fable 5.1 and Opus 5)",
  with the different-route caveat beside it so the sentence does not read as
  a vendor ranking.
- "Every number on the slides was checked on 6 September" overclaimed: the
  second AI's marks and the charts were added on 10 September. Corrected.
- "The audit found no use of the answers" for the 3.3% attempt now says "in
  the forecast itself" and notes the `test_selected` label (two reference
  methods scored on the same week; the method fixed beforehand), matching
  RESULTS.md section 4.
- "All three done the fair way" for Fable's 1,673-word attempts now also says
  all three named the winner by test-week error, as the recipe ordered.
- The 26 attempts the reviewers read as clean against the audit are 24
  `test_selected` plus 2 `leaked` outside the delivered forecast;
  WORKSHOP_REVIEW.md says "26 labelled test_selected". research/README.md
  keeps the 26 and states the recomputed split; the audit record was not
  edited.
- The scorer snippet gained the `utc=True` parse and an assertion that 168
  hours matched; the "0.05 points" flag threshold is now attributed to the
  design (DESIGN.md section 5.1) and worded as the rule, since no recomputed
  value actually crossed it.
- Glosses added for harness, UTC, lag, held-back data, checksums, sandbox,
  gateway, headless Chrome, reveal.js, Quarto and the `os` tag; the chart
  descriptions now say that unscored attempts appear as a count and that a
  stopped attempt counts as 0 on every practice; five rarely present fields
  of scoring.json were added to the audit table; "one slide per `##`
  heading" became "one slide per `#` or `##` heading plus the title slide".
- `data/README.md` was added because the brief asked for a note naming the
  commit under `data/`.

## For the owner to look at

1. **Two inherited sentences in the deck files** (copied unchanged, not
   corrected here): WORKSHOP_REVIEW.md's V2 paragraph says "29 main slides,
   14 backup" while PRESENTERS.md, the deck README and the brief say 28 and
   15 (both sum to 43; the difference is whether the backup divider counts as
   main). WORKSHOP_REVIEW.md's 10 September addendum says "26 attempts
   labelled test_selected read as clean" where the records give 24 plus 2
   `leaked`. The README follows PRESENTERS; research/README.md states the
   split.
2. **The deck's sources slide notes** (index.qmd, `#sources`) still say the
   second-AI marks are on "three backup slides"; in V2 they are one
   main-route slide. A deck-side fix, not made here.
3. **Local paths in the copied files.** WORKSHOP_REVIEW.md names a local
   checkout path `/Users/doob/dev/...` (a machine user name); the review
   record's `files_read` fields and the workflow script's `BASE` hold
   `/tmp/claude-501/...` paths. Harmless, but now public.
4. **The title slide names all three presenters** and the theme is the joint
   template, republished under one presenter's account with the EU notice.
   Confirm the co-presenters are content; the README credits them.
5. **The emblem.** LICENSE says the logos and theme remain the European
   Union's and nothing more; if a use restriction on the EU emblem should be
   stated, that is yours to add.
6. **No cross-vendor review** was possible (Codex quota). If you want one,
   the Astra lane reopens on 15 September.
7. **Pages** was enabled through the API; the first build's status is recorded
   at the top of this file. If it ever needs re-enabling: Settings, Pages,
   source "Deploy from a branch", branch `main`, folder `/docs`.
8. **Cosmetic choices you may want to change:** the repository description,
   homepage and topics; whether to keep the companion charts; whether to add
   a GitHub release with the PDF.
9. The brief folder `~/dev/ai_seminar_jrc_public_brief` was left as found
   (BRIEF.md, the two record copies, the workflow script, the backup-rewrite
   rules); nothing there is needed by the repository.

## Updating the repository later

```bash
cd ~/dev/ai-workshop-jrc-2026
# edit index.qmd or the figures, then:
bash scripts/build.sh        # renders and refreshes docs/
bash scripts/export_pdf.sh   # rewrites output/workshop-2026-09-11.pdf (Chrome needed)
bash scripts/build.sh        # once more, so docs/ picks up the new PDF
git add -A && git commit && git push
```

Pages republishes from `docs/` a minute or two after each push to `main`.

## Addendum, 11 September, morning

A slide with this repository's address and a QR code was added to the deck
before the closing slide (slide 28 of the main route), so the audience can find
this page. The deck is now 44 slides (29 main route, 15 backup) and the PDF 44
pages; the figures above that say 43 describe the night build. The same slide
is in the joint workshop deck as slide 73.
