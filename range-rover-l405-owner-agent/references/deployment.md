# Portable deployment guide

## Give this to your AI agent

```text
Install this as a skill, read BOOTSTRAP.md  here's the link: https://github.com/david-aicoach/range-rover-l405-owner-agent
```

That is the complete human handoff. The receiving agent should install the repository as a Skill, read the root `BOOTSTRAP.md`, then follow the bootstrap to fork the repository into the target owner's GitHub account/organisation, deploy the packaged Skill from that fork, and verify the deployment.

Do not make the human reconstruct the setup steps manually. The repository owns the bootstrap instructions so future bootstrap improvements remain durable at the same link.

## ChatGPT Skill deployment
Use `dist/skill.zip` from the target owner's fork as the portable ChatGPT Skill package. No private connector is required.

If the ChatGPT environment supports direct Skill upload/install, install it. If the platform requires the human to upload or enable the Skill, ask only for that unavoidable action and continue verification afterwards.

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
Keep the Skill self-contained and avoid TBHRC-specific paths, secrets, connectors or private assumptions. The target owner's GitHub fork is the editable deployment copy. The uploaded ChatGPT Skill is a runtime copy, not the source of truth.
