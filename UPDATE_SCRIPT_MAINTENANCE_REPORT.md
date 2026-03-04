## Update Script Maintenance Report

Date: 2026-03-04

- Root cause: repository had no executable updater automation even though stable source CSV URLs are documented.
- Fixes made: added `scripts/update.py` to sync `athletes.csv` and `events.csv` from upstream raw GitHub URLs with header-shape guardrails.
- Automation: added first scheduled/manual workflow with explicit `permissions: contents: write` and commit-if-changed behavior.
- Validation: ran updater locally and verified output schema remained consistent with existing files.
