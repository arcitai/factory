# Responsibility and access

Revision: 0.1.6 · Updated: 2026-10-09

Factory has three responsibilities around existing tools. It has no server,
provider adapter, task database or application runtime of its own.

| Responsibility | Owns | Does not establish |
| --- | --- | --- |
| Foundation | Project context, native setup, access choices and readiness checks; repair when these change | Product scope, continuous execution or readiness merely because files were installed |
| AgentOps | Research, priorities, assignments, worker model choices, reviewed skill/context improvements and acceptance within delegated authority | Administrator access, permission to bypass review or self-installed skills |
| ADLC | The concrete specification, implementation, independent review and authorized delivery | Authority to accept unrelated work or widen its own access |
| T3 and native harness | Conversations, models, worktree binding, native tools, permissions and recovery | Application deployment, monitoring or per-role OS isolation by naming a thread |
| OS and GitHub | Actual account/filesystem/process boundaries, token grants and repository protections | Independent review merely because CI is green |
| Application infrastructure | Hosting, data, deployment, health signals and recovery | A responsibility transferred to T3 by connecting the repository |

AgentOps remains responsible while ADLC works. Foundation is used when a setup
or context gap affects the task; it is not a stage repeated before every edit.
The owner decides admission and delivery by default, or delegates either for a
specific scope. A completed run is not acceptance; published is not installed.

## Three-level access architecture

The three access levels are **human owner → AgentOps → ADLC workers**. The arrows
mean scoped authority and assignments, not inherited credentials. Foundation
prepares and verifies the environments and controls for these levels; it is not
a fourth privileged agent tier.

| Level | Normal responsibility and access | Example of a separate grant |
| --- | --- | --- |
| Human owner | Sets the mandate and controls personal, administrative and account access | Authorizes a specific staging deployment without sharing a personal admin session |
| AgentOps | Works across Factory and the adopted repository within the mandate: reads project state, coordinates accepted work and reviews outcomes | A staging-only deployment identity for the authorized delivery step, kept outside implementation workers |
| ADLC worker | Uses its narrower assigned task workspace, build/test tools and task-specific services; reviewers get the candidate and evidence | Access to the specific test service needed to verify the change, with a removal condition |

Each level gets the least access needed. AgentOps can coordinate more while using
the same restricted baseline as a worker; broader access is an explicit exception.
For example, assigning a bug fix need not expose deployment credentials to the
implementer. Deliver through the selected, authorized identity after review.

Whether that separation is enforced depends on the actual setup. If the lead and
worker share an OS account and accessible credentials, the table describes their
responsibilities but does not prevent a worker from using the lead's access.
Use separately qualified OS identities/environments or an isolated runtime when
that prevention is required. Native sandboxes must be tested for the specific
tools, paths and services in use. Record the demonstrated boundary rather than
calling three role names three isolated environments.

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
