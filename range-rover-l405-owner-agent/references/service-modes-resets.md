# Service Modes, Resets and Benign “Hidden” Sequences

Use only the procedure that matches model year/build and hardware. Save diagnostic data before resets.

## Owner-safe, manufacturer-documented

### Window reset after battery interruption
1. Close the window fully.
2. Release the switch.
3. Lift to close again and hold **1 second**.
4. Repeat each window.

Source: https://topix.landrover.jlrext.com/topix/service/procedure/431773/PDF/aeb331d6-c054-425d-b45b-eed11669adf4/en_GB

### Sunroof recalibration
1. Ignition on; roof closed.
2. Press/release front of roof switch to tilt.
3. Hold front of switch for about **20 seconds**.
4. When movement begins, keep holding through the complete open/close cycle.
5. Release when movement stops.

Source: same JLR maintenance procedure above.

### Front wiper service position
1. Ignition off.
2. Ignition on, then off again.
3. Immediately hold the wiper control in the single-wipe/lowest position while switching ignition on again.
4. Wipers move to service position.
5. After blade work, switch ignition off to return them to park.

Source: https://topix.landrover.jlrext.com/topix/service/procedure/537467/PDF/dd755348-10a1-4fe1-b872-e0af9096e2e8/en_GB

### Powered-tailgate opening-height memory
See `features-hidden-functions.md` or `data/procedures.jsonl`.

### Smart-key remote suspension
Hazards on, vehicle safely parked, EPB applied, doors closed:
- approach lamps + unlock = raise;
- approach lamps + tailgate unlock = lower.

Source: https://topix.landrover.jlrext.com/topix/service/procedure/225635/PDF/77e06762-7baa-4327-8262-3c16e06fbecc/en_GB

## Model-year trap: service reset
A common internet instruction says “bonnet open + driver door open + ignition on + brake and accelerator.” JLR SSM71851 identifies the **manual** procedure for **14MY onward**, with L405 start VIN **LG124982**. Community reproduction of the TOPIx SSM explicitly notes earlier vehicles still require diagnostics.

Therefore:
- **13MY:** do not promise the pedal reset; use a JLR-capable service function unless the exact VIN/software is independently verified.
- **14MY+ from the documented boundary:** manual reset is supported after the service is actually completed.

Source reproduction: https://www.landroverworld.org/threads/manual-service-reset-my14.25667/

## Community-known oil-level forced readout
Repeated L405 owner reports describe: bonnet unlatched/open, ignition on/engine off, navigate to Oil Level; when “unavailable” appears, press cruise-control **CANCEL twice**. Treat this as a convenience/debug trick, not an official MY13 handbook instruction.

Never use it to rationalize overfilling or to ignore P250B/P0196-type sensor/loom faults.

Source: https://www.fullfatrr.com/forum/post712222.html

## EPB service mode
A manual EPB service sequence is widely reported for L405, but brake work is safety-critical and year/software differences exist. Prefer a capable diagnostic tool and current workshop procedure. This skill may explain what service mode is, but should not tell an untrained owner to retract/force powered calipers.

## BMS reset / battery replacement
A new battery is not simply “fit and forget.” Use correct battery specification, ensure the BMS clamp and grounds are correctly installed, and perform the applicable BMS reset/recalibration with a compatible diagnostic tool.

Source: https://static.nhtsa.gov/odi/tsbs/2016/SB-10106244-9340.pdf

## CCF personalization safety
Car Configuration File editing can expose benign personalization on supported hardware, but it can also misconfigure safety/security/powertrain systems.

Before any benign CCF change:
1. export/screenshot the entire original configuration;
2. stabilize battery voltage;
3. change one item only;
4. cycle and full-scan;
5. retain rollback data.

Never provide or execute experimental coding for immobilizer/keys, alarm defeat, SRS, ABS/braking, steering, emissions, odometer/VIN alteration or unsupported powertrain functions.

## GEN2.1 touchscreen engineering / diagnostic screens — read-only use
Later L405 workshop documentation for the same GEN2.1 family describes an engineering screen exposed by holding the **Valet** soft key for roughly 20 seconds. A documented diagnostic-screen path on applicable software uses a long press near the top-centre, then top-left, followed by PIN **753**. Software revisions differ, so treat the entry path as **interface-dependent**, not a universal MY13 promise.

Useful read-only pages can include battery voltage, vehicle signals, hard-key/soft-key tests, MOST status, video inputs, self-test and colour bars. These screens can help prove that the touchscreen receives a signal or sees a button press without replacing parts.

**Guardrail:** if the menu is absent, stop. Do not guess alternate codes. Do not change car configuration, speed-lock, security, immobilizer, SRS, brakes, steering, emissions, VIN/odometer or unsupported hardware flags.

Source/reference: https://www.scribd.com/document/945146822/Range-Rover-L405-2014-19-Information-and-Entertainment-System

## Cabin-filter access trick: command the recirculation flap
On the L405 HVAC layout, the cabin/pollen filter is behind the lower glovebox and the powered recirculation flap can obstruct the tray. Command **recirculation** so the flap lifts out of the access path. Do not force the flap manually: broken flap pivots/actuators are reported after rough filter changes.

Community/service pattern: https://www.fullfatrr.com/forum/topic67654.html
