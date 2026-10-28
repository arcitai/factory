![Factory — a method assembled from native tools](assets/branding/factory-banner.png)

# Factory

Revision: 0.1.26 · Updated: 2026-10-28

A portable method for using AI agents across software, BI, defence and research.
Start small, use existing tools, and add complexity when a real task needs it.

**[Read the practical guide and architecture](https://gustavanderson.notion.site/Factory-a-practical-guide-4046d2e17f568159a603de2dd6b91c2a)** — the public Notion home explains the method, diagrams, skills and current open choices.

Factory supplies methods and portable Agent Skills. Your chosen agent tools run
the work; their native configuration and service permissions enforce access.
T3 Code is our reference workspace. Codex, Claude Code or another capable native
setup can also be used after checking the capabilities the task needs. Choose
your own context home, tracker, source hosting and infrastructure.

## How it fits together

| Responsibility | Purpose |
| --- | --- |
| [Foundation](foundation/factory-foundation/SKILL.md) | Prepare the agent environment, project foundation, and operations and maintenance needed for the work |
| [AgentOps](agent-ops/factory-agent-ops/SKILL.md) | Lead one project: investigate, assign bounded work, coordinate review and deliver within the owner's mandate |
| Work modules | Supply domain methods and checks: [software](adlc/README.md), [scoped defence](adlc/factory-security/SKILL.md), and future dedicated BI and research methods |
| [Evaluation](adlc/factory-evaluate/SKILL.md) | Compare outcomes, defects, cost, time and human effort before recommending a change |

Independent review checks the actual result against the original requirements.
By default, use two fresh reviewers: one for objective/domain evidence, one for
qualitative intent, usefulness and experience. Delivery waits until both reviewers’ blocking concerns are resolved.
Projects and tasks can override roles, numbers and models within their mandate
and stronger requirements. Model judgments do not replace meaningful domain checks.

An optional [Factory entry skill](agent-ops/factory-entry/SKILL.md) helps your own
Planning Agent route requests to existing project leads. Each project keeps its
own AgentOps; Factory Lab develops this method rather than managing every project.

## Start with a new or existing project

1. Your Planning Agent can ask Foundation to prepare a new or existing project.
   Select the project's own context home and reuse its sources,
   useful conventions and existing checks; prepare only missing capabilities.
   Link the shared method rather than copying the public guide into every project.
   Follow [setup](foundation/factory-foundation/references/setup.md) for the
   selected native tools.
2. Select the declaration and skills, with their revisions. Our Lab's
   [YAML original lives in Notion](https://gustavanderson.notion.site/4056d2e17f56811b96fec7b970741916);
   [factory.yaml](factory.yaml) is a versioned export. AgentOps reads the
   declaration; it does not apply settings or grant access.
3. Give the project's AgentOps one bounded task. Check the result, get independent
   review, and deliver under the agreed authority.

**Already using Factory?** Use the same Foundation skill and its
[existing-project adoption guidance](foundation/factory-foundation/references/adoption.md#update-an-existing-project).
Compare the selected reviewed revision with local adaptations, update affected
routes and complete bundles, and prove discovery and use. A project shown in T3
has not automatically adopted the latest method. No extra migration agent or
synchronization service is needed.

## Context and distributions

Notion is our replaceable authoring home for shared methods, policies and skills.
The [Factory Skills library](https://gustavanderson.notion.site/5e1552911ffc42b8a999609cc6847a00)
contains their instructions and supporting files. Databricks remains a future
enterprise option. Project code, data, applied configuration, technical tasks and
results stay in their existing native sources. Keep one editable original.

A secret store protects stored values. When an agent must use a credential
without receiving its value, a native credential broker outside the execution
boundary can authenticate its service calls. Native controls and upstream service
grants still enforce what the agent can access. For details, see the public
[Context & access](https://gustavanderson.notion.site/Context-access-4056d2e17f5681e29517ecc664a137ed)
guide.

This repository contains reviewed portable distributions, bounded staging/check
helpers, and Factory Lab's technical work. Required references travel with each
skill. Use a reviewed release without live Notion access, or read the selected
Notion original and identify its revision. Changes go to their owning original
before a deliberate export; no process maintains two editable copies.
See [source ownership](docs/factory-definition.md) and [contributing](CONTRIBUTING.md).

## Where we are going

| Step | Status and next work |
| --- | --- |
| Method and distribution | The #98 transition is complete. Shared methods are authored in Notion and exported deliberately. This revision selects two independent reviewers by default, clarifies project context bootstrap and exports the Factory-only connection and execution-boundary guidance. |
| Factory Lab | The active AgentOps is pinned in the existing operator app. On 28 October, the dedicated Z13 Lab moved to official Nightly 3796 for native linked-environment delegation; stable 0.1.3 lacks that change. Factory-only Notion insert/update and two idle service-recovery cycles were observed. A native author → two reviewers → repair → two fresh reviewers path completed with one operator-detected approval, and a read-only reverse-control probe refused access to the lead. Approval notification, remote worktree isolation and on-demand per-agent provisioning remain gaps. [Isolation #32](https://github.com/arcitai/factory/issues/32) and [host adoption #34](https://github.com/arcitai/factory/issues/34) remain open for the limits below. |
| Improvement | Next: qualify automatic worker handoff and recovery before unattended intake. Later: [same-session comparisons #50](https://github.com/arcitai/factory/issues/50), [ZeroShot-style loops #97](https://github.com/arcitai/factory/issues/97), and [review quality #99](https://github.com/arcitai/factory/issues/99). Two reviewers are selected; automation and update ownership remain open choices. The target is AgentOps-managed, on-demand isolated sandboxes inside its own environment; provisioning and safe model/network access remain unqualified. |
| Other factories | Adopt the reviewed method project by project through Foundation, after the Lab path works. |

The [qualification record](docs/qualification.md) separates source checks,
synthetic exercises and observed native operation. A published package does not
install a connection, isolate workers or establish unattended operation.
The [technical architecture notes](docs/architecture.md) explain those boundaries.

## Decisions and credit

The owner decides admission and delivery by default and may explicitly delegate
either for a defined scope. Keep that authority through continuation and workers;
raise genuinely new material scope or risk. See the
[operating policy](agent-ops/factory-agent-ops/references/policy.md).

Substantially inspired by Zach Lloyd's [Factory Stack](https://www.warp.dev/blog/the-factory-stack)
and [Warp Factories examples](https://github.com/warpdotdev/warp-factory-examples).
Warp supplies a platform and native execution engine; this independent method
assembles existing capabilities. It does not claim Warp schema compatibility.

Factory's method, code and documentation are MIT licensed. Arc’ It AI branding
has [separate terms](assets/branding/README.md). Third-party products and projects
retain their own terms.
