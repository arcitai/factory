# Transition from the previous Factory

The owner selected a public method/setup package around T3 Code on 2026-10-07.
The prior [factory-software-defence](https://github.com/arcitai/factory-software-defence)
repository and releases remain historical sources. No old runtime history is
copied into this public package, and this transition does not stop an installed
service or archive the previous repository.

The audited source is release 0.18.11, main commit
`1b126c200c59f33005fc9f86ab82565a9f4a406b` (same tree as reviewed commit
`835e664b79d12779c4e311779fa2a3cad5a4d08c`). The
[complete file inventory](legacy-inventory.csv) accounts for all 142 tracked
source files in that baseline. This is a disposition audit, not a claim that
retired runtime behavior was ported or re-tested.

| Prior responsibility | Destination |
| --- | --- |
| Foundation | Rewritten portable skill with host/client, GitHub and adoption guidance |
| Six ADLC skills | Rewritten without Inbox/native bridge or fixed lifecycle-label assumptions |
| Agent Ops proposal | A standalone skill with idea research, assignments, backlog and scoped delegation |
| Dashboard, charts, forms and UI build | Omitted; use T3 and GitHub's native surfaces |
| Provider adapters, authentication, usage collection and session bridge | Omitted; native harness/T3 responsibility |
| Factory service, HTTP API, receipts, process control and updater | Omitted; native service/state and explicit migration qualification |
| npm CLI, lockfiles and runtime dependencies | Omitted; no npm or SDK distribution in the new package |
| Fixed phase/label catalogs | Omitted; adopting project's actual GitHub Project fields and labels are canonical |
| Runtime/integration tests and generated assets | Omitted with the code they verified |
| Export/validation/release tooling | Small local skill-staging and package checks; Git tags/releases |
| MIT attribution | Preserved from the original method; no bundled third-party runtime/font/UI payload |

The staging helper is retained for one setup responsibility: produce a fresh,
inspectable selected skill bundle with licenses and provenance. It does not become
an installer, daemon, provider manager or another executable Factory control plane.

## Existing installations

Keep the previous installed version available while qualifying the replacement.
Record active work and private native history. Choose a separate T3 workspace and
profile; do not start a second writer in the same checkout. Reusing an account
does not imply live-session migration between different runtimes.

Qualify one task, review, authorized delivery, disconnect/reconnect and recovery
before changing daily operation. Back up the actual native state before version
transitions. Retire only the identified obsolete service, timers and launch routes
after accepted cutover; preserve credentials/history needed by remaining tools.
No automated deletion or credential copying is part of this package.

## Issue continuity

Create focused new issues for the remaining method and qualification outcomes.
Link relevant old issues and distinguish completed package work from future live
proof. Retire obsolete custom UI/adapter proposals as superseded by this accepted
direction, rather than pretending those implementations were completed.
Keep the old repository recoverable until installation migration is accepted.
