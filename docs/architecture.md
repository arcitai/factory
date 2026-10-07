# Responsibility

```mermaid
flowchart TD
  Owner[Owner: idea, task or accepted backlog] --> Lead[Agent Ops lead]
  Foundation[Foundation: host and repo preparation] --> T3[T3 Code on execution host]
  Lead --> T3
  T3 --> Native[Native harnesses and models]
  Native --> Method[Selected ADLC skills and project instructions]
  Method --> GitHub[Issues, Projects, PR and CI]
  GitHub --> Delivery[Authorized application delivery]
  Lead --> Decisions[Admission and delivery decisions]
  Decisions --> Owner
```

The Mac/phone is an operator entry point. The Linux host runs T3, providers and
workspaces. Closing the client must not be assumed to preserve work until the
chosen service/connection has been tested. The host still needs power and network.
Application hosting is separate from the agent host.

Foundation prepares the environment and observes readiness. Agent Ops researches,
prioritizes within authority, delegates, handles exceptions and reports outcomes.
ADLC skills perform the relevant task; they are not mandatory sequential jobs.
T3/native tools own sessions, status, interruption and recovery. GitHub owns
work status and delivery records. No Factory runtime sits between them.

## Three different boundaries

- **Instructions:** selected skills, repository rules and accepted task context.
- **Native profile:** separate provider configuration, login, tools and history.
- **Host access:** actual OS user, filesystem, network and process permissions.

The first two do not enforce the third. T3 projects group work; they do not
sandbox the server account. A lead with cross-project oversight must not give
every worker all its context or credentials. Start with project-scoped work;
stronger trust separation uses distinct OS identities/environments or VMs.

The lead may read an idea without accepting it. Backlog status may describe
accepted work without starting an agent. A completed turn is not acceptance;
accepted code is not automatically merged, published or installed.

Use native worktree binding for concurrent writers. Delegating a chat can inherit
the parent's checkout, and changing directory inside a prompt does not necessarily
change the thread's bound workspace. Independent review uses the identified
candidate and a separate context. A second model alone does not prove independence.

Provider/model selection follows required capability, remaining judgment and
observed quota/cost. Start with a small supported set. The method does not hardcode
a best model, pool credentials or automatically buy overage. Usage comes from its
native source; missing data stays unknown.
