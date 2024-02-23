import re

def parse_static_routes(config):
    static_routes = []
    lines = config.split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('ip route'):
            parts = line.split()
            route_info = {}
            destination = parts[2]
            route_info['destination'] = destination
            if '/' in parts[3]:  # Check if next hop is specified as IP/mask
                route_info['next_hop'] = parts[3]
            else:
                next_hop = parts[3]
                if len(parts) == 5:
                    if parts[4].startswith('GigabitEthernet') or parts[4].startswith('Ethernet'):
                        route_info['interface'] = parts[4]
                    else:
                        route_info['next_hop'] = next_hop
                        route_info['administrative_distance'] = int(parts[4])
                else:
                    route_info['next_hop'] = next_hop
            static_routes.append(route_info)
        elif line.startswith('ipv6 route'):
            parts = line.split()
            route_info = {}
            destination = parts[2]
            next_hop = parts[3]
            route_info['destination'] = destination
            route_info['next_hop'] = next_hop
            static_routes.append(route_info)
        elif line.startswith('ip route vrf'):
            parts = line.split()
            route_info = {}
            vrf = parts[2]
            destination = parts[3]
            next_hop = parts[4]
            route_info['vrf'] = vrf
            route_info['destination'] = destination
            route_info['next_hop'] = next_hop
            static_routes.append(route_info)
    return static_routes

# Example usage:
router_config = """
ip route 192.168.1.0/24 10.0.0.1
ip route 10.10.10.0 255.255.255.0 GigabitEthernet0/0
ip route 192.168.2.0 255.255.255.0 10.0.0.2 150
ipv6 route 2001:db8::/32 2001:db8:0:1::1
ip route vrf CUSTOMER_A 192.168.3.0 255.255.255.0 10.0.0.3
"""
parsed_routes = parse_static_routes(router_config)
print(parsed_routes)