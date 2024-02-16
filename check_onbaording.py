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
