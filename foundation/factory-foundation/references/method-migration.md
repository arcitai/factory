# Migrate an optional method package on a host

Revision: 0.1.21 · Updated: 2026-10-23

Factory depends on no personal-method package. Some owners also use one, such as
**The Onlinesourdough Method (OSM)**, formerly AIOS. When that package changes its
identity, the hosts and consumers that call it must move without breaking working
calls or the owner's context. This guide covers that host and consumer side. The
package's own repository owns its source, release and distribution.

## OSM naming, as of 2026-10-23

- The public name is The Onlinesourdough Method (OSM). "Context Architecture" is a
  descriptive term, not a product. The owner's instruction page, **AI Operating
  Model**, keeps its name, link, selected home and IDs.
- The target plugin identity is `osm` with skills prefixed `osm-*`. The target
  repository, `onlinesourdough/OSM-plugin`, is not yet current; the marketplace
  publisher `online-sourdough` stays.
- The order is fixed: a qualified native package candidate
  ([OSM #62](https://github.com/onlinesourdough/AIOS-plugin/issues/62)), then host
  and consumer preparation ([Factory #93](https://github.com/arcitai/factory/issues/93)),
  then the verified distribution and repository cutover
  ([OSM #77](https://github.com/onlinesourdough/AIOS-plugin/issues/77)). The parent
  ledger is [OSM #76](https://github.com/onlinesourdough/AIOS-plugin/issues/76).

Until that candidate is qualified, the current AIOS invocation names, repository
URLs and marketplace selectors stay current and working. Do not rewrite them into
future names that do not resolve yet.

## Classify before changing

Sort every occurrence into one class:

| Class | Examples | Rule |
| --- | --- | --- |
| Current branding | Display names and current descriptions in guidance | Update to the current name |
| Executable identifier | Invocation and skill names, plugin IDs, marketplace selectors, install URLs, MCP identifiers | Change only together with the qualified package and its real callers |
| Compatibility or storage | Managed markers such as `AIOS:BEGIN`, source keys, context page and database IDs | Keep, and document why |
| History | Release notes, past evidence, provenance and license attribution, original source URLs, old comments | Leave as written |

Identify the installed **generation** from its version, provenance and source.
Never infer it from a prefix, namespace or display label: legacy OSM 0.1.x already
used `osm-*`, `OSM.md`, `OSM_FORMAT` and `OSM:BEGIN`, current AIOS uses other
names, and the new OSM reuses `osm-*`. A renamed label is not a migrated package,
and a legacy OSM block is not the new identity or something to delete.

## Record the baseline

Keep this per host, account and harness in the existing
[adoption record](adoption.md), privately:

- the installed generation, version, source revision or manifest, and namespace
  and invocation names;
- the manual and scheduled standing calls that invoke it, such as recurring
  prompts, automations and skill chains;
- the context home and its IDs, source keys, user-authored rules and the AI
  Operating Model link. Hosts can differ: one harness may route to a file home
  while another routes to Notion. Preserve each one; do not silently replace it;
- the permissions and connectors it relies on;
- the current, scoped recovery route that restores today's working state.

An unknown entry stays a named gap. A consumer you cannot reach, such as a project
outside this host's access, stays a required row marked unknown, not "not
applicable".

## Gates before cutover

All of these must hold for the host in question:

1. **The exact candidate** from the package's owner: an immutable source revision,
   package and manifest identity, a compatibility map from old to new identifiers,
   the supported native install, upgrade and recovery route for this harness, and
   the owner's qualification proof (clean install, upgrade keeping the existing
   home, mixed installations, fresh-session discovery and invocation).
2. Owner authority for this host, account and scope.
3. The recorded baseline and its recovery route, freshly verified on the same host
   before any effect (step 2 below).
4. An agreed idle checkpoint for the affected work, and its holder.

A missing gate is a blocked field naming its holder. Do not invent install
commands, URLs or controls to fill it.

## Cut over one host

1. Inventory and classify, as above.
2. Privately preserve the current program, registration and context-instruction
   files in scope on the same host, with their full modes. Then check the copy
   against the current files: the same file set, bytes, sizes and full modes, and
   internal links where they matter. Record what was preserved and the current
   state it came from. Do not copy authentication or profile roots.
3. Select the verified candidate and the compatibility route for this host's
   generation.
4. Reach the idle checkpoint with the affected work's holders. Do not end
   unrelated running work to rename it.
5. Apply only through the harness's supported native help, plugin or upgrade
   controls that the candidate names.
6. Verify that the installed payload matches the candidate's manifest, the native
   registration shows the new identity, and unrelated configuration is unchanged.
7. In a fresh target session, verify discovery, display, invocation and one real
   use that reaches the same AI Operating Model, home and IDs. Check that the
   standing calls resolve.
8. Only then retire the old active family through supported controls, leaving one
   active family.

Record one outcome per host: **changed and verified**, **already current**,
**blocked** (with the dependency and holder), **unavailable** (not migrated), or
**mixed, stopped**. Stop on an ambiguous generation, an unsupported native step, a
failed check or an uncertain effect. Never replay blindly, edit caches by hand or
change file modes to force a result.

## Roll back

Bind rollback to both the baseline's recorded immutable source or package
identity and the harness's supported native selector or route for exactly that
identity. A reused selector alone can resolve to something else. Keep the current
private state: context, homes, IDs and user rules. If an effect was partial or
uncertain, stop and reconcile the actual state before any rollback or retry. Then
verify in a fresh session that the old calls work again. Rolling back deletes no
context and no legacy blocks, and uses no invented command, cache edit, mode
change or grant.

Factory #93 stays open until each applicable host and consumer has its own
recorded outcome.
