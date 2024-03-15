def find_key_differences(list1, list2):
    keys1 = set(d.get('name') for d in list1)
    keys2 = set(d.get('device_name') for d in list2)
    differences = list(keys1.symmetric_difference(keys2))
    return differences

list1 = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]
list2 = [{'device_name': 'John', 'model': 'X1'}, {'device_name': 'Bob', 'model': 'X2'}]

key_differences = find_key_differences(list1, list2)
print(key_differences)