# Factory

A practical method for building and improving applications with coding agents.

Factory prepares a project, gives its lead a way to turn ideas into decisions,
and carries accepted work through implementation, independent review and delivery.
T3 Code provides the working environment; native harnesses run the agents;
GitHub holds the work and its delivery evidence.

| Part | Use it for |
| --- | --- |
| [Foundation](foundation/factory-foundation/SKILL.md) | Prepare the host, repository, accounts, skills, GitHub Project and delivery checks |
| [Agent Ops](agent-ops/factory-agent-ops/SKILL.md) | Research an idea, challenge a proposal, coordinate a task or work through an accepted backlog |
| [ADLC](adlc/README.md) | Triage, specify, implement, independently review, investigate security and evaluate results |

These are ordinary Agent Skills. They do not require AIOS, a Factory server,
a model router or a dashboard. T3 Code is the reference setup; the method can
also be used in another capable harness after checking its supported discovery
and execution behavior. A skill describes behavior; it does not create tools,
permissions, background execution or isolation.

## Start

Follow the [host and client setup](foundation/factory-foundation/references/setup.md).
It covers a Linux execution host such as Z13, a Mac as the operator client,
native accounts and project-scoped skills. Then prepare the repository with
the [GitHub guide](foundation/factory-foundation/references/github.md).

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

## Adopt the skills

Clone a reviewed release of this repository. The small staging helper copies a
selected bundle into a **new** directory, including licenses and a hash manifest:

```sh
factory_stage_root="$(mktemp -d)" &&
  python3 scripts/stage.py foundation --output "$factory_stage_root/foundation" &&
  python3 scripts/stage.py agent-ops --output "$factory_stage_root/agent-ops" &&
  python3 scripts/stage.py adlc --output "$factory_stage_root/adlc"
```

Inspect the staged files, then use the guide to install only the appropriate
skills in the selected project/profile. The helper does not install tools,
change a repository, create GitHub resources, log in or start an agent.
Use a fresh staging directory on updates and review differences before adoption.
In a Git checkout, only tracked files are staged; add intended new resources to
Git first. A source archive has version/hashes but no Git revision claim. Keep
the manifest with the persistent private adoption record before removing the stage.

## Evidence and development

This initial method package is not a claim that unattended T3 operation has been
qualified on your host. The [qualification record](docs/qualification.md)
separates package checks, behavioral rehearsals and live installation evidence.
The [architecture](docs/architecture.md) defines responsibility and trust boundaries.
The [research decision](docs/decision.md) explains the choice of native tools and
the remaining operational proof.

Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests` to
check the package. Consumers do not need Python to read or use the skills.
The [contributor guide](CONTRIBUTING.md) explains changes and releases.

This is the method-focused successor to
[factory-software-defence](https://github.com/arcitai/factory-software-defence).
The [transition record](docs/transition.md) explains what was retained and retired.
The prior repository, releases and private runtime history are preserved.

MIT licensed. Existing application licenses, third-party tools and provider
subscriptions retain their own terms.
