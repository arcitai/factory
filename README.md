# Factory

Revision: 0.1.5 · Updated: 2026-10-09

A practical method for building and improving applications with coding agents.

Use Factory when you want to give an agent an idea, a bug, a feature or an accepted
backlog and get back a useful decision or a verified change. It gives owners and
small teams a repeatable way to prepare a project, direct the work and review its
delivery. T3 Code provides the workspace, native harnesses run the agents, and
GitHub holds issues, pull requests and checks.

| Part | Responsibility | Example |
| --- | --- | --- |
| [Foundation](foundation/factory-foundation/SKILL.md) | Prepare and maintain the conditions for work | Connect the execution host; establish context, access and real delivery checks |
| [AgentOps](agent-ops/factory-agent-ops/SKILL.md) | Direct work within the owner's mandate, before and during execution | Investigate an idea, select accepted work, coordinate workers and bring back a decision |
| [ADLC](adlc/README.md) | Perform and verify a concrete task | Specify a feature, implement it, independently review it and deliver under the agreed rules |

ADLC means **Agentic Development Lifecycle**. The skills work with your
application's existing standards, tools and hosting choices.
AgentOps coordinates ADLC and calls on Foundation when setup needs repair.
These are responsibilities, not three servers or mandatory separate projects.

## Three access levels: owner, AgentOps and ADLC

Factory's access architecture starts with the human owner and gives each agent
only the access needed for its work:

- **You, the owner**, set the goals, approve or delegate decisions, and control
  which accounts, systems and permissions the agents may use. Personal and
  administrative access stays outside agent environments unless specifically granted.
- **AgentOps** directs the work within that mandate, assigns bounded tasks and
  brings back decisions. Any extra coordination or delivery access has a named
  purpose and scope; being the lead does not grant administrator rights.
- **ADLC agents** perform specific tasks in their assigned workspaces, using the
  tools and access needed to implement, test or independently review the change.
  They do not gain every permission held by the owner or lead simply by being delegated work.

Foundation prepares and checks these boundaries through the selected OS accounts,
environments, native harness sandboxes and service permissions. It tests both an
operation that should work and one that should be refused, and records the limits.
Least privilege applies at all three levels; additional access can be configured
for a concrete need and removed afterward.

Three access levels describe the intended responsibility and permission model.
Claiming **three isolated environments** also requires technical separation. In a
shared-account setup, AgentOps and workers can still reach the account's shared
resources; separate threads, skills and worktrees do not change that. Use separately
qualified identities/environments when workers must be unable to use the lead's
resources. The [architecture](docs/architecture.md#three-level-access-architecture)
and [setup guide](foundation/factory-foundation/references/setup.md#least-privilege-in-practice)
explain the controls; the [qualification record](docs/qualification.md) states what
has actually been demonstrated.

## Start

You need a repository, an execution machine, access to the selected coding
provider and permission to work with the repository on GitHub. T3 Code is the
reference workspace; another capable harness can use the skills after its
loading, access and execution behavior have been checked.

1. Follow the [setup guide](foundation/factory-foundation/references/setup.md)
   to connect the chosen host and clients, authenticate the tools and adopt the
   skills from a reviewed Factory release. It also covers least privilege,
   updates and recovery. Its worked example uses a Linux host and a Mac client.
2. Ask Foundation to assess and prepare your project. Reuse existing instructions,
   configuration and documentation; establish the missing context and real checks
   needed for the intended work. The [GitHub guide](foundation/factory-foundation/references/github.md)
   covers repository access, work tracking and delivery protections.
3. Keep a pinned **AgentOps** thread in your project. Use the
   [workspace guide](foundation/factory-foundation/references/workspace.md) to
   activate its role, then give it one bounded task and verify the result.

Give the lead an idea, a specific task or an accepted backlog. Examples:

- “Research this approach against our product goals. Recommend adopt, experiment,
  defer or reject. Bring me the decision before adding implementation work.”
- “Fix this accepted bug, run the relevant checks and get independent review.
  Bring me the candidate before merge.”
- “Work through these accepted issues in order. You may merge and release work
  that passes our rules. Ask me if new scope or significant risk changes the decision.”

There are two default human decisions: **admit work to the implementation
backlog**, and **accept its delivery before merge/release**. The owner may delegate
either decision for an explicit scope. Retain that delegation throughout the
task. Tests and independent review still apply, and material new risk can require
the owner to reconsider. See [the operating policy](agent-ops/factory-agent-ops/references/policy.md).

## How much is verified?

A published method release is not an installed or qualified system. Verify your
selected host, tools and a real task before relying on unattended operation.
The [qualification record](docs/qualification.md) separates package checks,
behavioral exercises and live proof. Skills guide work; the native tools and
infrastructure enforce access and run it.

Start both AgentOps and workers with only the access they need. AgentOps may
coordinate more work without having administrator rights. A wider grant needs
a concrete purpose and scope; a thread title or skill does not enforce it.
The [access section](foundation/factory-foundation/references/setup.md#least-privilege-in-practice)
explains the native controls, their limits and how to add access deliberately.

See the [architecture](docs/architecture.md) for responsibility boundaries and
[contributor guide](CONTRIBUTING.md) for versioning, checks and releases.
The earlier [migration audit](https://github.com/arcitai/factory/blob/v0.1.3/docs/transition.md)
and [research decision](https://github.com/arcitai/factory/blob/v0.1.3/docs/decision.md)
remain in release history; they are not prerequisites for a new installation.

MIT licensed. Existing application licenses, third-party tools and provider
subscriptions retain their own terms.
