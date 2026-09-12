# Features, Hidden Functions and Owner Controls

## Rule: option-aware, not trim-assumed
The 2013 handbook describes a broad platform feature set. A Vogue SE may not have every item, and UK/Europe/GCC/North America configurations differ. Say **documented**, **if equipped**, or **market dependent** rather than claiming a feature is standard.

Use `data/features.jsonl` for machine-searchable coverage.

## High-value owner functions people often miss

### Smart-key unlock mode toggle
The 13MY Quick Guide documents switching between single-point and multi-point entry by holding **lock + unlock together for about 3 seconds** while the vehicle is unlocked; hazard lamps confirm the change.

### Keyless-start backup
A valid Smart Key that is not being detected can be presented at the marked steering-column backup point and then used with the normal brake + START procedure. RF interference can come from phones/laptops, metal containers or loose coins near the key.

### Global opening / closing
13MY owner literature includes global opening and, on relevant market/configuration, global closing. Use it only with apertures visibly clear.

### Programmable powered-tailgate height
Set a lower maximum opening height for garages: stop the tailgate where wanted, keep stationary, hold the close switch 10 seconds, then close/reopen to verify. The same JLR procedure explains how to restore position memory after low voltage or repeated obstruction events.

### Remote suspension from the Smart Key
With the vehicle safely parked, EPB applied, doors closed and hazards on:
- **raise:** approach-lamps + unlock;
- **lower:** approach-lamps + tailgate-unlock.
This is useful for hitching/loading. Keep people and obstacles clear.

### Locked access / Crawl height
Use locked access height for slow manoeuvring under height restrictions. The system automatically cancels at higher speed. This is more useful than repeatedly lowering the car while entering a low garage.

### Reverse mirror dip can be personalized
On memory-seat vehicles, enable reverse dip, select R, adjust mirrors to the desired curb view, then select N to store.

### Courtesy-light delay shortcut
The headlamp courtesy delay can be configured up to 240 seconds in vehicle setup. Press the Smart Key headlamp/approach button to cancel the delay early.

### Wiper service position
Do not pull the blades upward from the normal parked position. Use the ignition + single-wipe service sequence in `service-modes-resets.md`.

### Tailgate / rear wiper logic
The rear wiper can activate automatically in reverse when the front wipers are active, but is inhibited when the tailgate is open.

### Camera gridlines are user-selectable
JLR issued SSM68338 because missing guidance lines were being treated as faults when the feature could simply be switched off.

### Valet mode
The touchscreen can set a 4-digit valet PIN to restrict selected vehicle/loadspace functions. If forgotten, use authorized JLR recovery; this skill never provides a bypass.

### Timed climate / auxiliary heater
Some engine/market specifications support programmed or remote pre-conditioning. It may suspend for low battery/fuel and is not present on every 2013 car.

### HomeLink / garage transceiver
Where fitted, the rear-view-mirror transceiver can learn compatible garage doors, gates and other RF devices. Rolling-code receivers usually need the receiver’s learning procedure as well.

## Driver-assistance features documented for the platform
Depending on equipment/build:
- Adaptive Cruise Control and Forward Alert
- advanced brake assistance
- Blind Spot Monitoring / Closing Vehicle Detection
- Reverse Traffic Detection
- parking sensors / Park Assist
- rear and surround cameras
- trailer guidance
- High Beam Assist / AFS

### Hidden diagnostic clue: ACC “blocked” can be the number plate
JLR SSM71999 documents **C1A67-97 / Radar Sensor Blocked** caused by an incorrect-size or stacked front number plate physically obstructing the radar below the plate plinth. Inspect that before paying for a radar module.

## Off-road and towing capability
2013 owner documentation covers:
- General / Grass-Gravel-Snow / Mud-Ruts / Sand / Rock Crawl Terrain Response programs;
- Dynamic program on applicable derivatives;
- HDC / Gradient Release Control;
- access, off-road, extended and locked-access heights;
- low range where fitted;
- Trailer Stability Assist and camera/trailer guidance where fitted.

## Infotainment reality check
Early L405 is a GEN2.1/MOST-era car. Later L405 feature guides can contain InControl Touch Pro behavior that does **not** apply to MY13. Keep MY13-specific instructions separate.

Primary source index:
- 2013 handbook: https://topix.landrover.jlrext.com/topix/service/document/194724
- 13MY alternate/ROW handbook: https://topix.landrover.jlrext.com/topix/service/document/194723
- 13MY Quick Guide: https://topix.landrover.jlrext.com/topix/service/document/453347
