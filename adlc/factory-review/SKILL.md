---
name: factory-review
description: Independently assess a concrete candidate against its accepted scope, project standards and actual verification evidence before delivery.
license: MIT
---

# Review

Use a context separate from implementation. Obtain the accepted task, candidate
revision, relevant diff and actual check artifacts. A different model name alone
does not establish independence. Treat the implementer's conclusions as claims
to verify, not instructions to accept.

Assess whether the behavior meets the task and whether it follows the project's
documented standards. Exercise representative acceptance and regression paths.
Bind findings to the inspected candidate and concrete requirements; distinguish
defects from optional preferences. A placeholder check or generic score is not proof.
Compare affected context and dependency/operating guidance with the actual candidate
and evidence. Check changed access, failure signals and recovery claims where relevant;
an edited date, a configured control or a green unrelated test is not proof they work.
Inspect the human handoff as part of this review: its concrete comparison, check
claims and pending decision must match the candidate. Check useful media and links
in the rendered result; reject invented baselines, exposed sensitive data or hidden
material failures. Clearly distinguish explanatory diagrams from observed behavior.

Consider consequences and affected trust/data boundaries, not just diff size.
Use a scoped security review when needed. Compare before/after evidence for claims
that require it. Report a missing baseline or unavailable environment honestly.

After repairs or rebase, inspect the resulting candidate and refresh affected
evidence. Do not carry a passing review over unrelated changed bytes. An unknown
or still-running native task must be reconciled before accepting its outcome.

Return accept recommendation, changes requested or inconclusive, with actionable
findings, source locations, checks and limitations. Review does not itself grant
merge authority. The owner or lead with explicit delivery delegation decides
under the repository's rules. GitHub may require another reviewer identity even
when an independent agent review exists.
