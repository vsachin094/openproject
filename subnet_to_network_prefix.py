import ipaddress

def find_network_prefix(ip_address, subnet_mask):
    # Create IPv4Address objects for IP address and subnet mask
    ip = ipaddress.IPv4Address(ip_address)
    
    # Check if subnet mask is in CIDR notation
    if '/' in subnet_mask:
        # Create IPv4Network object from CIDR notation
        network = ipaddress.IPv4Network(ip_address + subnet_mask, strict=False)
        
        # Return the network address with CIDR notation
        return str(network)
    else:
        # Create IPv4Address object for subnet mask
        mask = ipaddress.IPv4Address(subnet_mask)
        
        # Calculate network address using bitwise AND operation
        network_address = ipaddress.IPv4Address(int(ip) & int(mask))
        
        # Find the prefix length from the subnet mask
        mask_bits = bin(int(mask)).count('1')
        
        # Return the network address with prefix length
        return f"{network_address}/{mask_bits}"

# Example usage
ip_address = '192.168.1.10'
subnet_mask = '/24'

network_prefix = find_network_prefix(ip_address, subnet_mask)
print("Network Prefix:", network_prefix)

# Example usage with subnet mask in traditional format
subnet_mask = '255.255.255.254'

network_prefix = find_network_prefix(ip_address, subnet_mask)
print("Network Prefix:", network_prefix)
