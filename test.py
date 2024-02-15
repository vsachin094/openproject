import re
import pandas as pd

def get_interface_info(interface_config_output):
    interfaces = []
    # Regular expression pattern to match interface details
    interface_pattern = r"interface (\S+)\s*([\s\S]*?)(?=^interface|\Z)"
    # Search for all interface patterns in the configuration output
    matches = re.finditer(interface_pattern, interface_config_output, re.MULTILINE)
    hostname_pattern = re.compile(r"hostname\s+(\S+)")
    hostname_match = hostname_pattern.search(interface_config_output)
    hostname = hostname_match.group(1) if hostname_match else None
    for match in matches:
        # Extract interface name
        interface_name = match.group(1)
        # Extract interface configuration block
        interface_config = match.group(2)
        
        # Extract IPv4 addresses (both primary and secondary)
        ip_matches = re.finditer(r"(?:(ip|ipv4) address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?:/(\d{1,2}))?\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})?( secondary)?)", interface_config)
        
        # Extract IPv6 addresses
        ipv6_matches = re.finditer(r"(ipv6 address ([\w:]+)/(\d+))( secondary)?", interface_config)
        
        # Extract description
        description_match = re.search(r"description (.*)", interface_config)
        
        # Process IPv4 addresses
        for ip_match in ip_matches:
            interface_info = {'hostname': hostname, 'interface_name': interface_name, 'ip_address': ip_match.group(2)}
            if ip_match.group(3):
                interface_info['mask_prefix'] = ip_match.group(3)
            elif ip_match.group(4):
                interface_info['mask_prefix'] = ip_match.group(4)  # Default to /32 if no subnet mask is provided
            if ip_match.group(5):
                interface_info['ip_type'] = ip_match.group(5)
            else:
                interface_info['ip_type'] = 'primary'
            if description_match:
                interface_info['description'] = description_match.group(1).strip()
            interfaces.append(interface_info)

        # Process IPv6 addresses
        for ipv6_match in ipv6_matches:
            interface_info = {'hostname': hostname, 'interface_name': interface_name, 'ip_address': ipv6_match.group(2), 'mask_prefix': int(ipv6_match.group(3))}
            if ipv6_match.group(4):
                interface_info['ip_type'] = ipv6_match.group(4)
            else:
                interface_info['ip_type'] = 'primary'
            if description_match:
                interface_info['description'] = description_match.group(1).strip()
            interfaces.append(interface_info)
    return interfaces

# Example usage with provided interface config output
interface_config_output = """
hostname Router1
interface GigabitEthernet1/1/2
 description Some description
 ip address 192.168.1.1 255.255.255.0
 ip address 10.1.4.5 255.255.255.255 secondary
 ip address 10.2.3.4 255.255.255.0 secondary
 ip address 10.1.1.4/32
 ipv6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7334/64 secondary
!

interface Vlan1
 description Another interface
 ipv6 address 2001:0db8:85a3:0000:0000:8a2e:0370:7335/64
!

interface Tunnel0
 description Tunnel interface
 ip address 10.0.0.1 255.255.255.0
 ip address 192.168.2.1 255.255.255.0 secondary
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

# Convert interface info into DataFrame
df = pd.DataFrame(interfaces)
print(df.head())
