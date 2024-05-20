Textual Workflow:

Start
Fetch Devices:
Retrieve a list of devices from NMDB Group.
Create Empty Lists:
Initialize four empty lists:
devices_to_onboard_nso: Stores devices needing onboarding in NSO.
devices_to_onboard_cw: Stores devices needing onboarding in Cisco Crosswork (CW).
devices_to_remove_cw: Stores devices needing removal from CW.
devices_to_remove_nso: Stores devices needing removal from NSO.
Validate Onboarding (Loop):
For each device in the list from NMDB Group:
Check device presence in CW and NSO inventories.
If not found in CW, add to devices_to_onboard_cw.
If not found in NSO, add to devices_to_onboard_nso.
(Optional) Implement specific removal criteria here.
If the device meets removal criteria, add it to:
devices_to_remove_cw first.
devices_to_remove_nso next (if applicable).
Onboarding Flow:
Onboard NSO (if any devices need onboarding):
For each device in devices_to_onboard_nso:
Onboard the device to Cisco NSO.
Onboard CW (if any devices need onboarding):
For each device in devices_to_onboard_cw:
Onboard the device to Cisco Crosswork (CW).
Removal Flow:
Remove from CW (if any devices need removal):
For each device in devices_to_remove_cw:
Remove the device from Cisco Crosswork (CW).
Remove from NSO (if any devices need removal):
For each device in devices_to_remove_nso:
Remove the device from Cisco NSO.
End
Flowchart Symbols:

                  +--------------+
                  |      Start     |
                  +--------------+
                               |
                               V
                  +--------------+
                  | Fetch Devices | (NMDB Group)
                  +--------------+
                               |
                               V
                  +--------------+
                  | Create Lists  |
                  | devices_to_onboard_nso |
                  | devices_to_onboard_cw |
                  | devices_to_remove_cw |
                  | devices_to_remove_nso |
                  +--------------+
                               |
                               V
                   +--------------+           +--------------+
                   | Any device?   |           | All devices   |
                   | (Loop Start)  | (Yes)        | processed (No)|
                   +--------------+           +--------------+
                               |                   |
                               V                   V
                  +--------------+           +--------------+
                  | Check Device  |           | Device found |
                  | in CW/NSO      |           | in CW/NSO?   |
                  +--------------+           +--------------+
                               |                   |
                               V                   V
                       +--------------+           +--------------+
                       | Not found in |           | Not found in |
                       | CW? (Yes)      |           | NSO? (Yes)      |
                       +--------------+           +--------------+
                               |                   |
                               V                   V
                       +--------------+           +--------------+
                       | Add to        |           | Add to        |
                       | devices_to_onboard_cw |           | devices_to_onboard_nso |
                       +--------------+           +--------------+
                               |                   |
                               V                   V
                   +--------------+           +--------------+  (Optional)
                   | Removal       |           | Removal       |
                   | Criteria      |           | Criteria      |
                   +--------------+           +--------------+
                               |                   |
                               V                   V
                       +--------------+           +--------------+
                       | Meets Removal  |           | Not for       |
                       | Criteria?     |           | Removal       |
                       +--------------+           +--------------+
                               |                   |
                               V                   V
                       +--------------+           +--------------+
                       | Add to        |           |               |
                       | devices_to_remove_cw |           +--------------+
                       | (First)        |



tune

share


more_vert
