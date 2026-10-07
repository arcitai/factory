# Why a method around T3 and GitHub

Decision accepted 2026-10-07 after source research and an owner interview.
The intended outcome remains useful application development, research and scoped
Defence work. The implementation changes: Factory owns preparation and method;
maintained native tools own execution and the work surfaces.

The research compared Factory 0.18.11 with T3 stable 0.0.45 and a separately
identified 0.0.46 nightly. It inspected documentation and code, not a live T3
installation. The [earlier lifecycle audit](https://github.com/arcitai/factory-software-defence/issues/144)
retains the prior findings and their chronology.

| Evidence | Decision for Factory |
| --- | --- |
| T3 stable documents multiple native providers, remote environments, a background service and usage | Use these facilities; stop maintaining overlapping adapters, login flows and dashboard code |
| GitHub Projects supplies board/table views, fields and filters alongside issues, PRs and CI | Keep work status there; use live fields and labels rather than a Factory copy |
| Newer T3 V2 supplies delegation and automation | Qualify a chosen version before relying on autonomous backlog intake; stable and nightly are different baselines |
| Workspaces, provider profiles and model delegation do not establish OS isolation | Foundation must qualify access and workspace ownership for the actual host |
| Native permission review is distinct from independent code review | Preserve tests, separate candidate review and the owner's delivery decision or scoped delegation |

Primary sources: [T3 stable capabilities](https://github.com/pingdotgg/t3code/blob/v0.0.45/README.md),
[usage](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/usage.md),
[Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects),
[V2 operations](https://github.com/pingdotgg/t3code/blob/fd1c3386c4d60f3477ab3f13c87537848de099f5/docs/orchestration-v2/orchestrator-mcp-server.md),
[permissions](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/permission-modes.md).

The useful lesson from [Ras Mic's workflow](https://www.youtube.com/watch?v=blI10_91xgA)
is bounded work with worktree isolation, meaningful proof and review before
delivery. It is not evidence that infrastructure disappears or that all work
should merge automatically. [Matt Pocock's retrospective approach](https://www.aihero.dev/skills-retro)
supports improving methods from observed session friction, with judgment and
valid no-change outcomes. Warp's contributions workflow informed the earlier
UI iteration; it does not justify keeping a separate Factory interface once
native work surfaces meet the need. No third-party skill bundle is copied here.

T3 does not provide the application's hosting, databases, CI checks, backups,
deployment policy or production monitoring simply by being installed. Use the
application's chosen infrastructure and existing controls. The host must remain
available when clients disconnect. Upstream shutdown/reconnect reports
([15608](https://github.com/pingdotgg/t3code/issues/15608),
[16477](https://github.com/pingdotgg/t3code/issues/16477)) justify an actual recovery
test; they were inspected, not reproduced, in this research.

The next evidence is one qualified host/client route and one complete application
delivery, followed by a bounded Defence case. Measure verified outcomes, owner
interventions, rework and actual reported usage. No percentage saving, best-model
ranking or unattended-operation guarantee follows from this source review.

See the [qualification record](qualification.md) and [transition inventory](transition.md).
