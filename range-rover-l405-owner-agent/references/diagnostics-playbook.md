# L405 diagnostic playbook

## Universal intake
Capture:
- exact dashboard text/photo,
- when it happened (cold start, hot idle, highway, braking, turning, rain, after parking),
- whether it self-cleared after ignition cycle,
- engine/fuel/market,
- mileage,
- recent battery/jump-start/repair history,
- recent coolant/oil/fluid top-ups,
- whether any system behavior changed,
- full-vehicle scan before codes are cleared when possible.

## Pattern: intermittent warning that clears itself
1. Preserve exact message and timestamp.
2. Check the physical system if owner-accessible (e.g., cold coolant level, tyre pressure).
3. Look for a common upstream cause: low voltage, earth, network, temperature/pressure threshold.
4. Scan all modules, not only the named one.
5. Group DTCs by timestamp/voltage rather than counting them as separate failures.

## Pattern: low coolant
1. Engine fully cold: verify actual expansion-tank level.
2. If low, treat as real coolant loss until disproved.
3. Inspect dried residue around pump, tank, caps, hose joints and engine valley/pipe regions appropriate to engine.
4. Pressure-test cold; if no external leak, consider cap behavior, hot-only leaks, heater circuit and internal loss.
5. Only rank level sensor/tank sensing highly when measured level is repeatedly correct and stable.
6. Stop driving if temperature rises, steam appears, cabin heater abruptly goes cold during overheating, or coolant loss is substantial.

## Pattern: many electrical warnings
1. Battery conductance/state-of-charge test.
2. Charging output under load.
3. Main battery terminals and primary earths including known launch-era earth concerns.
4. Full module scan with voltage/timestamp context.
5. Water ingress inspection if faults persist or carpet/load area is damp.
6. Only then chase individual modules.

## Pattern: air suspension low/slow/fault
1. Observe parked height corner-by-corner over time.
2. Note compressor run duration/frequency.
3. Scan EAS live data and DTCs.
4. Leak-test air springs/lines/valve blocks/reservoir circuit.
5. Verify height sensors/calibration.
6. Replace compressor only after checking whether a leak caused overwork.

## Pattern: rattle from 5.0 SC front engine
Rank separately:
- supercharger isolator/backlash,
- accessory drive/tensioner/idler,
- water pump/bearing,
- timing drive,
- other engine mechanical sources.
A JLR-trained workshop can isolate the supercharger drive as described in applicable bulletin before condemning the timing system.

## Pattern: wet carpet / intermittent electronics
1. Lift/check underneath carpet, not just surface pile.
2. Water-test by zones.
3. Inspect roof drains/outlets, HVAC condensate drain connection, windscreen/cowl, door/tailgate seals and load-space paths as applicable.
4. Inspect connectors/modules in affected low areas for corrosion.
5. Dry completely before concluding an electrical module is defective.

## Pattern: driveline shudder
1. Confirm tyre sizes/pressures/tread depth across all four wheels.
2. Determine speed/load/turn dependence.
3. Inspect mounts/shafts/CVs/differentials.
4. Review transfer-case adaptation/software/fluid history with JLR-capable diagnostics.
5. Do not use a transfer-case replacement as the first diagnostic step.
