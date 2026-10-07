# Qualification

The initial release packages a method. It does not claim that a T3 installation,
autonomous backlog, mobile decision route or defensive environment has already
been qualified by publishing these files.

| Boundary | Evidence / status |
| --- | --- |
| Package structure | Eight skills across Foundation, Agent Ops and ADLC; local metadata and self-contained link validation |
| Staging helper | Disposable tests cover each bundle, manifest hashes/licenses, refusal to overwrite, symlink resources/destinations, ignored files in Git checkout mode and unrelated Git provenance; archives stage their reviewed contents without Git provenance |
| Package validator | Fixture checks exercise a mismatched skill name, missing references and links escaping the skill folder |
| Method decisions | Nine text-only Claude Opus 5.5 scenarios on the final method inputs matched their decision boundaries; see the [rehearsal record](rehearsals.md). Codex behavior remains unqualified. The final review verdict and revision are recorded with the release |
| Upstream capabilities | Documentation/code baseline: T3 0.0.45 and separately identified 0.0.46 nightly, checked 2026-10-07 |
| Operator workspace guidance | Fresh-context Opus setup and harness-role scenarios distinguish remote execution, source loading, role scope and pending actions; see [workspace rehearsals](rehearsals.md#operator-workspace-update-v011). This is text-only evidence, with a reporting failure and intervention limits retained |
| T3 on an execution host | Not established by this package release; verify the selected host/account/service |
| Native skill discovery | Must be observed in each installed provider/profile; a staged directory is insufficient |
| Client disconnect and recovery | Requires the actual selected service and connection route |
| Phone decisions | Requires a real T3 mobile notification/response observation |
| Application delivery | Requires a selected application and verified accepted task |
| Defence | Requires a bounded authorized target and isolated test |

Run package checks locally:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests -v
```

Package checks are not tests of provider behavior. Keep private installation
records and native evidence out of this repository. Record precise versions,
revision, actions, result and limits using the Foundation adoption outline.

For a material skill change, use a fresh context with the skill and a realistic
request. Inspect the resulting decision/artifact, not just whether keywords are
present. Include missing delegation, explicit delegation, new risk and untrusted
input where the change affects those boundaries. Do not spend a subscription down
to its limit just to demonstrate a quota condition.

The roadmap is maintained in GitHub issues, not a second local task list.
