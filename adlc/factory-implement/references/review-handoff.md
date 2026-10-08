# Make the change easy to review

Use when preparing or revising a PR or substantive handoff for a person. The
implementer owns this presentation; independent review checks its claims, and
AgentOps brings forward any remaining owner decision. Use the existing PR and
evidence locations. A small change needs a small explanation, not every section
below or a second report.

Lead with the concrete problem and resulting behavior in plain language. Show
one useful before/after example from the actual change. Point to the few files
or views that deserve attention and explain any material tradeoff or decision.
State observed checks and remaining limitations briefly, linking the full proof.
Keep raw transcripts, command logs and detailed review reports behind a link or
collapsed section. Keep a failure or missing check visible when it affects the
decision; do not bury it to make the headline look green.
Return the handoff itself, without narrating compliance with this method. Combine
problem, example and checks in a short paragraph when sufficient; do not add a
separate heading for every fact or repeat the same limitation in several places.

## Choose evidence that explains this change

Start with what the reviewer needs to understand about this specific change.
Choose the format for that question, not to fill a visual slot. The options below
are examples, not requirements for every PR. Plain text can be the best answer.

| Change | Useful comparison |
| --- | --- |
| Visible UI | Real captures of the affected view before and after; a short action/result sequence when interaction matters |
| CLI, API or data behavior | A small real input/output pair, response, failure/recovery example or measured result |
| Method, documentation or architecture | Exact changed excerpts or a clearly labelled explanatory table/diagram; a recorded behavior trial when making a behavior claim |

Use a diagram when its relationships explain an important mechanism, boundary,
decision or tradeoff. Show the concrete inputs, changed path or consequence that
answers the reader's question. A flowchart of phase names adds little unless
those phases or their relationships are the actual change. Review the meaning as
well as rendering: if removing the visual loses no useful understanding, omit it.
Do not replace a redundant chart with a redundant table or mandatory screenshot.

Capture a relevant baseline during investigation when practical. Reuse an
identified prior artifact or safe isolated preview; preserve other work. Bind
evidence to its source revision/environment and compare relevant state, inputs
and viewport fairly. If a baseline or check is unavailable, say so and show the
verified candidate. Do not fabricate a before-state, a passing result or a
measured improvement. Label illustrative examples and diagrams as explanation,
not observations. A screenshot proves appearance, not accessibility, correctness
or a completed interaction.

Use existing tools and approved storage. Inspect media for credentials, personal
or customer data before sharing. Do not install a recorder or upload to a public
image host merely to satisfy the format. Evidence does not replace real tests or
independent review.

Before requesting human review, inspect the rendered PR: images/diagrams must be
readable, links accessible to the intended reviewer, and the opening understandable
without the implementation chat. An absent visual is fine when a short example
communicates the change better. Rewrite the title, comparison and checks when
the candidate or scope changes; date and identify historical evidence instead
of silently presenting it as current. Update the existing handoff rather than
adding repeated summary comments. State the actual pending decision; reuse any
existing delivery delegation instead of inventing another approval gate.
A positive review recommendation is not itself permission to merge.

Inspiration: the comparison and observed-proof principles in
[before-and-after](https://github.com/michaelshimeles/skills/blob/4b72f46b045e6fef52e6a98d4c162dd309826aed/before-and-after/SKILL.md)
and [evidence-driven-testing](https://github.com/michaelshimeles/skills/blob/4b72f46b045e6fef52e6a98d4c162dd309826aed/evidence-driven-testing/SKILL.md).
Factory uses its own instructions and existing tools; these packages are not
installed or redistributed with the method.
