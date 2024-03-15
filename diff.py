def find_differences(list1, list2):
    onboarded_devices = {d['device_name'] for d in list2}
    devices_to_onboard = []
    devices_not_in_list1 = []

    for device in list1:
        device_name = device.get('name')
        if device_name:
            if device_name not in onboarded_devices:
                devices_to_onboard.append(device)
        else:
            devices_not_in_list1.append(device)

    return devices_to_onboard, devices_not_in_list1

# Example data
onboard_list = [{'device_name': 'iPhone'}, {'device_name': 'Samsung'}]
user_wants_list = [{'name': 'iPhone'}, {'name': 'OnePlus'}, {'name': 'Xiaomi'}]

to_onboard, not_in_list1 = find_differences(user_wants_list, onboard_list)
print("Devices to onboard:", to_onboard)
print("Devices not in list 1:", not_in_list1)