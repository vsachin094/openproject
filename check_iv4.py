import pandas as pd
import ipaddress

# Example DataFrame
data = {
    'IPv4_Subnet': ['192.168.1.0/24', '10.0.0.0/8', 'fe80::/64'],
    'IPv6': ['2001:0db8:85a3:0000:0000:8a2e:0370:7334', 'fe80::1', '192.168.1.1']
}

df = pd.DataFrame(data)

# Function to check if value is IPv6 address
def is_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

# Remove rows where IPv6 address is present
df = df[~df['IPv6'].apply(lambda x: is_ipv6(x))]

print(df)