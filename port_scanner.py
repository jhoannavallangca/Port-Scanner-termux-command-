import socket

# Get the target IP and port range
target = input("Enter Target IP: ")
port_min = int(input("Enter Starting Port: "))
port_max = int(input("Enter Ending Port: "))

# Function to scan a single port
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex((target, port)) == 0:
        print(f"Port {port} is open")
    sock.close()

# Scan the specified port range
print(f"\nScanning {target} from port {port_min} to {port_max}...")
for port in range(port_min, port_max + 1):
    scan_port(port)

print("\nScanning complete.")
