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
        
        
        
import requests

def fetch_registry_ip_with_proxy(domain, whois_server, proxy):
    try:
        response = requests.get(f'http://{whois_server}/lookup/{domain}', proxies={'http': proxy, 'https': proxy})
        return response.text
    except Exception as e:
        return str(e)

def check_ip_in_registries_with_proxy(ip, proxy):
    results = {}
    results['APNIC'] = fetch_registry_ip_with_proxy(ip, 'rdap.apnic.net', proxy)
    results['RIPE'] = fetch_registry_ip_with_proxy(ip, 'rdap.db.ripe.net', proxy)
    results['ARIN'] = fetch_registry_ip_with_proxy(ip, 'rdap.arin.net', proxy)
    return results

if __name__ == "__main__":
    ip = input("Enter the IP address to check: ")
    proxy = input("Enter the proxy (e.g., http://username:password@proxy_ip:proxy_port): ")
    registry_results = check_ip_in_registries_with_proxy(ip, proxy)
    for registry, result in registry_results.items():
        print(f"Result from {registry}:\n{result}\n")