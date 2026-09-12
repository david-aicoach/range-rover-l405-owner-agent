# Electronics Architecture — Early L405

## Purpose
Use this file when symptoms cross multiple systems, when battery/charging faults appear, when infotainment goes partly or fully dead, or when a scan contains many communication codes.

## 1. Power distribution is a system, not a single battery
The early L405 uses an AGM primary battery with a **Battery Monitoring System (BMS)** on the negative side. The BMS reports battery current/voltage/state information into the vehicle energy-management strategy. Depending on derivative/build, additional battery hardware may exist; never assume a second battery solely from trim.

Power is distributed through battery/junction-box architecture including BJB/BJB2 and front/passenger/rear junction boxes. Fuse continuity therefore needs to be tested at the circuit under load; a fuse that looks intact does not prove the holder or feed is healthy.

### Critical owner/workshop rule
When charging a BMS-equipped vehicle, connect the charger so the BMS can **see the charging current**. JLR SSM66617 instructs use of a suitable chassis/engine earth rather than bypassing the BMS measurement path. A replacement battery also requires correct specification and BMS reset/recalibration as applicable.

Sources:
- https://static.nhtsa.gov/odi/tsbs/2013/SB-10097364-1020.pdf
- https://static.nhtsa.gov/odi/tsbs/2016/SB-10106244-9340.pdf

## 2. Gateway, CAN and LIN
The **Gateway Module (GWM)** bridges vehicle networks and participates in battery/energy management. Early L405 documentation shows high-speed and medium-speed CAN domains plus LIN sub-networks. A problem at a gateway, earth, common supply, or CAN splice/connector can make many healthy modules complain at once.

Diagnostic implication:
1. Read *all* modules before clearing anything.
2. Sort codes into voltage, missing-message, bus, and local-component groups.
3. Ask which faults appeared first and which modules are absent entirely.
4. Prove battery state and loaded earths.
5. Inspect water ingress and shared connectors before replacing several modules.

### Launch-year tailgate CAN trap
JLR SSM66157 is unusually important for 13MY: poor female-terminal retention in the upper-tailgate harness connector **C44-R2** on MS-CAN could create a broad cluster including no-start, dead touchscreen, inoperative windows, seats in inch mode, instrument-pack issues and a dead/unresponsive A/C panel. This is a canonical example of why symptom count does not equal failed-module count.

Source: https://static.nhtsa.gov/odi/tsbs/2013/SB-10097352-1020.pdf

## 3. Earths are shared failure points
JLR has published multiple L405 ground/earth bulletins. SSM72333 ties ground point **G3D375** to rear-door locking, driver-seat switchpack, false door-open status, remote locking, window switchpack and interior-light anomalies. Earlier SSM67737 covers loose earth-fixing concerns.

Rule: when several body features fail together, perform a **loaded voltage-drop/continuity test**, not just a visual glance at the lug.

Sources:
- https://static.nhtsa.gov/odi/tsbs/2015/SB-10105660-9340.pdf
- https://static.nhtsa.gov/odi/tsbs/2013/MC-10206608-9999.pdf

## 4. Quiescent Current Control / sleep strategy
The vehicle uses energy-management logic to prevent non-essential consumers from flattening the main battery. The QCCM/quiescent relay architecture can isolate infotainment/climate loads. A flat battery with one normal quiescent-current snapshot does **not** prove there is no intermittent wake-up drain.

High-value trap: **B1412-96** in the GWM is a manufacturer-documented false log on L405 13MY onward. JLR specifically says not to replace the GWM or Quiescent Relay Box for this DTC alone.

Source: https://static.nhtsa.gov/odi/tsbs/2015/MC-10105081-9340.pdf

## 5. GEN2.1 infotainment and MOST
Early L405 infotainment uses JLR GEN2.1 architecture with a **MOST optical ring** linking key entertainment modules. The touchscreen is not synonymous with the entire infotainment system.

Patterns:
- No sound + greyed Audio/Video button can be a MOST-node software conflict (SSM69158).
- Bluetooth problems should not automatically trigger touchscreen replacement; SSM72011 says the front touchscreen has no effect on Bluetooth connectivity.
- A software download interrupted by low voltage/diagnostic-link interruption can leave the touchscreen blank and uncommunicative; JLR provides a staged recovery route (SSM59197).

Sources:
- https://static.nhtsa.gov/odi/tsbs/2013/SB-10072794-0699.pdf
- https://static.nhtsa.gov/odi/tsbs/2014/SB-10102721-9340.pdf
- https://static.nhtsa.gov/odi/tsbs/2014/MC-10101681-9340.pdf

## 6. Camera network clues
On surround-camera cars, JLR SSM71977 documents paired behavior:
- rear-view camera ↔ front-right camera;
- right-mirror camera ↔ front-left camera.

In the documented pattern, the failed camera is **permanently blue** while its paired camera flickers three times at initial switch-on. Replace nothing until the permanent-blue camera and its power/wiring have been proved.

Source: https://static.nhtsa.gov/odi/tsbs/2014/SB-10102424-9340.pdf

## 7. Low voltage creates misleading code clouds
SSM62457 lists early-L405 DTCs that may be oversensitive or associated with low voltage when there is no corresponding customer concern. This does **not** mean “ignore all U-codes.” It means correlate every code with symptoms, module status, voltage history and recurrence.

Source: https://static.nhtsa.gov/odi/tsbs/2013/MC-10072243-0699.pdf

## 8. Practical fault-tree for a Christmas-tree dashboard
If ABS + suspension + gearbox + steering + parking brake warnings appear together:
1. Check actual battery resting/cranking voltage and charging behavior.
2. Check recent battery replacement/charging/BMS procedure.
3. Check primary/shared earths under load.
4. Look for water in loadspace/under carpet and corrosion at rear/floor connectors.
5. Review GWM/network DTCs and missing modules.
6. Only then move into subsystem-specific diagnosis.

Do not clear all codes before saving a complete report.
