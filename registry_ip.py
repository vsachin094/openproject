import socket

def fetch_registry_ip(domain, whois_server):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((whois_server, 43))
            s.sendall((domain + '\r\n').encode())
            response = ''
            while True:
                data = s.recv(1024)
                if not data:
                    break
                response += data.decode()
        return response
    except Exception as e:
        return str(e)

def check_ip_in_registries(ip):
    results = {}
    results['APNIC'] = fetch_registry_ip(ip, 'whois.apnic.net')
    results['RIPE'] = fetch_registry_ip(ip, 'whois.ripe.net')
    results['ARIN'] = fetch_registry_ip(ip, 'whois.arin.net')
    return results

if __name__ == "__main__":
    ip = input("Enter the IP address to check: ")
    registry_results = check_ip_in_registries(ip)
    for registry, result in registry_results.items():
        print(f"Result from {registry}:\n{result}\n")