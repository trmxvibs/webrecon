#!/usr/bin/env python3

"""
WebRecon 2.0
Architect: Lokesh Kumar
Refactored: Fixed APIs, Restored Modules, True Cross-Platform (Termux/Windows/Linux/iOS)
"""

import os
import sys
import time
import socket
import platform
import subprocess
import random
import webbrowser
from datetime import datetime
import concurrent.futures

# --- External Libraries ---
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich.prompt import Prompt
    from rich.align import Align
    import requests
except ImportError:
    print("[!] Critical Error: Missing required libraries.")
    print("Run this command to fix: pip install rich requests")
    sys.exit(1)

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip(mode="public"):
    try:
        if mode == "public":
            return requests.get('https://api64.ipify.org', timeout=3).text
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
    except:
        return "Unknown"

# --- THE 30-SECOND CINEMATIC BOOT SEQUENCE ---
def insane_boot_sequence():
    clear_screen()
    console.print("[bold green]INITIATING COLD BOOT SEQUENCE...[/bold green]")
    time.sleep(1)
    checks = ["BIOS Signature... OK", "Kernel Memory Space... ALLOCATED", "Network Interfaces... DETECTED", "Encryption Keys... VERIFIED"]
    for check in checks:
        console.print(f"[bold cyan][*] {check}[/bold cyan]")
        time.sleep(0.8)
    
    clear_screen()
    console.print("[bold red]DECRYPTING MAINFRAME PAYLOADS...[/bold red]\n")
    start_time = time.time()
    while time.time() - start_time < 8:
        line = "".join(random.choice(["0", "1", "@", "#", "$", "%", "&", "*", "X"]) for _ in range(80))
        console.print(f"[green]{line}[/green]")
        time.sleep(0.05)
    
    clear_screen()
    console.print(Align.center("[bold magenta]WEBRECON KERNEL INITIALIZATION[/bold magenta]\n"))
    
    with Progress(
        SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
        BarColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console, transient=True
    ) as progress:
        task_net = progress.add_task("[cyan]Engaging Network Drivers...", total=100)
        task_waf = progress.add_task("[yellow]Loading WAF Bypass Signatures...", total=100)
        task_exp = progress.add_task("[red]Arming Exploit Modules...", total=100)
        task_sec = progress.add_task("[blue]Establishing Secure Tunnel...", total=100)

        while not progress.finished:
            progress.update(task_net, advance=random.uniform(0.5, 2))
            progress.update(task_waf, advance=random.uniform(0.3, 1.5))
            progress.update(task_exp, advance=random.uniform(0.2, 1))
            progress.update(task_sec, advance=random.uniform(0.4, 1.8))
            time.sleep(0.05)
            
    clear_screen()
    user = os.environ.get('USER', os.environ.get('USERNAME', 'Root'))
    welcome_text = f"\n[bold green]System Decrypted Successfully.[/bold green]\n[bold cyan]Welcome back, Architect [white]{user}[/white].[/bold cyan]\n[bold yellow]The digital realm awaits your command.[/bold yellow]\n"
    console.print(Align.center(Panel(welcome_text, style="bold blue", expand=False)))
    time.sleep(4)

# --- Compact UI Engine ---
def display_dashboard():
    clear_screen()
    banner_text = """[bold cyan]
 ██╗    ██╗███████╗██████╗ ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
 ██║    ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
 ██║ █╗ ██║█████╗  ██████╔╝██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
 ██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
 ╚███╔███╔╝███████╗██████╔╝██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
  ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝[/bold cyan]"""
    console.print(Align.center(banner_text))
    console.print(Align.center("[bold magenta]WebRecon  | Architect: Lokesh Kumar[/bold magenta]\n"))

    user = os.environ.get('USER', os.environ.get('USERNAME', 'Root'))
    dash_text = f"[bold green]USER:[/bold green] {user} | [bold yellow]OS:[/bold yellow] {platform.system()} | [bold cyan]LOCAL:[/bold cyan] {get_ip('local')} | [bold blue]PUBLIC:[/bold blue] {get_ip('public')}"
    console.print(Align.center(Panel(dash_text, border_style="blue", expand=False)))

def show_menu():
    menu_content = """
[bold cyan][01][/bold cyan] STEALTH PING        [bold yellow][06][/bold yellow] ADMIN FINDER
[bold cyan][02][/bold cyan] WHOIS LOOKUP        [bold yellow][07][/bold yellow] SUBDOMAIN HUNT
[bold cyan][03][/bold cyan] PORT SCANNER        [bold yellow][08][/bold yellow] WAF DETECTOR
[bold cyan][04][/bold cyan] DNS ENUMERATION     [bold yellow][09][/bold yellow] ROBOTS.TXT
[bold cyan][05][/bold cyan] GEO-IP TRACK        [bold red][10][/bold red] DEV YOUTUBE
    
[bold red][00] EXIT FRAMEWORK[/bold red]"""
    console.print(Align.center(Panel(menu_content, title="[bold white]MODULE SELECTION[/bold white]", border_style="magenta", expand=False)))

# --- Pro Recon Modules ---

def t_ping():
    console.print(Align.center(Panel("STEALTH PING INITIATED", style="bold cyan", expand=False)))
    target = Prompt.ask("[bold cyan]Target Host[/bold cyan]")
    with console.status("[bold green]Transmitting ICMP Echo Requests...[/bold green]"):
        try:
            ip = socket.gethostbyname(target)
            cmd = ["ping", "-n", "4", ip] if os.name == 'nt' else ["ping", "-c", "4", ip]
            output = subprocess.run(cmd, capture_output=True, text=True).stdout
            
            if "ttl=" in output.lower() or "time=" in output.lower():
                console.print(f"\n[+] TARGET   : [bold white]{target}[/bold white]", style="bold green")
                console.print(f"[+] IP ADDR  : [bold cyan]{ip}[/bold cyan]", style="bold green")
                console.print("[+] STATUS   : [bold green]ONLINE (Connection Verified)[/bold green]")
                if os.name == 'nt':
                    avg = [line.strip() for line in output.split('\n') if 'Average' in line]
                    if avg: console.print(f"[*] RTT STATS: [bold yellow]{avg[0]}[/bold yellow]")
                else:
                    avg = [line.strip() for line in output.split('\n') if 'avg' in line]
                    if avg: console.print(f"[*] RTT STATS: [bold yellow]{avg[0]}[/bold yellow]")
            else:
                console.print("\n[-] STATUS   : [bold red]OFFLINE or BLOCKING ICMP[/bold red]")
        except socket.gaierror:
             console.print("\n[!] Invalid hostname or unable to resolve.", style="bold red")

def t_whois():
    console.print(Align.center(Panel("WHOIS LOOKUP", style="bold cyan", expand=False)))
    domain = Prompt.ask("[bold cyan]Domain[/bold cyan]")
    with console.status("[bold white]Querying Whois DB...[/bold white]"):
        try:
            # Using HackerTarget API as it is more stable than networkcalc
            r = requests.get(f"https://api.hackertarget.com/whois/?q={domain}", timeout=10)
            if r.status_code == 200 and "error" not in r.text.lower():
                console.print("\n[bold green]" + r.text[:1200] + ("\n\n...[TRUNCATED]" if len(r.text) > 1200 else "") + "[/bold green]")
            else:
                console.print("\n[!] Whois data not available.", style="bold red")
        except:
            console.print("\n[!] API Connection Error.", style="bold red")

def t_portscan():
    console.print(Align.center(Panel("FAST PORT SCANNER (THREADS: 50)", style="bold cyan", expand=False)))
    target = Prompt.ask("[bold cyan]Target IP/Domain[/bold cyan]")
    try:
        ip = socket.gethostbyname(target)
        console.print(f"\n[*] Target IP resolved: {ip}", style="bold white")
    except socket.gaierror:
        console.print("\n[!] Invalid hostname.", style="bold red")
        return

    common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]
    open_ports = []

    def scan_port(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            s.close()
            if result == 0: return port
        except: pass
        return None

    with console.status("[bold yellow]Scanning ports (Multithreaded)...") as status:
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            results = executor.map(scan_port, common_ports)
            for port in results:
                if port:
                    console.print(f"[+] Port {port:<5} : [bold green]OPEN[/bold green]")
                    open_ports.append(port)

    if not open_ports:
        console.print("[-] No common ports are open or host is blocking scans.", style="bold red")

def t_dns():
    console.print(Align.center(Panel("DNS ENUMERATION", style="bold cyan", expand=False)))
    domain = Prompt.ask("[bold cyan]Target Domain[/bold cyan]")
    with console.status(f"[bold white]Extracting DNS Records for {domain}...[/bold white]"):
        try:
            r = requests.get(f"https://dns.google/resolve?name={domain}&type=ANY", timeout=5).json()
            if 'Answer' in r:
                table = Table(show_header=True, header_style="bold magenta", expand=True)
                table.add_column("Type", style="cyan", width=10)
                table.add_column("TTL", style="yellow", justify="right", width=10)
                table.add_column("Data", style="green")
                
                type_map = {1: "A", 5: "CNAME", 15: "MX", 16: "TXT", 28: "AAAA"}
                for ans in r['Answer']:
                    record_type = type_map.get(ans['type'], f"Type {ans['type']}")
                    table.add_row(record_type, str(ans.get('TTL', 'N/A')), ans.get('data', ''))
                print()
                console.print(table)
            else:
                console.print("\n[!] No records found or DNS lookup failed.", style="bold red")
        except:
             console.print("\n[!] API Connection Error.", style="bold red")

def t_geoip():
    console.print(Align.center(Panel("IP GEOLOCATION TRACKER", style="bold magenta", expand=False)))
    target = Prompt.ask("[bold cyan]Target IP/Domain[/bold cyan]")
    with console.status("[bold white]Tracing Route & Geolocation...[/bold white]"):
        try:
            ip = socket.gethostbyname(target)
            r = requests.get(f"http://ip-api.com/json/{ip}").json()
            if r.get('status') == 'success':
                print()
                console.print(f"[bold green][+] TARGET  :[/bold green] {r.get('query')}")
                console.print(f"[bold green][+] COUNTRY :[/bold green] {r.get('country')} ({r.get('countryCode')})")
                console.print(f"[bold green][+] CITY    :[/bold green] {r.get('city')}, {r.get('regionName')}")
                console.print(f"[bold green][+] ISP     :[/bold green] {r.get('isp')}")
                console.print(f"[bold yellow][+] MAPS    :[/bold yellow] http://maps.google.com/?q={r.get('lat')},{r.get('lon')}")
            else:
                console.print("\n[!] Lookup failed.", style="bold red")
        except socket.gaierror:
            console.print("\n[!] Error resolving host.", style="bold red")
        except Exception as e:
            console.print(f"\n[!] API Error: {e}", style="bold red")

def t_admin():
    console.print(Align.center(Panel("ADMIN PANEL HUNTER", style="bold yellow", expand=False)))
    target = Prompt.ask("[bold cyan]Target URL (e.g., example.com)[/bold cyan]")
    if not target.startswith("http"): target = "http://" + target

    paths = ["admin", "login", "wp-admin", "cpanel", "user", "administrator", "admin.php", "login.php", "dashboard", "manager"]
    found = False

    def check_url(path):
        url = f"{target}/{path}"
        try:
            r = requests.get(url, timeout=4, allow_redirects=True)
            if r.status_code in [200, 302, 401, 403]: return f"[+] {r.status_code} - {url}"
        except: pass
        return None

    with console.status("[bold green]Hunting admin panels (Multi-threaded)...") as status:
        print()
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            results = executor.map(check_url, paths)
            for res in results:
                if res:
                    console.print(res, style="bold green")
                    found = True

    if not found:
        console.print("[-] No common admin panels found.", style="bold red")

def t_subdomain():
    console.print(Align.center(Panel("SUBDOMAIN HUNTER", style="bold yellow", expand=False)))
    domain = Prompt.ask("[bold cyan]Target Domain[/bold cyan]").replace("http://","").replace("https://","").split('/')[0]
    
    with console.status(f"[bold white]Querying logs for {domain}...") as status:
        try:
            # Using HackerTarget instead of crt.sh to avoid timeouts
            url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
            r = requests.get(url, timeout=15)
            if r.status_code == 200 and "error" not in r.text.lower():
                subs = list(set([line.split(',')[0] for line in r.text.split('\n') if line]))
                
                print()
                for sub in subs[:15]:
                    console.print(f"[+] {sub}", style="bold green")
                
                if len(subs) > 15:
                    filename = f"{domain}_subdomains.txt"
                    with open(filename, 'w') as f:
                        f.write("\n".join(subs))
                    console.print(f"\n[*] Total Discovered: [bold yellow]{len(subs)}[/bold yellow]", style="bold cyan")
                    console.print(f"[*] Complete list saved to: [bold white]{filename}[/bold white]", style="bold green")
            else:
                console.print("\n[!] No subdomains found or API rate limit reached.", style="bold red")
        except Exception as e:
             console.print(f"\n[!] Error: Connection timed out or failed.", style="bold red")

def t_waf():
    console.print(Align.center(Panel("WAF DETECTOR", style="bold yellow", expand=False)))
    target = Prompt.ask("[bold cyan]Target URL[/bold cyan]")
    if not target.startswith("http"): target = "http://" + target
    
    with console.status("[bold green]Analyzing HTTP Edge Signatures...") as status:
        try:
            r = requests.get(target, timeout=8)
            headers = str(r.headers).lower()
            waf_signatures = {
                'Cloudflare': ['cloudflare', '__cfduid', 'cf-ray'],
                'Sucuri': ['sucuri', 'x-sucuri'],
                'Akamai': ['akamai', 'x-akamai-'],
                'AWS WAF / CloudFront': ['x-amz-cf-id', 'awselb'],
                'Fastly': ['fastly', 'x-fastly'],
                'Incapsula/Imperva': ['incapsula', 'x-iinfo']
            }
            
            found_waf = None
            for waf_name, sigs in waf_signatures.items():
                if any(sig in headers for sig in sigs) or any(sig in str(r.cookies).lower() for sig in sigs):
                    found_waf = waf_name
                    break
            
            print()
            if found_waf:
                console.print(f"[!] EDGE/WAF DETECTED: [bold red]{found_waf}[/bold red]", style="bold white")
            else:
                console.print("[+] No known commercial WAF signature detected.", style="bold green")
        except:
            console.print("\n[!] Connection to target failed.", style="bold red")

def t_robots():
    console.print(Align.center(Panel("ROBOTS.TXT READER", style="bold yellow", expand=False)))
    target = Prompt.ask("[bold cyan]Target URL[/bold cyan]")
    if not target.startswith("http"): target = "http://" + target
    
    with console.status("[bold white]Fetching paths...[/bold white]"):
        try:
            r = requests.get(f"{target}/robots.txt", timeout=5)
            if r.status_code == 200:
                text = r.text
                if len(text) > 800:
                    console.print("\n[bold white]" + text[:800] + "\n\n... [TRUNCATED][/bold white]")
                    domain_clean = target.replace("https://", "").replace("http://", "").split('/')[0]
                    filename = f"{domain_clean}_robots.txt"
                    with open(filename, 'w') as f: f.write(text)
                    console.print(f"\n[*] Output was long. Full file saved to [bold green]{filename}[/bold green]")
                else:
                    console.print("\n[bold white]" + text + "[/bold white]")
            else:
                console.print(f"\n[!] robots.txt returned Status Code: {r.status_code}", style="bold red")
        except:
            console.print("\n[!] Connection Failed.", style="bold red")

# --- Main Engine ---
def main():
    insane_boot_sequence()
    
    while True:
        display_dashboard()
        show_menu()
        
        choice = Prompt.ask("\n[bold green]ENTER COMMAND[/bold green]")
        
        if choice in ['0', '00', '1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06', '7', '07', '8', '08', '9', '09', '10']:
            clear_screen()
        
        if choice in ['1', '01']: t_ping()
        elif choice in ['2', '02']: t_whois()
        elif choice in ['3', '03']: t_portscan() 
        elif choice in ['4', '04']: t_dns()
        elif choice in ['5', '05']: t_geoip()    
        elif choice in ['6', '06']: t_admin()    
        elif choice in ['7', '07']: t_subdomain()
        elif choice in ['8', '08']: t_waf()
        elif choice in ['9', '09']: t_robots()
        elif choice == '10':
            console.print("[bold green]Opening Developer YouTube Channel...[/bold green]")
            # Cross platform native browser open
            webbrowser.open("https://youtube.com/@termux2")
        elif choice in ['0', '00']:
            console.print("\n[bold red]TERMINATING CONNECTION...[/bold red]")
            time.sleep(1)
            clear_screen()
            sys.exit(0)
        else:
            console.print("[!] Invalid Module.", style="bold red")
            time.sleep(1)
            continue
            
        console.input("\n[bold yellow]Press Enter to return to Main Menu...[/bold yellow]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold red][!] CONNECTION SEVERED. EXITING...[/bold red]")
        sys.exit(0)
