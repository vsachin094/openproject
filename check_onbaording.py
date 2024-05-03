def check_onboarding_status(list_of_data, list_of_dicts):
    # Initialize lists to store already onboarded and onboarding required items
    already_onboarded = []
    onboarding_required = []

    # Iterate over each item in the list of data
    for item in list_of_data:
        # Initialize a flag to indicate whether the item is found
        found = False
        
        # Iterate over each dictionary in the list of dicts
        for d in list_of_dicts:
            if item == d['id']:
                already_onboarded.append({'data': item, 'dict': d})
                found = True
                break  # Exit loop if the item is found
        
        # If the item is not found in any dictionary, add it to the onboarding required list
        if not found:
            onboarding_required.append(item)

    # Construct the result dictionary
    result_dict = {'already_onboarded': already_onboarded, 'onboarding_required': onboarding_required}
    return result_dict

# Sample data
list_of_data = [1, 2, 3, 4, 5]
list_of_dicts = [{'id': 1, 'name': 'John'},
                 {'id': 2, 'name': 'Alice'},
                 {'id': 3, 'name': 'Bob'}]

# Call the function
result = check_onboarding_status(list_of_data, list_of_dicts)
print(result)



def check_onboarding_status(onboarded_devices, new_devices):
    # Extract device names from dictionaries
    onboarded_device_names = [device['device_name'] for device in onboarded_devices]
    new_device_names = [device['device_name'] for device in new_devices]

    # Initialize lists to store already onboarded, devices needing onboarding, and devices needing removal
    already_onboarded = []
    need_to_onboard = []
    need_to_remove = []

    # Check if onboarded devices is not empty
    if onboarded_devices:
        # Check each new device
        for device in new_devices:
            if device['device_name'] in onboarded_device_names:
                already_onboarded.append(device)
            else:
                need_to_onboard.append(device)

        # Check each onboarded device
        for device in onboarded_devices:
            if device['device_name'] not in new_device_names:
                need_to_remove.append(device)
    else:
        # If onboarded devices list is empty, all new devices need onboarding
        need_to_onboard = new_devices

    # If new devices list is empty and onboarded devices list is not empty, all onboarded devices need removal
    if not new_devices and onboarded_devices:
        need_to_remove = onboarded_devices

    # Construct the result dictionary
    result_dict = {
        'already_onboarded': already_onboarded,
        'to_onboard': need_to_onboard,
        'to_remove': need_to_remove
    }
    return result_dict

# Sample data
onboarded_devices = [{"device_name": "Router1", "device_ip": "172.30.1.3", "device_os": "cisco-ios"},{"device_name": "Router3", "device_ip": "172.30.1.3", "device_os": "cisco-ios"},{"device_name": "Router2", "device_ip": "172.30.1.4", "device_os": "cisco-ios"}]
new_devices = [{"device_name": "Router2", "device_ip": "172.30.1.4", "device_os": "cisco-ios"}]

# Call the function
result = check_onboarding_status(onboarded_devices, new_devices)
print(result)



def check_onboarding_status(onboarded_devices, new_devices, cw_onboarded_devices, nso_onboarded_devices):
    # Extract device names from dictionaries
    onboarded_device_names = [device['device_name'] for device in onboarded_devices]
    new_device_names = [device['device_name'] for device in new_devices]
    cw_onboarded_names = [device for device in cw_onboarded_devices]
    nso_onboarded_names = [device for device in nso_onboarded_devices]

    # Initialize lists to store already onboarded, devices needing onboarding, and devices needing removal for each category
    already_onboarded_cw = []
    to_onboard_cw = []
    to_remove_cw = []
    already_onboarded_nso = []
    to_onboard_nso = []
    to_remove_nso = []

    # Check if onboarded devices is not empty for CW devices
    if cw_onboarded_devices:
        # Check each new device
        for device in new_devices:
            if device['device_name'] in cw_onboarded_names:
                already_onboarded_cw.append(device)
            else:
                to_onboard_cw.append(device)

        # Check each onboarded device
        for device in cw_onboarded_devices:
            if device not in new_device_names:
                to_remove_cw.append(device)

    # If new devices list is empty and onboarded devices list is not empty, all onboarded devices need removal for CW devices
    if not new_devices and cw_onboarded_devices:
        to_remove_cw = cw_onboarded_devices

    # Repeat the same process for NSO devices
    if nso_onboarded_devices:
        for device in new_devices:
            if device['device_name'] in nso_onboarded_names:
                already_onboarded_nso.append(device)
            else:
                to_onboard_nso.append(device)

        for device in nso_onboarded_devices:
            if device not in new_device_names:
                to_remove_nso.append(device)

    if not new_devices and nso_onboarded_devices:
        to_remove_nso = nso_onboarded_devices

    # Construct the result dictionaries for each category
    result_cw = {
        'already_onboarded_cw': already_onboarded_cw,
        'to_onboard_cw': to_onboard_cw,
        'to_remove_cw': to_remove_cw
    }

    result_nso = {
        'already_onboarded_nso': already_onboarded_nso,
        'to_onboard_nso': to_onboard_nso,
        'to_remove_nso': to_remove_nso
    }

    # Return results for CW and NSO
    return result_cw, result_nso



def check_onboarding_status(new_devices, cw_onboarded_devices, nso_onboarded_devices):
    # Extract device names
    new_device_names = [device['name'] for device in new_devices]
    cw_onboarded_names = cw_onboarded_devices
    nso_onboarded_names = [device['name'] for device in nso_onboarded_devices]

    # Initialize lists to store already onboarded, devices needing onboarding, and devices needing removal for each category
    already_onboarded_cw = []
    to_onboard_cw = []
    to_remove_cw = []
    already_onboarded_nso = []
    to_onboard_nso = []
    to_remove_nso = []

    # Check if onboarded devices is not empty for CW devices
    if cw_onboarded_devices:
        # Check each new device
        for device in new_devices:
            if device['name'] in cw_onboarded_names:
                already_onboarded_cw.append(device)
            else:
                to_onboard_cw.append(device)

        # Check for devices to remove
        for device in cw_onboarded_devices:
            if device not in new_device_names:
                to_remove_cw.append(device)

    # Check if onboarded devices is not empty for NSO devices
    if nso_onboarded_devices:
        # Check each new device
        for device in new_devices:
            if device['name'] in nso_onboarded_names:
                already_onboarded_nso.append(device)
            else:
                to_onboard_nso.append(device)

        # Check for devices to remove
        for device in nso_onboarded_devices:
            if device['name'] not in new_device_names:
                to_remove_nso.append(device)

    # Construct the result dictionaries for each category
    result_cw = {
        'already_onboarded_cw': already_onboarded_cw,
        'to_onboard_cw': to_onboard_cw,
        'to_remove_cw': to_remove_cw
    }

    result_nso = {
        'already_onboarded_nso': already_onboarded_nso,
        'to_onboard_nso': to_onboard_nso,
        'to_remove_nso': to_remove_nso
    }

    # Return results for CW and NSO
    return result_cw, result_nso


