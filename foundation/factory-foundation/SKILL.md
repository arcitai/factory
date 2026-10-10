---
name: factory-foundation
description: Prepare or assess a repository and execution host for Factory, including native harness access, selected skills, GitHub work tracking and delivery checks.
license: MIT
metadata:
  version: "0.1.8"
  updated: "2026-10-10"
---

# Factory Foundation

Use for requested setup, adoption, migration or readiness assessment. Assessment
is read-only. Preserve the application's existing vision, instructions, code,
standards and useful work. The setup request does not create product scope.

Identify the repository, owner, intended work, execution host, operator entry
point and delivery destination from accepted context. Resolve facts from the
actual environment before asking for a missing owner decision. Record only
what changes setup, authority or proof in the project's existing private record;
the [adoption outline](references/adoption.md) is available if one is missing.

Assess two scopes separately: the **execution host** that runs the agents and
the **application repository** they will work on. Reuse applicable host proof
when adding a repo; recheck affected capabilities when versions, identities,
configuration or access change. Repository readiness still needs its own sources,
tools, checks and delivery boundary. Application hosting is part of that repo's
operating needs, not automatically the agent execution host.

For T3 host/client setup use [the setup guide](references/setup.md).
For a pinned AgentOps thread, its skills and the host/client connection,
use [the operator workspace guide](references/workspace.md).
For GitHub Projects, labels, PR and CI use [repository preparation](references/github.md).
For application context, dependencies, operation and living documentation,
use [project context](references/context.md).
Keep the method independent of a particular model and personal plugin.

Prepare only the chosen capabilities:

- Find the authoritative project sources and concrete gaps for the intended work.
  Reuse existing docs, code/configuration and checks; establish missing context
  according to the product's purpose and actual risks. Weigh setup and upkeep
  against the benefit; the task does not require perfecting the whole repo.
  Keep the agent host distinct from application operation.
- Confirm the native versions, selected provider account, effective tools and
  permissions. A discoverable binary or copied skill does not establish readiness.
  Record the project's small model profile from live native IDs and owner choices.
- Start AgentOps and workers with least privilege. Distinguish coordination
  authority from enforced OS/tool/credential access. For a wider grant, identify
  the required action, target, authorizer and removal condition; apply the smallest
  native change and test an allowed and refused operation. Never make the lead
  an administrator merely because it coordinates workers.
- Scope the lead role to its chosen thread; an existing project is sufficient
  when it has the intended access. Separate credentials/access where required.
  A profile separates configuration/history, not OS access. Qualify the actual filesystem
  and network boundary; use a separate OS identity/environment where required.
  Prove each tool boundary the work relies on, such as shell, native file tools or
  MCP, in an actual launch with its effective settings source; a settings file's
  presence is not proof. Record success, permission denial, approval request and
  OS refusal as different results.
- Stage and review selected skills before native project/profile adoption.
  Keep one canonical copy, verify discovery in each chosen harness and preserve
  local adaptations on updates. Never install personal context as a dependency.
- Prepare meaningful project checks, work tracking and delivery protections.
  Preserve existing field/label conventions and read settings back from GitHub.
  A local workflow file does not prove service-side protection is enabled.
- Record admission and delivery authority, including explicit delegated decisions,
  approved data destinations and material risk/escalation conditions.
- Qualify service startup, client disconnect, restart and recovery on disposable
  work before relying on unattended operation. Reconcile active/unknown writers
  before stopping a service or changing its version.
- Establish the selected native update channel, updater ownership and maintenance
  boundary. Update checks are not automatic installs; interrupted turns, OS prompts
  and encrypted-disk unlock need an explicit recovery route. Preserve skill-local
  changes when adopting a new reviewed version.

Finish with one short readiness result in the existing project record, scoped
to the intended task. For each relevant capability, identify its host/repo scope,
owning source, **verified**, **required gap**, or **conditional/not needed**
disposition, and dated proof or the next action and responsible role. Explain
conditional choices; do not treat an unchecked requirement as not needed.
Include versions and identities without secrets. Hand this result to AgentOps,
which can start authorized, ready work and route setup repairs back to Foundation. ADLC keeps
affected application sources and checks current during delivery. A gap holds the
dependent capability, not unrelated work. Preserve unchanged proof rather than
rerunning the entire installation for every task.
Preserve native history and recovery material during migration. Retiring an old
runtime is a separate deliberate step after its replacement is qualified.
Foundation installs no Factory daemon and grants no authority beyond the request.
