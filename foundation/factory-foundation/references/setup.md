# Set up the host and operator client

Revision: 0.1.7 · Updated: 2026-10-09

This reference setup uses T3 Code on a Linux execution host, with a Mac and
optionally a phone as clients. The host can be a laptop, workstation or VPS.
The method itself also works without T3 after qualifying
the chosen harness's discovery and operation.

Reference version: T3 **0.0.46-nightly.20261009.2873**; upstream setup guidance
checked 2026-10-09. This is a prerelease qualification baseline, not a guarantee
for every host or future Nightly. Keep the selected client/server/provider versions
and observed proof in the installation record. Native delegation and automation
need their own qualification; installing them does not authorize their use.
See [upstream installation](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/install.md).

## 1. Choose the boundary

Use an ordinary execution account on the host, with access to the selected repos
and tools. On a shared personal machine, prefer a dedicated VM with its own
unprivileged guest account. Keep the personal home, SSH agent, browser, clipboard
and host sockets outside it; admit shared folders/devices only for a stated need.
On a dedicated host, a separate unprivileged OS user may be sufficient for the
selected workload. It shares the kernel and is not equivalent to a VM.
Keep deployment/admin credentials outside implementation workers unless a task
explicitly needs them. A second T3 project or provider config directory under the
same OS user is not a filesystem sandbox.

Use one persistent AgentOps thread in the owner's existing project when it has the
right context and access. A separate lead project is optional, not a requirement.
Activate the lead role in that thread; preserve the project's shared instructions.
Workers receive the target project's context and skills. Separate provider profiles,
T3 environments/OS identities or VMs are appropriate when
the lead, workers or projects require different filesystem/network trust.
Do not copy a personal AIOS installation or personal provider home into this setup.

Preserve any old Factory runtime and private history while qualifying this setup.
Avoid pointing two active agent writers at the same checkout. Do not run native
services as root. Keep the host powered, awake and network-accessible.

## Least privilege in practice

Start AgentOps and ADLC workers on the same restricted baseline when that meets
the intended trust boundary. AgentOps has more coordination responsibility, not
blanket root, unrestricted network or deployment access. Keep the service account
out of sudo/admin and host-control groups. Use task-specific GitHub/deployment
access where available; native tool approval does not shrink a token's permissions.

| Control | Configure and prove | Limit |
| --- | --- | --- |
| Host account | Unprivileged account; personal home, admin credentials and host sockets inaccessible; prove an allowed operation and a refused one | Same-account processes and projects still share accessible resources |
| T3 mode | Begin with supervised for read-only assessment; for accepted editing, choose and read back the mode per provider and task | Each mode maps to a different provider policy; Auto is an approval policy, not one universal sandbox |
| Codex | In this T3 baseline, Auto maps to workspace-write with on-request approval and native auto-review; supervised maps to read-only | T3 supplies the runtime policy; a CLI configuration default alone does not prove the T3 turn uses it. Measure its boundary separately from Claude's |
| Claude | Enable native Bash sandboxing and the outside-read block in the selected profile; disable unsandboxed retries and fail if sandboxing is unavailable; qualify Auto-accept edits where outside file edits must wait for approval; prove each in an actual T3-launched turn | Bash sandboxing does not enclose file tools, MCP servers or hooks. The read block does not stop writes, and in Auto outside native edits were not held |
| GitHub / delivery | Read effective repository, Projects and workflow permissions; use narrower credentials or a separate delivery identity where needed | A shared login remains shared access, even when commits credit several agents |

For a selected Claude profile on a supported host, this is a minimal configuration
to merge deliberately into its existing settings, not overwrite them. The read
block requires Claude Code 2.1.257 or later:

```json
{
  "permissions": {
    "blockReadsOutsideWorkingDirectories": true
  },
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false
  }
}
```

Install the native dependencies first. Check which setting sources and working
directories the T3/SDK launch actually uses; CLI and SDK defaults can differ, and
a launch that loads only user settings ignores a project-local file. Start a new
session after a change. Test a permitted workspace write and a denied write to a
disposable path outside it, without retrying outside the sandbox. Then test native
Read, Edit and Write inside and outside the workspace, plus required network
destinations and MCP operations. A terminal probe or a present settings file is
not a passing T3 integration test. Keep configured and demonstrated controls separate.

In this T3 baseline, Auto maps to Claude's `auto` mode and Auto-accept edits to
`acceptEdits` with T3's approval callback. In a qualified launch with the read
block, Auto still let native Edit and Write change files outside the workspace.
When outside file edits must wait for a person, qualify Auto-accept edits for that
Claude worker: workspace edits proceed, while outside edits, many shell commands
and explicit reads of installed skills can each ask for approval. Budget that
attention; keep a declined operation declined rather than retrying it through
another tool. This is assisted operation with user-editable guardrails, not
unattended throughput, an unbypassable policy or role/process isolation.

Native sandbox defaults may allow broad reads. Keep credentials outside the
agent's accessible environment where possible, and use native read-deny/credential
controls for selected secrets. User-editable settings are a guardrail, not an
administrator-enforced policy. For non-bypassable restrictions, use managed native
policy controlled outside the agent's identity, plus OS/remote-service enforcement.
Do not install a machine-wide policy blindly on a shared personal host.

**To add access:** name the operation and target, choose the smallest native grant
(path, domain, tool, repository or deployment environment), identify who authorizes
it, and set its duration or removal condition. Apply at the appropriate control,
read it back, and prove the required operation while an unrelated operation still
fails. Remove temporary grants afterward. Avoid changing every thread to Full
access to resolve one denied build command. If AgentOps needs access that workers
must not possess, use separate identities/environments; a title is not an ACL.

Sources: [T3 permission modes](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/permission-modes.md),
[T3 Claude mode mapping](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/apps/server/src/orchestration-v2/Adapters/ClaudeAdapterV2.ts#L1511-L1603),
[Codex permissions](https://learn.chatgpt.com/docs/permissions),
[Claude permission modes](https://code.claude.com/docs/en/permissions),
[Claude read restriction](https://code.claude.com/docs/en/settings-reference#permissions-blockreadsoutsideworkingdirectories),
[Claude sandbox scope and enforcement](https://code.claude.com/docs/en/sandboxing).

## 2. Install and authenticate on the execution host

Install Git, the GitHub CLI and the native provider CLIs using their supported
instructions. Prefer a maintained native installation owned by the execution user
for provider CLIs. Point T3 at its stable launcher, not a copied versioned binary
under an administrator-owned directory; copied binaries can break native updater
detection. Keep provider profiles and credentials unchanged when repairing paths. Inspect versions and authenticate the intended execution account.
Repository and Project operations need appropriate GitHub access; deployment
credentials are a separate decision. Follow the
[GitHub connection checks](github.md#qualify-the-connection) for CLI, Git and
Project access on that same account and the native T3 readback.

Install a selected T3 release using its official installer. For the documented
baseline, download and inspect the script before executing it:

```sh
factory_install_dir="$(mktemp -d)" &&
  curl -fsSLo "$factory_install_dir/install.sh" https://t3.codes/install.sh &&
  less "$factory_install_dir/install.sh"
```

After reviewing that downloaded script, execute the same file:

```sh
T3CODE_CHANNEL=nightly T3CODE_VERSION=0.0.46-nightly.20261009.2873 sh "${factory_install_dir:?Use the directory from the successful download and review above}/install.sh"
```

Use the installer-reported binary path if `~/.local/bin` is not on `PATH`.
Check `t3 --version`, `codex --version`, `claude --version`, `git --version`
and `gh --version` as the account that will run the service.
Stop and reconcile if the reported T3 version differs from the selected version.
Select the official Nightly release, not a maintainer's `preview` build. Keep all
clients on a compatible orchestration protocol and check the provider compatibility
reported for that release before starting agent work.

In T3's provider settings, choose separate Codex and Claude configuration
directories for this work. Authenticate against those same paths on the host:

```sh
factory_codex_profile="$HOME/.local/share/factory-profiles/codex"
factory_claude_profile="$HOME/.local/share/factory-profiles/claude"
mkdir -p "$factory_codex_profile" "$factory_claude_profile"
chmod 700 "$factory_codex_profile" "$factory_claude_profile"
CODEX_HOME="$factory_codex_profile" codex login
CLAUDE_CONFIG_DIR="$factory_claude_profile" claude auth login
```

Open the provider's login link in the browser you use, complete authentication,
and finish any native callback on the execution host. The browser may be on the
host or another machine. Keep codes and credentials out of issues and docs.
Use the provider's documented remote/device-login route if its callback requires it.
Verify the account in T3; a browser login alone does not prove the CLI profile is
authenticated. Existing dedicated profiles may be reused deliberately without
copying their credentials into a new location.

Start with Codex and Claude if those are the selected subscriptions. Choose models
from the actual provider catalog; use the owner's selection and measured results.
Extra providers and automatic model routing are optional. Usage belongs in T3;
API-equivalent estimates are not subscription charges and missing limits are unknown.

References: [Codex profiles](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/providers-codex.md),
[Claude profiles and skills](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/providers-claude.md),
[usage](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/usage.md).

## 3. Make the service independent of the client

On the host, as its execution user:

```sh
t3 service install
t3 service status
```

Linux uses a systemd user service. Confirm the service is running, enabled and
able to survive logout. If setup reports that lingering needs an administrator,
complete only the reported host-administration step with that administrator.
Do not solve it by granting the worker unrestricted sudo.

Use T3 Connect or the supported direct/private-network connection to the already
running service. Do not assume a server started and managed by a desktop SSH
connection survives closing that client. Qualify the selected route under load
and reconnection: [known shutdown/reconnect report](https://github.com/pingdotgg/t3code/issues/15608).
Inspect service ownership before mixing multiple launch methods.

Before an update or restart, read active work and arrange interruption/recovery.
Pin versions for a qualification run. Stop the service and privately back up its
`userdata`, service configuration and prior version before a major migration.
The backup contains credentials and history; keep it with restricted access on
the execution host. Restart the service after the consistent backup, then use the
native update path, for example:

```sh
t3 update 0.0.46-nightly.20261009.2873 --channel nightly
```

The restart interrupts active turns. V2 copies `state.sqlite` to `statev2.sqlite`
once, preserving the V1 database. Later activity in the two versions does not
sync. Messages and thread metadata migrate; live provider sessions, old tool
activity, approvals and checkpoints do not. The first continued turn must reload
instructions, skills and outstanding decisions. Preserve the recovery copy;
inspect it read-only if needed. A binary downgrade alone is not a data rollback.

Upgrade every operator client to a compatible V2 build, then verify the service,
connection route, projects, pins, archives, transcripts and a harmless provider
turn. Record missing history or changed behavior before restarting real work.
[Updating](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/updating.md),
[V2 migration and backup](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/thread-migration.md).

## 4. Connect the operator clients

Install the matching T3 desktop release on the Mac. Use **Settings → Connections**
to connect to the host and verify the displayed execution environment before
starting work. Provider logins, tools, repos and worktrees for remote tasks belong
on the host. The Mac does not need another set of worker credentials for those tasks.

A desktop app running on the host is also a client. If it runs as a different
OS user, connect it to the existing execution service rather than importing the
same repositories into that user's local environment. Use native pairing to its
reachable endpoint; on the same host this can be the service's loopback address.
For a saved SSH environment, verify that it attaches to this independent service
instead of starting a desktop-managed server. Check service ownership and process
identity, then prove a bounded task survives closing the client and is readable
after reconnect. If service reuse is not established, use Connect or supported
direct/private-network pairing to the existing service. Verify both clients show
the same project and thread history, not two independent copies.

**Local environment** controls the extra backend managed by that desktop client.
For a client used only to access the execution service, turn it off under
**Settings → Connections**, using T3's native restart confirmation. First reconcile
any local work and confirm the saved service connection. This does not stop the
independent systemd service, even when the client is on the host itself. Keep it
on if local work is also intended. Local history and remote connections are retained.
After restart, check the toggle, Connected status and the same thread; check that
the execution service remained active. Avoid manually editing T3's database.

Check the permissions of the route actually in use; saved routes can have different
sessions and grants. A migrated connection notice does not authorize broader access.

Pairing links are credentials. Transfer them directly into the intended client,
then verify readback and remove temporary copies. If typing a full link fails,
use the dialog's separate Host and Pairing code fields. Reconcile an uncertain
pairing before creating another. Do not import a personal browser profile to solve
an execution-host login, or infer GitHub CLI access from a browser session.

T3 Connect links environments through its native account flow, including headless
hosts. When Connect and mobile notifications are selected, a headless host with
an existing service can use the following as its execution account. Reconcile
active runs and known background work before the restart:

```sh
t3 connect link --headless
t3 connect publish
t3 service restart
t3 connect status
```

Complete the account login and native relay-client installation prompts. Linking
finishes asynchronously after the service starts; saved authorization alone is
not reachability. Reuse that service rather than starting another server. Sign
in to the same T3 account on each client. Add Connect as a route to the existing
environment and inspect the route actually in use; retained SSH/direct routes
can provide fallback. If a newly linked environment is absent from a client that
was already open, refresh its view before trying to pair again.

Direct/Tailscale connections are alternatives for access. Background phone
push requires T3 Connect; the phone app is T3 Code, not the existing Codex/ChatGPT
conversation. Test a real question/approval from the phone before relying on it.
Select notification preferences deliberately. Keep external integrations for a
later qualified route.

Nightly V2 requires the **beta mobile app**; the stable store apps cannot connect
to this baseline. Use the beta links in T3's **Settings → General → Mobile app**
and prove the actual phone question/response route before relying on it.

[Connections](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/remote-access.md),
[mobile notifications](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/mobile-notifications.md).

## 5. Adopt selected skills

Clone a reviewed Factory tag on the host into a source directory, separate from
the application. From that checkout, run the staging helper for each needed bundle:

```sh
factory_stage_root="$(mktemp -d)" &&
  python3 scripts/stage.py foundation --output "$factory_stage_root/foundation" &&
  python3 scripts/stage.py agent-ops --output "$factory_stage_root/agent-ops" &&
  python3 scripts/stage.py adlc --output "$factory_stage_root/adlc"
```

Select scope deliberately:

| Bundle | Destination |
| --- | --- |
| Foundation | The setup/operator context; not needed by every implementation worker |
| Agent Ops | The selected project, activated in its Ops thread; use a separate project/profile/identity when its access needs differ |
| ADLC | The application project, or the native user/config scope described below |

For Codex, use the native project location `.agents/skills/`. Its documented user
location is `$HOME/.agents/skills`, shared across that OS user's projects; changing
`CODEX_HOME` alone does not isolate that skill location. A project skill is discoverable
by other threads in that project; discovery is not assignment of the lead role.
Use a separate project or OS identity when discovery or access must be exclusive.
See [native Codex discovery](https://learn.chatgpt.com/docs/build-skills).
For Claude, T3 reads the project's `.claude/skills/`
and the selected config directory's `skills/`; the config copy wins on a name clash.
Prefer project scope. Copy a reviewed complete skill folder from the stage into
the chosen location, including its references and license. Refuse an existing
same-name destination until you have reviewed the differences; do not blindly merge
or overwrite it. Keep separate installed copies only where the harness requires
them, derived from the same reviewed source. Do not maintain two edited originals.

For application worktrees, commit the selected project skills through that
application's normal review process so new worktrees contain them. If the project
should not track skills, use a deliberately chosen native user/config scope
with the sharing boundary described above; verify it in the selected harness. Never
assume an untracked copy in one checkout exists in another worktree. Verify native
discovery in an actual new worktree before delegating to it.

After reviewing the selected source and bundle, this example stages a fresh
copy and adopts it into the selected existing Codex project. Replace the example
path with the inspected workspace and run it from the Factory source checkout:

```sh
factory_lead_project="$HOME/Developer/your-project"
factory_lead_stage="$(mktemp -d)" &&
  python3 scripts/stage.py agent-ops --output "$factory_lead_stage/bundle" &&
  mkdir -p "$factory_lead_project/.agents/skills" &&
  test ! -e "$factory_lead_project/.agents/skills/factory-agent-ops" &&
  test ! -L "$factory_lead_project/.agents/skills/factory-agent-ops" &&
  cp -R "$factory_lead_stage/bundle/skills/factory-agent-ops" "$factory_lead_project/.agents/skills/"
```

Read the destination and compare it with the stage manifest. An existing folder
requires deliberate reconciliation; failure of the command is not successful adoption.
Before removing the temporary stage, retain its `manifest.json` in the persistent
private adoption record, alongside the version, date and installed destination.
The manifest is at the bundle root, not inside the copied skill directory.
Use `.claude/skills` instead for a project-scoped Claude installation. Load a new
native session and verify the correct skills appear and can read their references.
Ask it to assess a harmless example; copied files alone are not discovery proof.
Do not replace the application's AGENTS/CLAUDE instructions. Add a short route only
where the native harness requires one, preserving the canonical source.

In the Factory method repository itself, the Ops thread can read the reviewed
canonical skill files directly without copying them back into their own source
tree. Record this as explicit source loading, not native skill discovery. Configure
the persistent thread with [the operator workspace guide](workspace.md).

## 6. Prepare the repo and prove one delivery

Follow [repository preparation](github.md). Record the two decision points,
delegation, checks and delivery boundary using [the adoption outline](adoption.md).
Start with one bounded real task; prove implementation, independent review, a
review finding/fix and the authorized delivery. Then exercise client disconnect,
reconnect, permission refusal, unavailable provider and recovery without duplicates.

Add autonomous backlog scheduling or GitHub webhooks only after selecting the
supported native capability and qualifying its sender, authority, duplicates and
offline behavior. Native schedules are version-specific. A GitHub issue alone
does not wake the stable baseline or grant implementation access.

## Updates and host maintenance

Use the installed tools' native update paths. Record the selected channel,
responsible operator, interruption/recovery rules and last actual result in the
private installation record. Checking for updates, installing them and proving
compatibility are different actions.

| Component | Native route | Boundary |
| --- | --- | --- |
| Desktop/mobile clients | Official application updater or store/beta channel | Match the host's protocol; an updated client does not update the server |
| T3 background server | The named environment's Update server action or `t3 update <selected-version>` | Reconcile active turns and background commands first; it restarts the service |
| Claude native installation | Native background updates; `claude doctor` reports installation, channel and updater state | New version takes effect on the next process; custom/copied launchers may prevent adoption |
| Codex | Native installation/update support, or T3's detected provider update action | Inspect the actual installation; do not infer automatic installation merely from a version-check setting |
| Linux/Omarchy | Distribution's maintained update command and notifications | Package changes, migrations, prompts and reboot are system administration; a check notification is not an unattended update |
| Factory skills | Reviewed tag → staged diff → checks → deliberate adoption | Preserve local adaptations and verify discovery; do not auto-overwrite project instructions |

Native update checks may stay enabled. Automatically applying updates requires a
selected, supported and tested maintenance route: idle-work checks, bounded scope,
recovery, readback and an actionable failure signal. Do not add a Factory updater
or promise scheduling from a skill. An agent must not stop its own host mid-task
and assume it can inspect the result. Hand off disruptive maintenance to the
host's existing operator/maintenance facility and reconcile on return.

For Omarchy, use the installed version's supported updater; inspect its prompts
and restart behavior before unattended use. Encrypted boot may still require a
person to unlock the disk. A system snapshot need not cover the separate home
volume containing T3 history and provider profiles. Verify the actual coverage;
keep private native state recoverable under the owner's retention choice. Never
grant worker sudo, bypass package failures or weaken encryption to make updates
appear automatic.

After an update, check the service, connection route, selected CLI/authentication,
loaded skills and one harmless native turn. Repeat relevant permission and recovery
checks when those paths changed. Keep prior proof at its tested version. A saved
SSH fallback may reconnect successfully without automatically returning to Connect.

Sources: [T3 updating](https://github.com/pingdotgg/t3code/blob/ec80933ac8cd02fec5c97b342462ccc9567cdb1e/docs/user/updating.md),
[Claude installation and updates](https://code.claude.com/docs/en/setup),
[Codex installation](https://developers.openai.com/codex/cli/),
[Omarchy update process](https://github.com/omacom/omarchy/blob/c668141e9c42b13c80c9ca4ea108e11708c5e8a5/bin/omarchy-update).

## Removal and recovery

Stop new admissions and reconcile active work first. Keep native history and the
installed source manifest. Remove only the skill folders owned by this adoption;
restore a prior reviewed copy if required. Stop/uninstall the T3 service through
its native command only when it is the intended service. Preserve other projects,
provider accounts and private state. Update the installation record from readback.

To remove an obsolete T3 project in Nightly 2873: open **Settings**, change
**Applying settings for** from **All projects** to that project, then open the
**Project** section that appears in the settings menu. Under **Danger**, choose
**Remove project**. Confirm the exact project and chat count. This removes its
threads, including archived chats, from T3; the folder and Git repository remain
on disk. Archiving a thread does not remove its project. Reconcile active work
first and obtain the owner's explicit deletion decision. Use the native action,
not manual database edits. Backup retention/deletion is a separate scoped choice.
