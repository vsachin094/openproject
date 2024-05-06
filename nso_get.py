import requests
from requests.auth import HTTPBasicAuth

# Cisco NSO RESTCONF endpoint
restconf_url = "https://your_nso_server/restconf/data/tailf-ncs:devices/device={device_name}/live-status/ios-stats:exec/show/ip/ospf"

# Authentication credentials
username = "your_username"
password = "your_password"

# Device name where OSPF is running
device_name = "your_device_name"

# Command to retrieve OSPF process information
ospf_command = "show ip ospf | include Process ID"

# Prepare headers
headers = {
    "Accept": "application/yang-data+json",
}

# Prepare payload (command to send)
payload = {
    "input": {
        "tailf-ncs:args": ospf_command.split(" ")
    }
}

# Send RESTCONF request using GET method
response = requests.get(
    restconf_url.format(device_name=device_name),
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    params=payload,
    verify=False  # Set to True if using SSL/TLS
)

# Check if request was successful
if response.status_code == 200:
    # Parse response JSON
    response_json = response.json()
    # Extract OSPF process ID from response
    ospf_process_id = response_json["tailf-ncs:output"]["result"]
    print("OSPF Process ID:", ospf_process_id)
else:
    print("Error:", response.text)
