# Adoption record

Revision: 0.1.10 · Updated: 2026-10-10

Foundation identifies the appropriate existing project/adoption record and
establishes the relevant choices. AgentOps maintains them and scoped exceptions
for its current project within the owner's mandate. Extend that record;
do not create a separate register or require the whole inventory for every project.
Record choices that need to survive the task, affect later work or need removal,
not every transient task choice. Unknown is a visible gap, not a made-up default.

Version safe project-shared policy in the repository where useful. Keep host
identities, private paths, account references and sensitive evidence in the existing
private installation record; share only sanitized summaries. Credentials belong
only in actual secret stores. Executable native configuration is the source of
truth for applied state: link to its owning source/control instead of copying
values uncritically. An observation may quote a safe value with its source and date.

## Persistent choices and exceptions

Use short prose or a small table with only meaningful fields:

| Distinction | Useful content |
| --- | --- |
| Scope | Affected project, environment and role; requested scope versus actual account, provider, global, project, chat or task scope |
| Intent | Requested or approved value/capability, source, owner, authority and reason; the default displaced by a scoped exception |
| Application | Owning native configuration/control, actual applied scope and application date, or unapplied/uncertain status |
| Verification | Dated effective-state readback and relevant operation/outcome, with version and evidence; keep unverified claims visible |
| Upkeep | Relevant review trigger, expiry/removal condition, responsible owner and rollback/recovery route; verified removal when due |

Requested intent, approved intent, applied settings and observed behavior are
different states. A provider-wide setting or grant is not project isolation. If
the native control cannot isolate the requested project, record that limitation
and resolve an authorized supported boundary before applying; do not silently
propagate the choice to other projects. The record grants no authority, enforces
no access and applies no configuration. Factory Markdown does not apply itself.

For an authorized persistent change:

1. Read effective native state and its source, including overrides; assess the
   real scope and affected projects before changing it.
2. Reuse existing authority and its conditions. Resolve only missing authority or
   material new scope/risk under the two decision points; retain the prior state
   and a relevant recovery route.
3. Apply through supported native controls and verify meaningful readback at the
   affected scope, plus the operation or boundary the claim relies on. A failed
   or uncertain apply remains unverified; reconcile actual state before retrying.
4. Update the existing record without secrets, preserving intent versus applied
   scope and observed proof. For a temporary grant or override, use native expiry
   where supported or assign its actual removal; verify revocation/removal when
   due and record the result. Prose expiry does not enforce itself.

Reconcile affected entries on relevant setup, configuration or provider upgrades,
incidents and task needs. Preserve unchanged evidence at its observed date; no
watcher or expensive full scan is required on each run.

The reviewable intent and reproducibility principle is informed by Warp's
[versioned definitions](https://docs.warp.dev/factories/factory-as-code/) and
[agent configuration](https://docs.warp.dev/factories/factory-agents/), read
2026-10-10. Factory retains its existing records and native controls, with no
imported schema or runtime.

## Relevant installation context

Reuse the following existing choice families only where they matter:

- Project, owner, approved vision, canonical instructions and actual repo/branch.
- Routes to relevant architecture, checks, dependency/configuration sources and
  operational guidance. Preserve the project's existing names and records.
- Execution host and OS identity, client route, service owner, native versions,
  provider profiles and billing/usage source.
- Model profile: a small editable default per role or kind of work, such as lead
  research, implementation, independent review and small mechanical work, with
  any concrete exception and its reason. Use live native provider, model and option
  IDs/values. Mark each entry as owner-selected or proposed, and keep it separate
  from configured settings and observed child readback. Explicit owner choices
  prevail. Refresh it when models, requirements or retained outcomes change.
- Selected skills, Factory tag/revision, stage hashes, installed paths, preserved
  local changes and observed native discovery.
- Ops thread identity, project/workspace binding, role/source paths, pin and
  auto-settle choice; explicit source loading distinguished from native discovery.
- Each client's saved service connection and Local environment choice; observed
  execution host, OS/account and workspace, distinguished from the client device.
- Selected update channels and native installer/updater ownership; checks versus
  automatic installs, idle/interruption rules, recovery and last observed result.
- AgentOps scope (Factory and the adopted repository) and the narrower ADLC task
  workspaces. Record each extra grant separately from that baseline: who or which
  role, target, environment, purpose, date, authorizer, expiry/removal condition
  and readback, without secrets; user-editable versus managed controls.
- Effective filesystem/network/tool boundaries, allowed data destinations,
  deployment credential requirements and private security reporting route.
- Work-status source and actual Project/field/label identifiers; priority and
  readiness policy; issue intake and trusted owner identity.
- Admission authority and delivery authority separately, including explicit
  delegation and conditions. State any pause/risk conditions that change them.
- Real checks, required GitHub rules, review context, release/deployment policy
  and recovery route.
- Application environments separately from the execution host: chosen platform,
  artifact/deploy route, data/migrations, allowed agent access, rollback and the
  last observed restore where recovery of state matters.
- External services/connectors and their dependent features: configuration owner,
  required access, actual operation checked and remaining gaps. Installed,
  authenticated, resource-accessible and usable are separate observations.
- Operational signals, their locations, access/redaction/retention, response owner
  and runbook. Retain the result of relevant health, alert and failure-path checks.

For each claimed capability retain the tested revision/version, action, outcome,
date and evidence. Relevant proof includes:

1. Correct native account, tools and skill discovery at the selected scope.
2. One real task through independent review and authorized delivery.
3. Permission refusal/unavailable provider is visible and does not become success.
4. Client disconnect and reconnect; then controlled interruption/restart with
   native state reconciled and no duplicate writer or replayed external action.
5. The actual phone/remote decision route if selected.
6. A representative isolation check for each trust boundary being claimed.
7. Readback of actual GitHub status/protections and delivered application behavior.

Keep source inspection, disposable rehearsals and live installation evidence
distinct. One successful run qualifies that path, not every model or future update.
Record the next required observation for each incomplete capability.
