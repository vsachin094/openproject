import re

def parse_router_interfaces(config_text):
    interfaces = {}
    interface_pattern = re.compile(r"interface (\S+)(?:\n\s+description (.*?))?\n\s+ip address ((?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4})")
    matches = interface_pattern.findall(config_text, re.DOTALL)

    for match in matches:
        interface_name = match[0]
        description = match[1]
        ip_address = match[2]
        subnet_mask = match[3]
        interfaces[interface_name] = {'description': description, 'ip_address': ip_address, 'subnet_mask': subnet_mask}

    return interfaces

# Function to read router configuration from file
def read_config_file(file_path):
    with open(file_path, 'r') as file:
        config_text = file.read()
    return config_text

# Example file path where router configuration is stored
config_file_path = 'router_config.txt'

# Read configuration from file
router_config = read_config_file(config_file_path)

# Parse interfaces
parsed_interfaces = parse_router_interfaces(router_config)

# Display parsed interfaces
for interface, config in parsed_interfaces.items():
    print(f"Interface: {interface}")
    if config['description']:
        print(f"Description: {config['description']}")
    print(f"IP Address: {config['ip_address']}")
    print(f"Subnet Mask: {config['subnet_mask']}")
    print()
