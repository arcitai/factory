# Responsibility and access

Revision: 0.1.4 · Updated: 2026-10-09

Factory has three responsibilities around existing tools. It has no server,
provider adapter, task database or application runtime of its own.

| Layer | Owns | Does not establish |
| --- | --- | --- |
| Foundation | Project context, native setup, access choices and readiness checks; repair when these change | Product scope, continuous execution or readiness merely because files were installed |
| AgentOps | Research, priorities, assignments, exceptions and acceptance within delegated authority | Administrator access or permission to bypass review |
| ADLC | The concrete specification, implementation, independent review and authorized delivery | Authority to accept unrelated work or widen its own access |
| T3 and native harness | Conversations, models, worktree binding, native tools, permissions and recovery | Application deployment, monitoring or per-role OS isolation by naming a thread |
| OS and GitHub | Actual account/filesystem/process boundaries, token grants and repository protections | Independent review merely because CI is green |
| Application infrastructure | Hosting, data, deployment, health signals and recovery | A responsibility transferred to T3 by connecting the repository |

AgentOps remains responsible while ADLC works. Foundation is used when a setup
or context gap affects the task; it is not a stage repeated before every edit.
The owner decides admission and delivery by default, or delegates either for a
specific scope. A completed run is not acceptance; published is not installed.

## Where the work and authority live

| Resource | Normal location | Useful check |
| --- | --- | --- |
| Operator view | Desktop/phone connected to the selected T3 environment | Same project and thread; route actually in use |
| Agent processes and worktrees | Execution host, unprivileged service account | Native turn reports host, account, bound checkout and effective permission mode |
| Method and project instructions | Reviewed source plus selected native skill scope | Loaded sources match the adopted revision |
| Work status and delivery | GitHub issues/Projects, PRs, CI and releases | Actual fields, credentials and protections read back |
| Deployment/data/telemetry | Application's chosen infrastructure | Task-specific operation and recovery evidence |

A client can be on the execution machine itself and still connect to a different
OS account's service. Closing a client is safe only after service independence
has been tested. Power, network and encrypted-disk unlock remain host concerns.
A worktree prevents writers colliding in one checkout; it is not a security wall.

## Least privilege has more than one control

Instructions describe what an agent should do. Native permissions restrict tools
and selected shell/filesystem/network operations. The OS and remote services
restrict what the whole account and its credentials can do. These boundaries
complement each other; a provider profile or pinned AgentOps thread creates no
new OS identity.

AgentOps can have broader coordination authority while sharing workers' baseline
permissions. Additional repositories, telemetry or delivery operations are granted
only for a named need. If workers must be technically unable to use the lead's
credentials, use separate identities/environments or an appropriately isolated
runtime. A role instruction cannot provide that guarantee under a shared account.
The [setup guide](../foundation/factory-foundation/references/setup.md#least-privilege-in-practice)
contains the native configuration and expansion procedure.

## Sources kept by this package

| Need | Canonical source |
| --- | --- |
| Purpose and contributor rules | [Vision](../VISION.md), [README](../README.md), [AGENTS](../AGENTS.md) |
| Versions, checks and release | [Contributing](../CONTRIBUTING.md), [validator](../scripts/check.py), [tests](../tests), [CI](../.github/workflows/check.yml) |
| Dependencies and installation | Python standard library for optional helpers; pinned CI action; selected native tools/accounts in [setup](../foundation/factory-foundation/references/setup.md) |
| Access and changing claims | [Security](../SECURITY.md), [qualification](qualification.md), private installation [record](../foundation/factory-foundation/references/adoption.md) |

For applications, reuse their authoritative context. A separate dependencies,
observability or architecture document needs a real discovery/maintenance benefit;
see [project context](../foundation/factory-foundation/references/context.md).
Historical migration and rehearsal detail remains in the earlier reviewed releases.
