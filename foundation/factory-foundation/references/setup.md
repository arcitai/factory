# Set up the host and operator client

This reference setup uses T3 Code on a Linux execution host, with a Mac and
optionally a phone as clients. The host can be a laptop, workstation or VPS.
The method itself also works without T3 after qualifying
the chosen harness's discovery and operation.

Source baseline checked 2026-10-07: stable T3 **0.0.45**. Newer V2 delegation and
automation are an additional qualification, not a prerequisite for the first
manually coordinated task. Keep the chosen client/server/provider versions in
the installation record. See [upstream installation](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/install.md).

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

Use one persistent Ops thread in the owner's existing project when it has the
right context and access. A separate lead project is optional, not a requirement.
Activate the lead role in that thread; preserve the project's shared instructions.
Workers receive the target project's context and skills. Separate provider profiles,
T3 environments/OS identities or VMs are appropriate when
the lead, workers or projects require different filesystem/network trust.
Do not copy a personal AIOS installation or personal provider home into this setup.

Preserve any old Factory runtime and private history while qualifying this setup.
Avoid pointing two active agent writers at the same checkout. Do not run native
services as root. Keep the host powered, awake and network-accessible.

## 2. Install and authenticate on the execution host

Install Git, the GitHub CLI and the native provider CLIs using their supported
instructions. Inspect versions and authenticate the intended execution account.
Repository and Project operations need appropriate GitHub access; deployment
credentials are a separate decision.

Install a selected T3 release using its official installer. For the documented
baseline, download and inspect the script before executing it:

```sh
factory_install_dir="$(mktemp -d)" &&
  curl -fsSLo "$factory_install_dir/install.sh" https://t3.codes/install.sh &&
  less "$factory_install_dir/install.sh"
```

After reviewing that downloaded script, execute the same file:

```sh
T3CODE_VERSION=0.0.45 sh "${factory_install_dir:?Use the directory from the successful download and review above}/install.sh"
```

Use the installer-reported binary path if `~/.local/bin` is not on `PATH`.
Check `t3 --version`, `codex --version`, `claude --version`, `git --version`
and `gh --version` as the account that will run the service.
Stop and reconcile if the reported T3 version differs from the selected version.

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

References: [Codex profiles](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/providers-codex.md),
[Claude profiles and skills](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/providers-claude.md),
[usage](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/usage.md).

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
Pin versions for a qualification run. The documented update path is `t3 update`
with a selected version; restarting interrupts active turns. Back up native state
with the service stopped before a major migration. Preserve the prior installation
and selected userdata; a binary downgrade alone may not undo a database migration.
[Service behavior](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/background-service.md),
[V2 migration and backup](https://github.com/pingdotgg/t3code/blob/fd1c3386c4d60f3477ab3f13c87537848de099f5/docs/user/thread-migration.md).

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

Pairing links are credentials. Transfer them directly into the intended client,
then verify readback and remove temporary copies. If typing a full link fails,
use the dialog's separate Host and Pairing code fields. Reconcile an uncertain
pairing before creating another. Do not import a personal browser profile to solve
an execution-host login, or infer GitHub CLI access from a browser session.

T3 Connect links environments through its native account flow, including headless
hosts. Direct/Tailscale connections are alternatives for access. Background phone
push requires T3 Connect; the phone app is T3 Code, not the existing Codex/ChatGPT
conversation. Test a real question/approval from the phone before relying on it.
Select notification preferences deliberately. Keep external integrations for a
later qualified route.

[Connections](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/remote-access.md),
[mobile notifications](https://github.com/pingdotgg/t3code/blob/v0.0.45/docs/user/mobile-notifications.md).

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

## Removal and recovery

Stop new admissions and reconcile active work first. Keep native history and the
installed source manifest. Remove only the skill folders owned by this adoption;
restore a prior reviewed copy if required. Stop/uninstall the T3 service through
its native command only when it is the intended service. Preserve other projects,
provider accounts and private state. Update the installation record from readback.
