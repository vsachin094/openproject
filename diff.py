def find_differences(list1, list2):
    onboarded_devices = {d['device_name'] for d in list2}
    devices_to_onboard = []
    devices_already_onboarded = []
    devices_to_remove = []

    for device in list1:
        device_name = device.get('name')
        if device_name:
            if device_name in onboarded_devices:
                devices_already_onboarded.append(device)
            else:
                devices_to_onboard.append(device)
        else:
            devices_to_remove.append(device)

    return devices_to_onboard, devices_already_onboarded, devices_to_remove

# Example data
onboard_list = [{'device_name': 'iPhone'}, {'device_name': 'Samsung'}]
user_wants_list = [{'name': 'iPhone'}, {'name': 'OnePlus'}, {'name': 'Xiaomi'}]

to_onboard, already_onboarded, to_remove = find_differences(user_wants_list, onboard_list)
print("Devices need to onboard:", to_onboard)
print("Devices already onboarded:", already_onboarded)
print("Devices need to remove:", to_remove)