import re

def get_interface_info(interface_config_output):
    interfaces = []
    # Regular expression pattern to match interface details
    interface_pattern = r"interface (\S+)\s*([\s\S]*?)(?=^interface|\Z)"
    # Search for all interface patterns in the configuration output
    matches = re.finditer(interface_pattern, interface_config_output, re.MULTILINE)
    for match in matches:
        interface_name = match.group(1)
        interface_config = match.group(2)
        # Extract IPv4 addresses
        ipv4_matches = re.finditer(r"ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?:/(\d{1,2}))?", interface_config)
        # Extract IPv6 addresses
        ipv6_matches = re.finditer(r"ipv6 address ([\w:]+)/(\d+)", interface_config)
        # Extract description
        description_match = re.search(r"description (.*)", interface_config)
        for ipv4_match in ipv4_matches:
            interface_info = {'interface_name': interface_name, 'ip_address': ipv4_match.group(1)}
            if ipv4_match.group(2):
                interface_info['mask_prefix'] = int(ipv4_match.group(2))
            if description_match:
                interface_info['description'] = description_match.group(1).strip()
            interfaces.append(interface_info)
        for ipv6_match in ipv6_matches:
            interface_info = {'interface_name': interface_name, 'ip_address': ipv6_match.group(1), 'mask_prefix': int(ipv6_match.group(2))}
            if description_match:
                interface_info['description'] = description_match.group(1).strip()
            interfaces.append(interface_info)
    return interfaces

# Example usage with provided interface config output
interface_config_output = """
interface GigabitEthernet1/1/2
 description Some description
 ip address 192.168.1.1 255.255.255.0
 ip address 10.1.4.5 255.255.255.255
 ipv6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64
!

interface Vlan1
 description Another interface
 ipv6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7335/64
!

interface Tunnel0
 description Tunnel interface
 ip address 10.0.0.1 255.255.255.0
!

interface Loopback0
 description Loopback interface
 ip address 127.0.0.1 255.0.0.0
!

interface Loopback1
 description Loopback interface
 ip address 127.0.0.1/32
!
"""

interfaces = get_interface_info(interface_config_output)
print(interfaces)
