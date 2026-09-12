# Bootstrap — Range Rover L405 Owner Agent

This bootstrap is **agent-led**. The human should only need to give a capable AI agent the public repository link. The agent should handle the GitHub fork, deployment preparation and verification, asking the human only for an unavoidable sign-in/authorisation or ChatGPT Skill-upload action.

**Source repository:** https://github.com/david-aicoach/range-rover-l405-owner-agent

## 0. Start from the link

When you are given the repository URL, open the repository and read the root `AGENTS.md` first. Do not ask the user to copy setup instructions from the README.

## 1. Establish the target GitHub identity

Use the authorised GitHub connection already available to you where possible. Resolve the active GitHub identity and target account/organisation before mutation.

Default outcome for another owner: **fork this public repository into that owner's GitHub account or organisation** so they have their own portable copy and can receive/update the upstream source cleanly.

Do not deploy into `tbhrc` or another unrelated organisation unless the user explicitly asks for that target.

If GitHub authorisation or the target owner genuinely cannot be resolved, ask only for that unavoidable action, then continue.

## 2. Fork, do not reconstruct

Prefer a native GitHub fork of:

`https://github.com/david-aicoach/range-rover-l405-owner-agent`

Preserve the repository structure, history and upstream relationship. Do not rebuild the corpus from chat history and do not copy files manually into a new empty repository when a fork is available.

After the fork exists, work from the fork as the user's deployment copy. Keep the original repository as upstream reference unless the user explicitly wants a different ownership model.

## 3. Verify the portable package

Confirm the fork contains at least:

- `AGENTS.md`
- `BOOTSTRAP.md`
- `README.md`
- `SOURCES.md`
- `range-rover-l405-owner-agent/SKILL.md`
- `range-rover-l405-owner-agent/agents/openai.yaml`
- `range-rover-l405-owner-agent/references/`
- `range-rover-l405-owner-agent/data/`
- `range-rover-l405-owner-agent/scripts/`
- `dist/skill.zip`

Run the bundled catalogue validator when execution is available:

```bash
python3 range-rover-l405-owner-agent/scripts/validate_catalog.py
```

Do not silently continue if the Skill source, structured corpus or package is missing/corrupt.

## 4. Deploy to ChatGPT

Use the fork's `dist/skill.zip` as the portable ChatGPT Skill package.

If the current ChatGPT environment supports direct Skill upload/install, install it. If the platform requires the human to complete the upload or enable the Skill, present that as the **single unavoidable action** and continue verification immediately afterwards.

The editable canon is the GitHub fork. The uploaded ChatGPT Skill is a runtime copy, not the source of truth.

## 5. Other agent runtimes

If the target is not ChatGPT, treat `range-rover-l405-owner-agent/SKILL.md` as the operating entrypoint and expose its one-level `references/` and structured `data/` to the runtime. Preserve the evidence hierarchy, variant boundaries and safety rules.

Do not introduce private TBHRC connectors, memory systems or organisational dependencies merely to make the agent work.

## 6. Optional owner profile

Only when useful and with the vehicle owner's permission, persist the minimum vehicle identity that improves answers:

- model year;
- exact derivative;
- engine/fuel type;
- market;
- VIN if the owner chooses to provide it;
- wheel/tyre size;
- relevant maintenance history and known faults.

Do not make profile completion a deployment gate.

## 7. Prove the deployment

Run representative checks against the deployed agent:

1. one owner/how-to question;
2. one warning/fault question;
3. one obscure or misdiagnosis-trap question;
4. one model-year/engine/market applicability question.

The agent should use bundled evidence first, distinguish official from specialist/community evidence, and avoid inventing variant-specific facts.

## 8. Completion

Return only the useful outcome:

- fork/repository ready;
- Skill deployed or the one remaining human upload action;
- validation result;
- any real residual gap.

Do not teach the user GitHub mechanics unless they ask.
