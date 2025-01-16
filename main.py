import socket

def port_scanner(target, ports):
    print(f"Scanning {target} for open ports (1-{ports})...\n")
    for port in range(1, ports + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"[+] Port {port}: Open")
        except Exception as e:
            print(f"[-] Error on port {port}: {e}")

if __name__ == "__main__":
    target_ip = input("Enter target IP or domain: ")
    max_ports = int(input("Enter the number of ports to scan (e.g., 100): "))
    port_scanner(target_ip, max_ports)
