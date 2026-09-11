# Workshop delivery, 11 September 2026 (V2)

The deck has **44 slides: 29 in the main route and 15 backup slides.** The main
route is written for a **30-to-40-minute talk** to a mixed audience of JRC
scientists and civil servants, many of whom have never used an AI assistant.
There is no exercise and no breakout; the practical steps are in a written
walkthrough that goes out after the talk. Every number on the main slides is
unchanged from the 6 September audit (WORKSHOP_REVIEW.md); the qualifications
live in the speaker notes and the backup slides. V2 (11 September) moved five
chart slides drawn from the run records into the experiment part: one scale
for all three request lengths, how often the OpenAI models stopped, what each
request length bought in good practice, a range is not evidence, and a second
AI's marks for the saved work.

## The route

| Minutes | Slides | Section | The one thing the room should take |
|---|---|---|---|
| 0–2 | 1–3 | Title, what I learned since May, three things you will leave with | "This is for me, even though I don't code." |
| 2–6 | 4–7 | 1. What these tools are, and the harness around them | A well-read new colleague, not a calculator; the software around it matters. |
| 6–25 | 8–21 | 2. One experiment, and what it taught me | The best score used the answers; the newest AI asked the question that would have caught it; the recipe made forecasts more alike, not better. |
| 25–33 | 22–27 | 3. How I work with AI now | Goal, ask, discuss, decide. Seven questions. You still check. |
| 33–40 | 28–29 | The public repository, close and questions | "Ask, then check." |

Plan for 33 minutes of speaking and 7 for questions. Rehearse once to 31 with a
timer; real delivery runs longer. If the slot is 30 minutes, drop slides 18
(how often they stopped) and 21 (a second AI's marks): the story survives
without them and the route returns to about 27 minutes.
Never cut slides 9 to 17.

Solo delivery by Dermot is assumed. If the slot is shared, slides 4–7 (what
the tools are) and 27 (checking) hand over cleanly.

## Speaker framing

Opening (slide 2): "In May the result looked fine and it taught me a lesson I no
longer believe. There had been a data leak: the model had found a way to cheat,
and I did not notice. That is what today is about: how to work with an AI
assistant, and how to check its work."

The hinge is slides 11 to 17. Say the "24 hours earlier" explanation slowly
(slide 10): on 1 January the value was known; from 2 January it had not happened
yet; the honest method plugs in its own prediction; the May code plugged in the
real number. Slide 12 says why: an analyst knows not to, an AI needs to know or be
told, and the newer models catch more of it themselves. Slide 13 shows the same
method scored both ways, so the gap is visibly the answer sheet. Slide 15 makes
the harness point: the May model in the September harness gave a different
answer, so compare models only inside one harness. Slide 16 puts every attempt
on one scale: say that the recipe made the forecasts more alike, not better, and
that the only low 1,673-word scores are the coral peeks. Slide 17 is
where the talk turns: the newest OpenAI
model asked exactly the question that would have caught the May mistake.

Slides 20 and 21 are the two chart slides after the note: what each request length bought in good practice (say: the note bought the most) and a second AI's marks (say: a fast first check, not the last word, and it found the same peeks the audit did). Slide 24 is personal experience and the notes say so. The experiment measured
forecasts, process and stopping behaviour; it did not measure conversational
tone or intent recognition, and it is not a vendor ranking.

Slide 28 is the public repository (github.com/DermotOBrien-EC/ai-workshop-jrc-2026)
with a QR code: the slides, the setup guide for Claude Code and Codex, the
experiment records and how to run it yourself. Say it in one breath and leave
it up while people scan it.

Closing (slide 29): "The skill is no longer writing perfect instructions. It is
asking good questions and judging the answers." Leave it on screen for questions.

## Questions to expect

- **Will it replace us?** It replaces tasks, not judgement.
- **Can I trust it?** As much as a clever new colleague's first draft. Read before you send.
- **Is it allowed here?** Within the staff guidance, yes: check which tool may handle which material, and you stay accountable. Andrés's section covers the four staff rules; point to it.
- **What about the AI Act?** Not covered by the deck's evidence audit. Check the current staff guidance before the event and answer from it; the safe line is that the internal rules apply regardless.
- **Was the May result cheating?** Not deliberate. The long instructions asked for the 24-hour clue; the same feature code ran over the test week, so the real values flowed in. A data leak, not intent. For the task as set, the result is invalid.
- **If it used the real numbers, why was the error 3.4% and not 0%?** It never saw the real number for the hour it was predicting, only the real number from 24 hours earlier, used as a clue. Tuesday 3pm is close to Monday 3pm but not identical, so the prediction is still off by 3 to 4%. Done fairly, the method has to use its own prediction for the day before, errors pile up over the week, and the same method scores about 5.5%.
- **Did the old model really beat the new one?** No. The old model's low score used the answers; the honest score for this task is about 5%, and the newest model produced a real 3.3% from ten words.

## Before the event

- Rehearse the rendered `index.html`. Press **S** for notes, **O** for the
  overview, and **F** for fullscreen.
- Keep `index_files/`, `assets/` and `figures/` beside `index.html` when copying
  it, or use the PDF export (README, "PDF export").
- Treat 6 September as the evidence cutoff. If new runs arrive, check their
  source and audit labels before changing any number.

Stable slide IDs in `index.qmd`: `#hook`, `#harness-main`, `#task`, `#may`, `#answers`, `#not-to-do`, `#same-model-main`, `#all-levels`, `#stopped`, `#checks-stacked`, `#review-stacked`,
`#two-scores`, `#ten-words`, `#asked`, `#paragraph`, `#now`, `#questions`,
`#check`, `#try`, `#close`, and `#backup` for the start of the backup
section. Use them if later edits change the slide numbers.
