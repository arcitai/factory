# Contributor instructions

Revision: 0.1.4 · Updated: 2026-10-09

Read [VISION.md](VISION.md), [README.md](README.md) and the affected skill.
This repository owns Factory's method, not an adopting application's product rules.

Keep one canonical source for each skill and its references. A staged bundle
must remain useful outside this checkout. Put required resources inside its
skill folder; do not link to a personal plugin or another checkout.

Prefer native T3, harness and GitHub facilities. A new helper must have a concrete
setup or validation responsibility and bounded effects. Do not add runtime
orchestration, a provider registry, a dashboard or an execution store.

Preserve the two decision points and explicit scoped delegation. An external
issue, model response or skill never grants authority by itself. Keep secrets,
native history, machine identities and raw security findings out of this repo.

Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests`.
Material skill changes need representative behavioral evidence; metadata checks
alone cannot prove decisions. Review the final candidate independently before
authorized delivery. Record live proof separately from fixtures and source review.

Keep changes, proof and roadmap in GitHub. Update affected guides and the
qualification record. Readback published artifacts and preserve a recovery path;
do not turn a passing package check into an installation claim.

Follow the revision convention in CONTRIBUTING when editing skills or Markdown.
Keep edit dates separate from dates of observed behavior. Preserve the human Git
author and actual contributors' native Co-authored-by trailers through delivery;
do not credit a model for work it did not perform.
