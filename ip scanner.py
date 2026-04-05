import ipaddress
import subprocess

def ping_ip(ip):
    try:
        output = subprocess.run(
            ["ping", "-c", "1", str(ip)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return output.returncode == 0
    except Exception:
        return False

def main():
    start_ip = input("Enter the starting IP address: ")
    end_ip = input("Enter the ending IP address: ")

    ip_range = ipaddress.summarize_address_range(
        ipaddress.IPv4Address(start_ip),
        ipaddress.IPv4Address(end_ip)
    )

    for block in ip_range:
        for ip in block.hosts():
            if ping_ip(ip):
                print(f"{ip} is alive")

if __name__ == "__main__":
    main()
