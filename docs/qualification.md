# Qualification

The initial release packages a method. It does not claim that a T3 installation,
autonomous backlog, mobile decision route or defensive environment has already
been qualified by publishing these files.

| Boundary | Evidence / status |
| --- | --- |
| Package structure | Eight skills across Foundation, Agent Ops and ADLC; local metadata and self-contained link validation |
| Staging helper | Disposable tests cover each bundle, manifest hashes/licenses, refusal to overwrite, symlink resources/destinations, ignored files in Git checkout mode and unrelated Git provenance; archives stage their reviewed contents without Git provenance |
| Package validator | Fixture checks exercise a mismatched skill name, missing references and links escaping the skill folder |
| Method decisions | Nine text-only Claude Opus 5.5 scenarios on the initial method inputs matched their decision boundaries; see the [rehearsal record](rehearsals.md). Codex was not part of that rehearsal; the narrower native Nightly sample is recorded below. Final review verdicts and revisions belong with the release |
| Upstream capabilities | Reference setup now targets T3 0.0.46-nightly.20261009.2861, checked 2026-10-09 against pinned upstream source and the bounded pilot below; other builds require their own checks |
| Operator workspace guidance | Fresh-context Opus setup and harness-role scenarios distinguish remote execution, source loading, role scope and pending actions; see [workspace rehearsals](rehearsals.md#operator-workspace-update-v011). This is text-only evidence, with a reporting failure and intervention limits retained |
| Project context guidance (#10 candidate) | Fresh Opus cases cover proportional context, connector access, migration/recovery and telemetry review. A success-shaped draft and unsupported dates were observed; instructions were clarified and affected cases repeated. See [scope and limits](rehearsals.md#project-context-and-operation-issue-10) before relying on this guidance |
| Human review handoff (#12 candidate) | Factory/AIOS text-only cases cover comparisons, media, delegation and choosing a useful format. Residual failures include invented provenance and a docs-only “no runtime risk” claim. See [observations and limits](rehearsals.md#human-review-handoff-12-candidate); rendering and installation require separate proof |
| T3 on an execution host | One Nightly pilot observed below; publishing the package does not qualify another host/account/service |
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

## Nightly pilot — 2026-10-09

T3 `0.0.46-nightly.20261009.2861` ran on an unprivileged Linux execution account,
with matching Linux and Mac desktop clients. Private backups preceded the native
update. All nine thread shells and all 98 user/assistant messages migrated;
message text, three operator pins and four archived trial threads were checked.
V1 and V2 databases passed integrity checks. V1 tool/reasoning history remains in
the retained V1 data, not the V2 timeline. The service retained its private
loopback binding and host restrictions.

The existing Opus 5.5/High operator reloaded its role, called native capability
discovery and delegated one read-only review to Codex GPT-6.1-Sol/High. The child
ran in `approval-required` mode and needed **six individual command approvals**.
Its terminal result returned to the parent with a durable task identity. It found
two real documentation defects: an obsolete full-access launch requirement and
the missing fresh-review-round rule. Its three textual cases correctly required
bound worktrees, rejected authority from external issue text and required a new
reviewer task. These cases were decisions about supplied evidence, not executions
of parallel writers, hostile input or failed writes.

A subsequent candidate review inherited the caller's existing `auto` mode and
needed no command approvals. It returned a missing per-round retry-key and
review-brief rule; the candidate was amended for a fresh review round.

This proves assisted native delegation and result retrieval on that installation.
It does not prove unattended operation, restart during delegated work, independent
review of arbitrary application code, physical reboot/network recovery or phone
delivery. Nightly V2 needs the beta phone app. Native transcripts, task identities,
host details and backup locations remain in the private installation record.

## Agent Ops native probes — 2026-10-09

**Source analysis only.** Idea research for #6 compared no change, native T3
schedule/webhook configuration and new Factory code, using pinned upstream
source (`3b6af0bd`) and live capability discovery (scheduled tasks available,
none configured). Decision: defer automated intake; reject a Factory queue or
scheduler. No schedule or webhook was enabled or tested live.

**Live: two writers.** The Opus 5.5/High operator launched two Opus 5.5/High
`auto` threads with T3's explicit new-worktree launch from the 0.1.2 release
commit. Each reported its launch-bound working directory, Git root, branch and
HEAD before writing and created only one untracked probe file. Native run
timestamps overlapped by about ten seconds; no human approvals were requested.
The operator verified each worktree contained only its own file, no tracked diff
and an unchanged main checkout, then removed the files and archived both
threads. Worktrees and history were retained.

**Live: deferred completion.** The Claude harness blocked a foreground sleep, so
each worker moved its pause to a background command; its first run completed
before its readback. The background completion notification started a second
run in each thread, and those runs also overlapped. The operator waited for them
before cleanup. This motivated the background-continuation note in the T3 guide.
See the [rehearsal](rehearsals.md#background-continuation-8-candidate).

**Partly live: Connect.** The service was restarted after all recorded runs were
terminal. Persisted server state read on the host shows Connect exposure enabled,
the environment link provisioned, agent-activity publishing enabled and the
managed relay client available; the service is active and still bound to
loopback. Persisted state is configuration, not reachability. *Owner-reported:*
the Mac client used the Connect route, with the saved SSH route second.

**Not proved.** OS/filesystem isolation between worktrees (they share the
account), recovery from an uncertain or lost launch, permission denial, failed
writes, phone notification/question/response and physical reboot, lid or
network recovery. These probes do not qualify the installation.
