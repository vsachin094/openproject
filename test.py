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

# Example configuration text from a router
router_config = """
interface GigabitEthernet0/0
 description This is the LAN interface
 ip address 192.168.1.1 255.255.255.0
!
interface GigabitEthernet0/1
 ipv6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64
!
interface GigabitEthernet0/2
 ip address 10.0.0.1/24
!
"""

parsed_interfaces = parse_router_interfaces(router_config)

for interface, config in parsed_interfaces.items():
    print(f"Interface: {interface}")
    if config['description']:
        print(f"Description: {config['description']}")
    print(f"IP Address: {config['ip_address']}")
    print(f"Subnet Mask: {config['subnet_mask']}")
    print()
