import socket

# Input the target host (IP or domain) and port range
target = input("Enter the target IP or hostname: ")
port_min = int(input("Enter the starting port: "))
port_max = int(input("Enter the ending port: "))

# Function to scan a single port
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: Open")
    sock.close()

# Scanning ports in the specified range
print(f"\nScanning target {target} from port {port_min} to {port_max}...")
for port in range(port_min, port_max + 1):
    scan_port(port)

print("\nScanning complete.")
