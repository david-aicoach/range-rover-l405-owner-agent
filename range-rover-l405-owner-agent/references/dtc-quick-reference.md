# DTC Quick Reference and Scan Interpretation

Use `data/codes.jsonl` for searchable code-specific entries.

## Never drop the suffix
On JLR scans, the suffix after the base DTC (for example **-96**, **-62**, **-87**, **-97**) materially narrows the failure type. Search and report the **full code**, not only B1412 or C1A67.

## Prefix families
- **P** — powertrain
- **B** — body
- **C** — chassis
- **U** — network/communication

This prefix is only a routing hint. A U-code in five modules often points upstream to power/network loss rather than five failed modules.

## Manufacturer-documented early-L405 ghost/noise codes
JLR SSM62457 lists several codes that may appear on 13MY L405 with no corresponding concern, often around low battery voltage. The list includes examples such as:
- U3003-62 in ATCM / blind-spot modules;
- B1304-16 in PSCM;
- U3000-54 in EPBCM;
- U3000-04 and U0300-46 in GWM;
- U0001-81 in seat-belt pretensioner modules.

**Important:** this is not permission to ignore them when a matching live symptom exists.

Source: https://static.nhtsa.gov/odi/tsbs/2013/MC-10072243-0699.pdf

## B1412-96 — one of the best L405 “do nothing yet” codes
JLR SSM72286 says B1412-96 can be falsely logged in the GWM due to software, may refuse to clear and does not affect vehicle performance in that bulletin context. It specifically says **do not replace the GWM or Quiescent Relay Box for this DTC alone**.

Source: https://static.nhtsa.gov/odi/tsbs/2015/MC-10105081-9340.pdf

## C1A67-97 — radar blocked
Before radar replacement/alignment, inspect the front number plate. JLR documents incorrect-size or multiple/stacked plates obstructing the forward radar.

Source: https://static.nhtsa.gov/odi/tsbs/2014/SB-10102441-9340.pdf

## Dynamic Response code cluster
C1119-09, C1B11-62, C1046-91 and C104A-94 appear in JLR SSM64917’s trapped-air/bleed context. If the problem followed hydraulic work, bleed state is a higher-value hypothesis than immediate module/valve replacement.

Source: https://static.nhtsa.gov/odi/tsbs/2013/MC-10206492-9999.pdf

## Scan-reading workflow
1. Save all DTCs with module name, full suffix and status.
2. Save freeze-frame/environmental data and battery voltage.
3. Mark modules that cannot be contacted at all.
4. Separate **primary/local** codes from **secondary/missing-message** codes.
5. Correct known low voltage/earth/network problems first.
6. Clear only as a controlled test.
7. Reproduce the symptom and rescan.

## “Missing message” versus “bus off”
Treat these differently. A missing-message code can arise because one expected module/message disappeared. A bus-off condition suggests a wider network-level fault. Do not treat every communication DTC as equivalent.

## Security boundary
This reference decodes diagnostic information. It does not provide key programming, immobilizer bypass, alarm defeat, OBD security circumvention, odometer/VIN modification, or anti-theft coding instructions.
