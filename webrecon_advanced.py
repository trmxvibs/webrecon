# tool made by lokesh kumar
# Lokesh Kumar
# [Github](https://github.com/trmxvibs/webrecon)
# [Youtube](https://youtube.com/@termux2)


import os
import webbrowser
import random
import time

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Loading Bars Function
def loading_bars(duration=15):
    end_time = time.time() + duration
    loading_styles = ["|/-\\", "█░░░░░░░░░░", "░█░░░░░░░░░", "░░█░░░░░░░░", "░░░█░░░░░░░"]
    while time.time() < end_time:
        style = random.choice(loading_styles)
        for char in style:
            print(f"\r{MAGENTA}{char}{RESET}", end='', flush=True)
            time.sleep(0.1)
        print("\r", end='', flush=True)

# Banner Function
def banner():
    print(f"{CYAN}{'=' * 50}")
    print("Welcome to WebRecon Toolkit!")
    print("YouTube: https://www.youtube.com/@TermuxVibes")
    print(f"{'=' * 50}{RESET}")

# Main Menu
def main_menu():
    print(f"{YELLOW}\n1. Ping Test\n2. Whois Lookup\n3. NSLookup\n4. Port Scanning (Nmap)\n5. Banner Grabbing\n6. Open YouTube Channel\n7. Exit{RESET}")
    return input("Choose an option: ")

# Sub-menu for Ping
def ping_menu():
    print(f"{GREEN}\nPing Test Options:\n1. Ping a domain or IP\n2. Continuous Ping Test\n3. Ping with specific packet size\n4. Return to Main Menu{RESET}")
    return input("Choose an option: ")

def ping_test():
    while True:
        choice = ping_menu()
        if choice == "1":
            domain = input("Enter domain or IP to ping: ")
            os.system(f"ping -c 4 {domain}")
        elif choice == "2":
            domain = input("Enter domain or IP for continuous ping: ")
            os.system(f"ping {domain}")
        elif choice == "3":
            domain = input("Enter domain or IP: ")
            size = input("Enter packet size (in bytes): ")
            os.system(f"ping -s {size} -c 4 {domain}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

# Sub-menu for Whois Lookup
def whois_menu():
    print(f"{BLUE}\nWhois Lookup Options:\n1. Domain Whois\n2. IP Whois\n3. Whois with full output\n4. Return to Main Menu{RESET}")
    return input("Choose an option: ")

def whois_lookup():
    while True:
        choice = whois_menu()
        if choice == "1":
            domain = input("Enter domain for Whois Lookup: ")
            os.system(f"whois {domain}")
        elif choice == "2":
            ip = input("Enter IP address for Whois Lookup: ")
            os.system(f"whois {ip}")
        elif choice == "3":
            domain = input("Enter domain for full Whois output: ")
            os.system(f"whois -H {domain}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

# Sub-menu for NSLookup
def nslookup_menu():
    print(f"{MAGENTA}\nNSLookup Options:\n1. Basic NSLookup\n2. Reverse DNS Lookup\n3. Query specific DNS record (A, MX, CNAME, etc.)\n4. Return to Main Menu{RESET}")
    return input("Choose an option: ")

def nslookup():
    while True:
        choice = nslookup_menu()
        if choice == "1":
            domain = input("Enter domain for NSLookup: ")
            os.system(f"nslookup {domain}")
        elif choice == "2":
            ip = input("Enter IP address for Reverse DNS Lookup: ")
            os.system(f"nslookup {ip}")
        elif choice == "3":
            domain = input("Enter domain: ")
            record_type = input("Enter DNS record type (e.g., A, MX, CNAME): ")
            os.system(f"nslookup -type={record_type} {domain}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

# Updated Nmap Menu Function
def nmap_menu():
    print(f"{RED}\n--- Nmap Scanning Menu ---")
    print("1. Root User Commands")
    print("2. Non-Root User Commands")
    print("3. Back to Main Menu{RESET}")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        print(f"{RED}\n--- Root User Commands ---")
        print("1. Full Scan (All ports and services)")
        print("2. Vulnerability Scan (Find vulnerabilities)")
        print("3. OS Detection (Operating system details)")
        print("4. Aggressive Scan (Comprehensive scan)")
        print("5. UDP Scan (Scan for UDP services)")
        print("6. Script Scan (Run custom Nmap scripts)")
        print("7. Firewall Evasion (Bypass firewalls)")
        print("8. Stealth Scan (Avoid detection)")
        print("9. Traceroute Analysis (Identify route to target)")
        print("10. Back to Nmap Menu")
        
        root_choice = input("Choose an option (1-10): ")
        target = input("Enter target IP or domain: ")
        
        if root_choice == "1":
            os.system(f"sudo nmap -p- {target}")
        elif root_choice == "2":
            os.system(f"sudo nmap --script vuln {target}")
        elif root_choice == "3":
            os.system(f"sudo nmap -O {target}")
        elif root_choice == "4":
            os.system(f"sudo nmap -A {target}")
        elif root_choice == "5":
            os.system(f"sudo nmap -sU {target}")
        elif root_choice == "6":
            os.system(f"sudo nmap --script default {target}")
        elif root_choice == "7":
            os.system(f"sudo nmap -f {target}")
        elif root_choice == "8":
            os.system(f"sudo nmap -sS {target}")
        elif root_choice == "9":
            os.system(f"sudo nmap --traceroute {target}")
        elif root_choice == "10":
            nmap_menu()
        else:
            print("Invalid choice. Returning to Nmap Menu.")
            nmap_menu()
    
    elif choice == "2":
        print(f"{RED}\n--- Non-Root User Commands ---")
        print("1. Quick Scan (Fast scan for common ports)")
        print("2. Service Version Scan (Detect service versions)")
        print("3. Host Discovery (Find live hosts)")
        print("4. Port Scan (Scan specific ports)")
        print("5. Top Ports Scan (Scan the most used ports)")
        print("6. Ping Sweep (Ping multiple hosts)")
        print("7. No DNS Resolution (Skip DNS resolution)")
        print("8. Scan a Specific Range (Define a port range)")
        print("9. Scan a List of Targets (File input)")
        print("10. Back to Nmap Menu")
        
        non_root_choice = input("Choose an option (1-10): ")
        target = input("Enter target IP or domain: ")
        
        if non_root_choice == "1":
            os.system(f"nmap -F {target}")
        elif non_root_choice == "2":
            os.system(f"nmap -sV {target}")
        elif non_root_choice == "3":
            os.system(f"nmap -sn {target}")
        elif non_root_choice == "4":
            ports = input("Enter specific ports (e.g., 22,80,443): ")
            os.system(f"nmap -p {ports} {target}")
        elif non_root_choice == "5":
            os.system(f"nmap --top-ports 100 {target}")
        elif non_root_choice == "6":
            os.system(f"nmap -sn 192.168.1.0/24")
        elif non_root_choice == "7":
            os.system(f"nmap --dns-server 8.8.8.8 {target}")
        elif non_root_choice == "8":
            range_input = input("Enter port range (e.g., 1-1000): ")
            os.system(f"nmap -p {range_input} {target}")
        elif non_root_choice == "9":
            file_path = input("Enter path to file with targets: ")
            os.system(f"nmap -iL {file_path}")
        elif non_root_choice == "10":
            nmap_menu()
        else:
            print("Invalid choice. Returning to Nmap Menu.")
            nmap_menu()
    
    elif choice == "3":
        print("Returning to Main Menu...")
    else:
        print("Invalid choice. Please try again.")
        nmap_menu()

# Sub-menu for Banner Grabbing
def banner_grabbing():
    domain = input("Enter domain for Banner Grabbing (e.g., example.com): ")
    try:
        os.system(f"nc -v {domain} 80")
    except Exception as e:
        print(f"Netcat failed: {e}")
        print("Trying with telnet...")
        try:
            os.system(f"telnet {domain} 80")
        except Exception as e:
            print(f"Telnet failed: {e}")
# Open YouTube Channel
def open_youtube():
    print("Opening Termux Vibes YouTube Channel...")
    os.system("xdg-open https://www.youtube.com/@TermuxVibes")

# Main Function
def main():
    os.system('clear' ) # to clear the terminal 
    loading_bars()
    while True:
        banner()
        choice = main_menu()

        if choice == "1":
            ping_test()
        elif choice == "2":
            whois_lookup()
        elif choice == "3":
            nslookup()
        elif choice == "4":
            nmap_menu()
        elif choice == "5":
            banner_grabbing()
        elif choice == "6":
            open_youtube()
        elif choice == "7":
            print("Exiting... Thank you for using WebRecon!")
            break
        else:
            print("Invalid option. Please try again!")

if __name__ == "__main__":
    main()
