# Range Rover L405 Owner, Electronics & Diagnostic Agent

A standalone, portable knowledge repository and ChatGPT Skill for the full-size **Range Rover L405**, centred on the **2013 Range Rover Vogue / Vogue SE** and launch-era **2013-2017** vehicles.

This project is deliberately independent of any private organisation, memory system or connector. It can be forked into another person's GitHub account and deployed as a portable ChatGPT Skill.

## Start here — Give this to your AI agent

```text
https://github.com/david-aicoach/range-rover-l405-owner-agent
```

That is the complete handoff. The agent should open the repository, read `AGENTS.md`, then follow [`BOOTSTRAP.md`](BOOTSTRAP.md) to fork, deploy and verify it. The human should not need to copy a longer setup prompt.

## Manual links

- **Repository:** https://github.com/david-aicoach/range-rover-l405-owner-agent
- **Bootstrap:** [BOOTSTRAP.md](BOOTSTRAP.md)
- **Portable Skill package in source:** [`dist/skill.zip`](dist/skill.zip)
- **Portable source Skill:** [`range-rover-l405-owner-agent/`](range-rover-l405-owner-agent/)

For a normal handoff, use only the repository URL above. The manual links are for operators who want to inspect or troubleshoot the deployment directly.

## What makes it different
This is not an owner's-handbook chatbot and not a generic “common problems” list. It combines five layers:

1. **Manufacturer owner truth** — JLR handbook/iGuide/TOPIx controls, features and maintenance procedures.
2. **Manufacturer technical intelligence** — JLR SSM/LTB/workshop failure patterns and diagnostic warnings.
3. **Government evidence** — recalls, investigations and government-hosted manufacturer bulletins.
4. **Hard-won L405 knowledge** — repeated specialist/community findings, explicitly labelled when not manufacturer-confirmed.
5. **Misdiagnosis prevention** — hidden clues, false positives and the highest-value proof test before parts are ordered.

The repository is **variant-aware**: L405 versus L494/L322, engine, model year, market, VIN/build boundary and optional equipment are kept separate.

## Current structured corpus
Validated locally:

- **58** issue / failure signatures
- **77** features, owner controls and hidden-function records
- **24** procedures, resets and service/engineering-mode sequences
- **15** DTC-specific records
- **27** electronic module / network records
- **201 total structured records**, plus long-form references

The counts are intentionally visible rather than implying “complete forever”; future evidence can be added without bloating the Skill entrypoint.

## Deep electronics coverage
The agent understands the early-L405 architecture, including:

- BMS / smart charging and battery-replacement implications
- GWM / CAN / LIN network reasoning
- QCCM sleep and quiescent-current protection
- BJB/BJB2/CJB/RJB power distribution
- GEN2.1 infotainment and MOST optical-ring logic
- touchscreen vs IAM/AAM/ICP responsibilities
- KVM/keyless software traps
- camera pairing diagnostics
- shared earth/ground failures
- fuse-holder continuity traps
- low-voltage “ghost” DTC patterns
- cross-system no-start / dead-module network signatures

## Features, tricks and hidden functions
Coverage includes, where equipped / market-applicable:

- single-point vs multi-point unlocking and Smart Key toggle
- keyless-start backup
- global opening/closing
- programmable powered-tailgate height and memory restoration
- Smart Key remote suspension raising/lowering
- access / locked-access / Crawl height behavior
- reverse mirror dip memory
- courtesy headlamp delay cancellation
- front-wiper service position
- one-touch window reset and sunroof recalibration
- camera gridline settings
- timed climate / auxiliary heater
- HomeLink
- Terrain Response / low range / HDC / towing guidance
- driver assistance: ACC, Forward Alert, BSM, closing-vehicle/reverse-traffic detection, Park Assist and cameras
- cabin-filter recirculation-flap access trick
- MY13 versus MY14+ service-reset boundary
- community oil-level forced-read shortcut, clearly labelled as non-official
- read-only GEN2.1 touchscreen engineering diagnostics, including the applicable **753** diagnostic screen path

## Hidden diagnostics without unsafe “hacking”
Where the installed GEN2.1 software supports it, the repository documents read-only engineering/diagnostic screens that can expose battery voltage, vehicle signals, hard/soft-key tests, MOST status, video inputs and display tests.

The repository does **not** provide immobilizer/key bypass, alarm defeat, theft-enabling OBD techniques, video-in-motion/safety-interlock defeat, SRS/ABS/steering disablement, emissions defeat, odometer/VIN manipulation or unsupported powertrain coding.

## High-value obscure examples
A few examples of the type of information captured:

- a 13MY upper-tailgate **C44-R2 MS-CAN terminal-retention fault** can produce no-start + dead touchscreen + windows + seat + instrument + climate faults from one connector;
- early rear fuse-holder poor continuity can group **air suspension + rear climate + rear seat + rear wiper** failures;
- JLR listed several early L405 DTCs that can be oversensitive/low-voltage artifacts when there is no matching symptom;
- **B1412-96** can be a false GWM log that may refuse to clear and should not trigger GWM/QCCM replacement by itself;
- a front number plate can physically obstruct the ACC radar and create **C1A67-97**;
- a surround-camera blue-screen pattern can identify the failed member of a paired camera set;
- Bluetooth faults are not automatically touchscreen faults;
- a touchscreen that dies during a failed software download follows a recovery diagnosis, not an immediate display replacement;
- a seemingly innocent cabin-filter change can break the powered recirculation flap if it is forced;
- JLR published a no-fault-found starter diagnostic because battery/relay/harness/earth faults were causing unnecessary starter replacement on applicable 14MY+ derivatives.

## Repository layout

```text
AGENTS.md
BOOTSTRAP.md
README.md
SOURCES.md
range-rover-l405-owner-agent/
  SKILL.md
  agents/openai.yaml
  data/
    issues.jsonl
    features.jsonl
    procedures.jsonl
    codes.jsonl
    modules.jsonl
  scripts/
    query_knowledge.py
    query_issues.py
    validate_catalog.py
  references/
    vehicle-profile.md
    powertrains.md
    handbook-map.md
    source-policy.md
    electronics-architecture.md
    module-map.md
    features-hidden-functions.md
    service-modes-resets.md
    dtc-quick-reference.md
    tips-life-hacks.md
    cooling-system.md
    common-systems.md
    recalls-tsbs.md
    rare-knowledge.md
    diagnostics-playbook.md
    ownership-baseline.md
    question-patterns.md
    deployment.md
```

## Example questions
- “Low coolant appeared for 30 seconds and disappeared. Rank the causes for my exact engine.”
- “ABS, suspension, gearbox and steering warnings all appeared together. What common upstream faults should I test first?”
- “What does B1412-96 mean on an L405 and should I replace the Gateway Module?”
- “Show me every hidden/less-obvious feature on a 2013 Vogue SE.”
- “What can I safely see in the GEN2.1 engineering menu?”
- “The touchscreen works but there is no sound and AV is greyed out.”
- “The key is only detected right next to the handle after the dealer programmed it.”
- “The rear seat, rear wiper, rear climate and air suspension failed together.”
- “Give me all life hacks and service sequences that actually apply to genuine MY13.”
- “What obscure things should I inspect before buying this car?”

## Local knowledge search

```bash
python3 range-rover-l405-owner-agent/scripts/query_knowledge.py coolant
python3 range-rover-l405-owner-agent/scripts/query_knowledge.py B1412-96
python3 range-rover-l405-owner-agent/scripts/query_knowledge.py GWM --kind module
python3 range-rover-l405-owner-agent/scripts/query_knowledge.py tailgate
python3 range-rover-l405-owner-agent/scripts/query_knowledge.py 753
python3 range-rover-l405-owner-agent/scripts/query_knowledge.py battery --category electrical
python3 range-rover-l405-owner-agent/scripts/validate_catalog.py
```

`query_issues.py` remains for fault-signature-only searches.

## Deployment
For normal deployment, give the receiving AI agent only the repository URL from the start section. The agent then follows [`BOOTSTRAP.md`](BOOTSTRAP.md).

For manual operation, install the contents of `range-rover-l405-owner-agent/` as a ChatGPT Skill, or use the repository as retrieval/context material for another agent runtime. See `range-rover-l405-owner-agent/references/deployment.md`.

The Skill is designed for progressive loading: `SKILL.md` remains a control plane while deep electronics, features, DTCs and rare-knowledge material stays in one-level references/data files.

## Copyright / source policy
The repository does **not** redistribute complete copyrighted JLR owner or workshop manuals. It stores derived guidance, structured facts, citations/source links and diagnostic synthesis. Obtain full current JLR technical documents through official JLR/TOPIx/iGuide access where required.
