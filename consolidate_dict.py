consolidated_dict = {}

for inner_list in list_of_dicts:
    for d in inner_list:
        device_name = d['device_name']
        configs = d['config'].split(',')
        if device_name in consolidated_dict:
            consolidated_dict[device_name].append(configs)
        else:
            consolidated_dict[device_name] = [configs]

print(consolidated_dict)
