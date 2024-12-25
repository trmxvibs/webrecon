import os
import webbrowser

# Banner Function
def banner():
    print("=" * 50)
    print("Welcome to WebRecon Toolkit!")
    print("YouTube: https://www.youtube.com/@TermuxVibes")
    print("=" * 50)

# Main Menu
def main_menu():
    print("""
1. Ping Test
2. Whois Lookup
3. NSLookup
4. Port Scanning (Nmap)
5. Banner Grabbing
6. Open YouTube Channel
7. Exit
""")
    return input("Choose an option: ")

# Sub-menu for Ping
def ping_menu():
    print("""
Ping Test Options:
1. Ping a domain or IP
2. Continuous Ping Test
3. Ping with specific packet size
4. Return to Main Menu
""")
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
    print("""
Whois Lookup Options:
1. Domain Whois
2. IP Whois
3. Whois with full output
4. Return to Main Menu
""")
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
    print("""
NSLookup Options:
1. Basic NSLookup
2. Reverse DNS Lookup
3. Query specific DNS record (A, MX, CNAME, etc.)
4. Return to Main Menu
""")
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

# Sub-menu for Nmap
def nmap_menu():
    print("""
Port Scanning Options (Nmap):
1. Root User Commands
2. Non-Root User Commands
3. Return to Main Menu
""")
    return input("Choose an option: ")

def nmap_root():
    commands = [
        "nmap -sS target", 
        "nmap -sU target", 
        "nmap -A target", 
        "nmap -p 22,80,443 target",
        "nmap -Pn target",
        "nmap -O target",
        "nmap --script vuln target",
        "nmap --top-ports 20 target",
        "nmap --script ssl-enum-ciphers target",
        "nmap -p- target"
    ]
    print("Root User Commands:")
    for i, cmd in enumerate(commands, 1):
        print(f"{i}. {cmd}")
    input("Press Enter to return to previous menu...")

def nmap_non_root():
    commands = [
        "nmap -sT target", 
        "nmap -p 80 target", 
        "nmap -sV target", 
        "nmap -O target",
        "nmap --script http-title target",
        "nmap -Pn target",
        "nmap --top-ports 10 target",
        "nmap --script dns-brute target",
        "nmap -F target",
        "nmap -A -p 22,80,443 target"
    ]
    print("Non-Root User Commands:")
    for i, cmd in enumerate(commands, 1):
        print(f"{i}. {cmd}")
    input("Press Enter to return to previous menu...")

def nmap():
    while True:
        choice = nmap_menu()
        if choice == "1":
            nmap_root()
        elif choice == "2":
            nmap_non_root()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

# Sub-menu for Banner Grabbing
def banner_grabbing():
    domain = input("Enter domain for Banner Grabbing (e.g., example.com): ")
    os.system(f"nc -v {domain} 80")

# Open YouTube Channel
def open_youtube():
    print("Opening Termux Vibes YouTube Channel...")
    webbrowser.open("https://www.youtube.com/@TermuxVibes")

# Main Function
def main():
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
            nmap()
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
