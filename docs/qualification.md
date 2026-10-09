# Qualification

Revision: 0.1.4 · Updated: 2026-10-09

This record distinguishes source review, disposable exercises and observed native
operation. A package release does not qualify another host, every future update
or an application deployment. Detailed private transcripts, identities and state
remain with the installation; public issues track the remaining acceptance work.

| Boundary | Observed evidence | Limit / next check |
| --- | --- | --- |
| Package | Eight portable skills, metadata/link checks and staging tests | Mechanical checks do not establish agent decisions |
| Earlier method cases | Opus cases exercised admission, delegated delivery, proportional context and review handoffs | Text-only cases had failures, including invented provenance; preserved in the [v0.1.3 rehearsal record](https://github.com/arcitai/factory/blob/v0.1.3/docs/rehearsals.md) |
| Native delegation | Nightly 2861: Opus 5.5/High delegated separate Codex review; a fresh review found and led to fixes | One assisted path, not arbitrary application quality or unattended acceptance |
| Concurrent writers | Nightly 2861: two Opus workers ran in distinct native-bound worktrees with overlapping run times; main stayed unchanged | Same account; worktrees are not OS isolation |
| Deferred completion | Worker background completion started further runs; the lead waited before cleanup | First-run completion alone did not mean work was finished |
| Mac independence | A Connect-launched task continued and delegated after the Mac app quit; reopening recovered the same thread | Host power/network still required |
| Phone | Owner confirmed Factory and pinned AgentOps visible in the iPhone beta | Background notification and a real question/response remain unproved |
| Service interruption | A bounded worker wrote its marker once; restart cancelled the run; one deliberate follow-up inspected state | No duplicate write observed; this was not automatic completion of the interrupted task |
| Physical host reboot | 2026-10-09: boot identity changed, service returned after the owner unlocked the disk; message contents and adopted skills were preserved; an Opus readback completed | Mac initially used saved SSH fallback; returning to Connect required a manual reconnect. Network-loss/lid behavior still open |
| Project cleanup | Nightly 2873: native removal deleted two obsolete project registrations and their four archived chats from the picker; active Factory stayed | Source folders remained; the specifically identified recent backup was deleted at owner request, not every historical copy |
| Native update paths | T3 server updated to 2873 and preserved 216 message texts; Codex 0.162.0 and Claude 2.1.295 installed under the execution user | Root-owned copied launchers had broken updater detection. New native launchers repaired that path; future automatic installation is not established for every tool |
| Claude automatic updates | `claude doctor`: native installation, latest channel, auto-updates enabled, no installation issues; subscription authentication retained | New versions apply to later processes; this is not a future compatibility guarantee |
| Access | Unprivileged host account could not access the personal home or Docker socket; no effective worker sudo | AgentOps and ADLC still share the account and its GitHub identity |
| Codex workspace sandbox | 0.162.0 native `:workspace` probe: workspace write succeeded and the outside write failed with read-only filesystem | This tests the installed native sandbox, not a new T3-launched turn |
| Claude Bash sandbox | 2.1.295 terminal probes: workspace write succeeded, outside write failed with read-only filesystem; explicit user settings loaded | T3 launch configuration is set to load that user policy; an actual T3-launched sandbox probe is still required. File tools/MCP/hooks are separate boundaries |
| System maintenance | Omarchy 4.0.4-1 source/config inspection found native update checks and an interactive system-update path | No unattended OS installation enabled; prompts, administrator access, snapshot coverage and encrypted boot remain relevant |

The older [Nightly 2861 record](https://github.com/arcitai/factory/blob/v0.1.3/docs/qualification.md)
retains the original migration counts, approval friction and limitations. Updating
this document does not change those observations to the newer build.

## Current setup baseline

The setup guide references T3 `0.0.46-nightly.20261009.2873`, upstream
`ec80933ac8cd02fec5c97b342462ccc9567cdb1e`, inspected 2026-10-09. The server and
operator desktop version matched after the update. Subsequent provider and sandbox
changes need their own native T3 readback; the operator desktop was locked during
that part of qualification. Do not report the pending UI/turn check as passed.

Codex native Auto policy and Claude approval mode were inspected in T3's adapters.
The two providers do not implement an identical boundary. Claude's user-editable
sandbox settings are configured protection, not a managed per-role policy. No
blanket administrator access or cross-role credential isolation is claimed.

Native scheduled intake was researched against Nightly 2861 and deliberately
deferred; no Factory queue or scheduler was built. That decision is distinct from
using native provider update facilities. No OS/server auto-install schedule has
been qualified or enabled by this release.

## How to qualify a change

Run `python3 scripts/check.py` and `python3 -m unittest discover -s tests -v`.
For changed instructions, use a fresh context with realistic requests. Inspect
resulting actions/artifacts, not keyword presence. Include missing and explicit
delegation, new risk and untrusted input when those boundaries change. Independent
review must inspect the actual final candidate; record findings and repairs in
its PR. Do not consume quota merely to manufacture a limit condition.

For host changes, retain exact versions, command/result, date and limits in the
private adoption record. Exercise allowed and denied operations. A native CLI
probe does not by itself prove the same configuration in a T3-launched session.
Read back publication separately from installed files and loaded skills.

Open acceptance work lives in [Factory issues](https://github.com/arcitai/factory/issues):
actual phone decisions and remaining recovery cases, end-to-end application
adoption, and a separately authorized Defence case. These do not become complete
because the method package passes its checks. Kastanje product work remains parked.
