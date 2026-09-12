# Electronic Module and Network Map — Early L405

Use this as a routing lexicon, not as a substitute for the exact wiring diagram for a VIN/build. Module names, locations and fitment can vary by market and equipment. Search `data/modules.jsonl` for concise module records.

## Core power / sleep architecture
- **BMS — Battery Monitoring System:** measures battery current/voltage/state on the negative side.
- **GWM — Gateway Module:** bridges network domains and participates in energy-management decisions.
- **QCCM — Quiescent Current Control Module:** can cut non-essential infotainment/climate loads to protect the battery.
- **BJB/BJB2 — Battery Junction Boxes:** high-current distribution architecture.
- **CJB/RJB — Central/Rear Junction Boxes:** body/rear distribution and fuse architecture.
- **PSDB — Power Supply Distribution Box:** present on selected multi-battery architectures.

A battery/earth/network problem can therefore manifest as many downstream warnings without many failed modules.

Workshop battery architecture source: https://www.fullfatrr.com/gallery/albums/userpics/10672/L405%20battery%20mounting%20and%20cables.pdf

## GEN2.1 infotainment path
Early L405 infotainment is a distributed system rather than one “radio screen”:
- **TS / FCDIM / HLDF** — front touchscreen/display interface; terminology varies by document.
- **IAM** — Integrated Audio Module; early Bluetooth/audio-source control.
- **AAM** — Audio Amplifier Module on applicable Meridian systems.
- **ICP** — Integrated Control Panel.
- **NCM** — separate Navigation Control Module on certain market architectures.
- **IC** — Instrument Cluster, also consumes infotainment/navigation information.
- **RSE/TVCM** — rear-seat entertainment / TV modules where fitted.

These nodes can communicate over **MOST optical**, **MS-CAN comfort**, LVDS/CVBS video links and hardwired circuits depending on function. A failure in one MOST node can remove audio/AV functions while the touchscreen itself remains alive.

Sources:
- https://static.nhtsa.gov/odi/tsbs/2013/SB-10072794-0699.pdf
- https://static.nhtsa.gov/odi/tsbs/2014/SB-10102721-9340.pdf

## Body / access / assistance modules useful in scans
- **KVM** — Keyless Vehicle Module.
- **ATCM** — Automatic Temperature Control Module.
- **PSCM** — Power Steering Control Module.
- **EPBCM** — Electronic Park Brake Control Module.
- **ABS** — ABS/stability-control module; wheel-speed/vehicle-speed data is consumed widely.
- **SODL/SODR** — left/right side-object detection (blind-spot) modules.
- **RCM** — Restraints Control Module.
- **SPMA/SPMB** — seat-belt pretensioner modules named in early-L405 DTC guidance.
- **DSS** — optional Deployable Side Step controller.
- **TCU** — telematics on later/appropriately equipped L405s; do not assume MY13 fitment.

## Network interpretation rules
1. **One local code + one local symptom** can be a local component/circuit problem.
2. **Many missing-message codes** often indicate one absent node, common power/earth loss or a network fault.
3. **Many undervoltage codes** first require battery/charging/BMS/earth chronology.
4. A module that is **completely absent from the scan** is often more informative than a module containing secondary U-codes.
5. Use the **full DTC suffix** and module name; base code alone can mislead.
6. Do not swap control modules from donor cars as a casual test. Configuration/security dependencies can create additional faults.

## Launch-year connector trap
On 13MY L405, JLR SSM66157 documents poor terminal retention at upper-tailgate connector **C44-R2** on MS-CAN producing an extraordinary multi-system cluster: no-start, dead touchscreen, windows, seat operation, instrument display and climate/control-panel faults. It is the model example of a single network fault looking like many dead ECUs.

Source: https://static.nhtsa.gov/odi/tsbs/2013/SB-10097352-1020.pdf

## Read-only touchscreen diagnostics
On GEN2.1 L405 software that exposes the engineering screen, read-only diagnostics can include:
- battery voltage;
- vehicle/GPS speed and reverse/EPB state;
- ambient/light/dimming signals;
- hard-key and soft-key checks;
- MOST status/device information;
- video-input checks;
- self-test / colour-bar screens.

Use `references/service-modes-resets.md` for the guarded entry method. Do not use this menu to alter configuration, security or safety settings.
