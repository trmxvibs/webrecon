#!/usr/bin/env python3

"""
Author: Lokesh Kumar
Date: February 06, 2026
"""
import os
import sys
import time
import socket
import platform
import subprocess
import urllib.request
import urllib.error
import shutil
import json
import random
import string
from datetime import datetime

# --- Configuration & Aesthetics ---

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
# --- UI Engine (Centering & Layout) ---

def get_width():
    try:
        cols, _ = shutil.get_terminal_size()
        return cols
    except: return 80

def c_print(text, color=Colors.WHITE):
    w = get_width()
    clean = text.replace(Colors.RED,'').replace(Colors.GREEN,'').replace(Colors.YELLOW,'').replace(Colors.BLUE,'').replace(Colors.MAGENTA,'').replace(Colors.CYAN,'').replace(Colors.WHITE,'').replace(Colors.RESET,'').replace(Colors.BOLD,'')
    pad = max(0, (w - len(clean)) // 2)
    print(" " * pad + color + text + Colors.RESET)

def c_input(prompt, color=Colors.GREEN):
    w = get_width()
    pad = max(0, (w - len(prompt) - 20) // 2)
    return input(" " * pad + color + prompt + Colors.RESET)

def draw_bar():
    w = int(get_width() * 0.95)
    pad = (get_width() - w) // 2
    print(" " * pad + Colors.BLUE + "━" * w + Colors.RESET)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- THE INSANE BOOT SEQUENCE (30 Seconds) ---

def insane_boot_sequence():
    clear_screen()
    
    # Phase 1: BIOS/Kernel Check (5 Seconds)
    print(Colors.CYAN + "[*] BIOS DATE 01/01/2026 14:22:55 VER 1.02")
    print(Colors.CYAN + "[*] CPU:  CORES DETECTED")
    time.sleep(1)
    checks = ["RAM", "VRAM", "SSD", "NETWORK", "KERNEL", "PYTHON3", "SOCKETS", "WIFI"]
    for check in checks:
        print(f"{Colors.WHITE}[+] CHECKING {check:<10} ......... {Colors.GREEN}[ OK ]")
        time.sleep(0.4)
    print(Colors.YELLOW + "\n[!] SYSTEM INTEGRITY VERIFIED. LOADING CORE MODULES...\n")
    time.sleep(5)

    # Phase 2: Hex/Matrix Dump 
    print(Colors.GREEN)
    start_hex = time.time()
    while time.time() - start_hex < 7:
        # Generate random hex strings
        hex_str = " ".join([f"{random.randint(0, 255):02X}" for _ in range(12)])
        print(f" {hex_str}  |  {hex_str}  |  {hex_str}")
        time.sleep(0.05)
    
    # Phase 3: Module Extraction 
    clear_screen()
    c_print("[ INITIALIZING WEBRECON FRAMEWORK ]", Colors.BOLD + Colors.WHITE)
    print("\n")
    modules = [
        "loading_network_driver.py", "bypass_firewall.exe", "bruteforce_engine.lib",
        "geoip_satellite_uplink.dll", "nmap_stealth_mode.sh", "admin_panel_finder.py",
        "sql_injection_scanner.rb", "xss_payload_generator.js", "tor_proxy_chain.conf",
        "anonymous_identity.ovpn", "decryption_keys.pem", "target_lock_system.bin"
    ]
    for mod in modules:
        c_print(f"> Extracting: {mod} ...", Colors.CYAN)
        c_print(f"  [####################] 100%", Colors.GREEN)
        time.sleep(0.6)
    
    # Phase 4: Connection Uplink 
    clear_screen()
    c_print("ESTABLISHING SECURE CONNECTION...", Colors.RED)
    time.sleep(1)
    servers = ["192.168.1.1", "10.0.0.55", "172.16.42.12", "PROXY_NODE_01", "TOR_EXIT_RELAY"]
    for server in servers:
        c_print(f"Handshake with {server} ... SUCCESS", Colors.YELLOW)
        time.sleep(0.8)
    
    # Phase 5: Final Engine Launch 
    clear_screen()
    c_print("STARTING MAIN ENGINE", Colors.MAGENTA)
    width = 50
    for i in range(width + 1):
        percent = int((i / width) * 100)
        bar = "█" * i + "░" * (width - i)
        c_print(f"[{bar}] {percent}%", Colors.GREEN)
        sys.stdout.write("\033[F") # Cursor up
        time.sleep(0.1)
    
    time.sleep(1)
    c_print("\n\nACCESS GRANTED.", Colors.BOLD + Colors.WHITE)
    time.sleep(1)

# --- Network Helpers ---

def get_ip(mode="public"):
    try:
        if mode == "public":
            with urllib.request.urlopen('https://api64.ipify.org', timeout=2) as r:
                return r.read().decode('utf-8')
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
    except: return "Unknown"

# --- Visual Components ---

def banner():
    clear_screen()
    print("\n")
    art = [
        "██╗    ██╗███████╗██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗",
        "██║    ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║",
        "██║ █╗ ██║█████╗  ██████╔╝██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║",
        "██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║",
        "╚███╔███╔╝███████╗██████╔╝██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║",
        " ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝"
    ]
    for line in art: c_print(line, Colors.CYAN + Colors.BOLD)
    print("\n")
    c_print("WebRecon 1.2 ACTIVATED", Colors.WHITE + Colors.BOLD)
    c_print("Architect: Lokesh Kumar", Colors.MAGENTA)
    print("\n")

def dashboard():
    u = os.getlogin() if hasattr(os, 'getlogin') else 'Root'
    o = f"{platform.system()} {platform.release()}"
    l_ip = get_ip("local")
    p_ip = get_ip("public")
    t = datetime.now().strftime('%H:%M:%S')
    
    # Dashboard Grid
    c_print(f"╔{'═'*20}╦{'═'*20}╦{'═'*20}╗", Colors.BLUE)
    c_print(f"║ USER: {u[:12]:<12} ║ IP: {l_ip:<14} ║ TIME: {t:<12} ║", Colors.WHITE)
    c_print(f"╚{'═'*20}╩{'═'*20}╩{'═'*20}╝", Colors.BLUE)
    c_print(f" ► PUBLIC NODE: {p_ip} | SYSTEM: {o} ◄ ", Colors.YELLOW)
    print("\n")

def menu_item(idx, name, color):
    return f"{Colors.BLUE}[{Colors.WHITE}{idx}{Colors.BLUE}] {color}{name:<22}{Colors.RESET}"

def show_menu():
    pad = (get_width() - 60) // 2 
    sp = " " * pad
    
    draw_bar()
    print(f"{sp}{menu_item('01', 'PING TARGET', Colors.CYAN)}  {menu_item('06', 'ADMIN FINDER', Colors.YELLOW)}")
    print(f"{sp}{menu_item('02', 'WHOIS LOOKUP', Colors.CYAN)}  {menu_item('07', 'SUBDOMAIN HUNT', Colors.YELLOW)}")
    print(f"{sp}{menu_item('03', 'PORT SCANNER', Colors.CYAN)}  {menu_item('08', 'WAF DETECTOR', Colors.YELLOW)}")
    print(f"{sp}{menu_item('04', 'DNS LOOKUP', Colors.CYAN)}  {menu_item('09', 'ROBOTS.TXT', Colors.YELLOW)}")
    print(f"{sp}{menu_item('05', 'GEO-IP TRACK', Colors.MAGENTA)}  {menu_item('10', 'YOUTUBE CHANNEL', Colors.RED)}")
    print(f"{sp}{menu_item('00', 'EXIT SYSTEM', Colors.RED)}")
    draw_bar()

# --- TOOLS ---

def t_admin():
    c_print("--- ADMIN PANEL HUNTER ---", Colors.YELLOW)
    url = c_input("Target URL: ")
    if "://" not in url: url = "http://" + url
    paths = ["admin/", "login/", "wp-admin/", "cpanel/", "user/", "administrator/"]
    for p in paths:
        try:
            full = f"{url}/{p}"
            r = urllib.request.urlopen(full, timeout=2)
            if r.getcode() == 200: c_print(f"[+] FOUND: {full}", Colors.GREEN)
        except: pass
    c_print("[*] Scan Complete.", Colors.WHITE); input()

def t_geoip():
    c_print("--- IP GEOLOCATION TRACKER ---", Colors.MAGENTA)
    target = c_input("Enter IP or Domain: ")
    try:
        ip = socket.gethostbyname(target)
        c_print(f"[*] Resolving {ip}...", Colors.CYAN)
        with urllib.request.urlopen(f"http://ip-api.com/json/{ip}") as r:
            data = json.load(r)
        c_print(f"\n[+] COUNTRY : {data.get('country')}", Colors.GREEN)
        c_print(f"[+] ISP     : {data.get('isp')}", Colors.GREEN)
        c_print(f"[+] MAPS    : http://maps.google.com/?q={data.get('lat')},{data.get('lon')}", Colors.YELLOW)
    except: c_print("[!] Lookup Failed.", Colors.RED)
    input()

def t_robots():
    c_print("--- ROBOTS.TXT READER ---", Colors.YELLOW)
    url = c_input("Target URL: ")
    if "://" not in url: url = "http://" + url
    try:
        with urllib.request.urlopen(f"{url}/robots.txt", timeout=5) as r:
            c_print("\n" + r.read().decode(), Colors.WHITE)
    except: c_print("[!] No robots.txt found.", Colors.RED)
    input()

def t_portscan():
    c_print("--- PYTHON PORT SCANNER ---", Colors.CYAN)
    target = c_input("Target IP: ")
    c_print("[*] Scanning Top Ports...", Colors.WHITE)
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, p)) == 0:
            c_print(f"[+] Port {p} : OPEN", Colors.GREEN)
        s.close()
    input()

def t_subdomain():
    c_print("--- SUBDOMAIN HUNTER ---", Colors.YELLOW)
    d = c_input("Domain: ").replace("http://","").split('/')[0]
    try:
        url = f"https://crt.sh/?q=%.{d}&output=json"
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.loads(r.read().decode())
        subs = set(e['name_value'].split('\n')[0] for e in data)
        for s in list(subs)[:10]: c_print(f"[+] {s}", Colors.GREEN)
    except: c_print("[!] Error fetching data.", Colors.RED)
    input()

def t_waf():
    c_print("--- WAF DETECTOR ---", Colors.YELLOW)
    url = c_input("URL: ")
    if "://" not in url: url = "http://" + url
    try:
        r = urllib.request.urlopen(url, timeout=5)
        h = str(r.info()).lower()
        if 'cloudflare' in h: c_print("[!] CLOUDFLARE DETECTED", Colors.RED)
        elif 'sucuri' in h: c_print("[!] SUCURI DETECTED", Colors.RED)
        else: c_print("[+] No Standard WAF Detected", Colors.GREEN)
    except: c_print("[!] Connection Failed", Colors.RED)
    input()

def run_sys(cmd):
    subprocess.call(cmd, shell=True)
    input()

# --- MAIN ---

def main():
    # RUN BOOT SEQUENCE
    insane_boot_sequence()
    
    while True:
        banner()
        dashboard()
        show_menu()
        
        print("\n")
        ch = c_input("SELECT MODULE >> ", Colors.GREEN + Colors.BOLD)
        
        if ch == '1' or ch == '01': 
            t = c_input("Target: ")
            run_sys(f"ping -c 4 {t}" if os.name != 'nt' else f"ping -n 4 {t}")
        elif ch == '2' or ch == '02': 
            t = c_input("Domain: ")
            run_sys(f"whois {t}")
        elif ch == '3' or ch == '03': t_portscan() 
        elif ch == '4' or ch == '04':
            t = c_input("Domain: ")
            run_sys(f"nslookup {t}")
        elif ch == '5' or ch == '05': t_geoip()   
        elif ch == '6' or ch == '06': t_admin()
        elif ch == '7' or ch == '07': t_subdomain()
        elif ch == '8' or ch == '08': t_waf()
        elif ch == '9' or ch == '09': t_robots()  
        elif ch == '10':
            if sys.platform=='win32': os.system("start https://youtube.com/@TermuxVibes")
            else: os.system("xdg-open https://youtube.com/@TermuxVibes")
        elif ch == '0' or ch == '00': 
            c_print("SHUTTING DOWN...", Colors.RED)
            time.sleep(1)
            clear_screen()
            sys.exit() # Clean Exit

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: 
        print("\n")
        c_print("[!] KEYBOARD INTERRUPT DETECTED. EXITING...", Colors.RED)
        sys.exit()
