import ipaddress

def subtract_two_from_third_octet(ip_address):
    try:
        # Parse the IP address
        ip = ipaddress.IPv4Address(ip_address)
        
        # Split the IP address into octets
        octets = list(ip.packed)
        
        # Subtract 2 from the third octet
        octets[2] = max(0, octets[2] - 2)
        
        # Create a new IPv4Address object with the modified octets
        new_ip = ipaddress.IPv4Address(bytes(octets))
        
        return str(new_ip)
    except ipaddress.AddressValueError:
        return "Invalid IPv4 address"

# Example usage:
ipv4_address = "192.168.1.100"
new_ipv4_address = subtract_two_from_third_octet(ipv4_address)
print("Original IPv4 Address:", ipv4_address)
print("Modified IPv4 Address:", new_ipv4_address)


import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum level for the messages to be logged
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the format of the log messages
    datefmt='%Y-%m-%d %H:%M:%S'  # Define the date/time format for log messages
)
