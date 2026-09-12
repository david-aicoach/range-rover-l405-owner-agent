# Portable deployment guide

## ChatGPT Skill deployment
Upload the packaged `skill.zip` to the target ChatGPT Skill environment. No private connector is required.

Recommended capabilities:
- web browsing for current JLR/TOPIx lookup;
- image understanding for dashboard/engine-bay photos;
- optional file upload for user-provided service invoices, scan reports or manuals.

## Other agent runtimes
Treat `SKILL.md` as the system workflow and mount `references/` as retrieval documents. Preserve the source hierarchy and safety rules.

A minimal runtime needs:
1. LLM with tool/function calling or retrieval support;
2. optional web/browser tool;
3. retrieval over markdown references;
4. conversation state for vehicle identity (VIN/engine/market once supplied).

## Suggested persistent vehicle profile
Store only with the vehicle owner's permission:
- model year;
- exact derivative;
- engine/fuel type;
- market;
- VIN if they choose to provide it;
- wheel/tyre size;
- recent maintenance and known faults.

Do not store passwords, payment data, or unrelated personal data.

## Repo portability
Keep the Skill self-contained and avoid TBHRC-specific paths, secrets, connectors or private assumptions. The source repository may use GitHub for versioning, but runtime operation must not depend on GitHub.
