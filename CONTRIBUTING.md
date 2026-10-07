# Contributing

Start with a concrete problem, the applicable project goal and observable proof.
Use an issue or accepted brief; research may end with a decision rather than code.
Preserve the small method-only scope in [VISION.md](VISION.md).

Edit a skill in its canonical bundle: `foundation/`, `agent-ops/` or `adlc/`.
Supporting references belong inside the skill directory so staging keeps them
usable. The root documentation is for maintainers/operators and is not a hidden
runtime dependency. Preserve the existing MIT attribution.

Before a PR:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
```

Exercise changed staging behavior on disposable destinations. For substantive
instruction changes, rehearse a realistic task in a separate context and retain
sanitized inputs, outcome and limitations. Include failures and fixes. Checks
must demonstrate decisions or artifact behavior rather than count wording.

Separate review assesses the accepted scope and actual candidate. A human may
delegate delivery under project rules; neither a skill nor a green workflow grants
it. New commits require refreshed affected evidence. GitHub protection may require
a separate GitHub reviewer identity; a second model on the author's account does
not satisfy that rule.

Release reviewed commits with a Git tag matching `VERSION` and a GitHub release.
Consumers can clone that tag or download the source archive. There is no npm
package or daemon to publish. Verify the tag, checks and release contents after
publication. Describe native setup and qualification limits in release notes.
For recovery, select the previous reviewed release and diff staged skills against
the installed copy; preserve local adaptations and private native state.
