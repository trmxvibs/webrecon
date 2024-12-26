# WebRecon Toolkit 🕵️‍♂️🔍

Welcome to WebRecon Toolkit! This tool provides various network reconnaissance functionalities including Ping Test, Whois Lookup, NSLookup, Port Scanning using Nmap, and Banner Grabbing.

## Prerequisites 🛠️

Before you start using WebRecon Toolkit, you need to install the following packages on your system:

- `whois`
- `dnsutils`
- `nmap`
- `netcat-openbsd`

You can install these packages using the following commands:
### Kali Linux
```sh
sudo apt-get update
sudo apt-get install whois dnsutils nmap netcat-openbsd
```
### Termux 
```sh
pkg update && pkg upgrade -y && pkg install -y whois dnsutils nmap netcat-openbsd
```

# Features 🌟
## Ping Test 🏓

### Ping a domain or IP
### Continuous Ping Test
### Ping with specific packet size
### test Result with google.com
```sh
Enter domain or IP to ping: google.com
PING google.com (142.250.77.46) 56(84) bytes of data.
64 bytes from bom07s26-in-f14.1e100.net (142.250.77.46): icmp_seq=1 ttl=112 time=44.9 ms
64 bytes from bom07s26-in-f14.1e100.net (142.250.77.46): icmp_seq=2 ttl=112 time=72.1 ms
64 bytes from bom07s26-in-f14.1e100.net (142.250.77.46): icmp_seq=3 ttl=112 time=53.5 ms
64 bytes from bom07s26-in-f14.1e100.net (142.250.77.46): icmp_seq=4 ttl=112 time=61.2 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
rtt min/avg/max/mdev = 44.951/57.975/72.181/10.017 ms
```

# Whois Lookup 🔎

### Domain Whois
### IP Whois
### Whois with full output
### test Result with google.com
```sh
Domain Name: GOOGLE.COM
   Registry Domain ID: 2138514_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.markmonitor.com
   Registrar URL: http://www.markmonitor.com
   Updated Date: 2019-09-09T15:39:04Z
   Creation Date: 1997-09-15T04:00:00Z
   Registry Expiry Date: 2028-09-14T04:00:00Z
   Registrar: MarkMonitor Inc.
   Registrar IANA ID: 292
   Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
   Registrar Abuse Contact Phone: +1.2086851750
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Domain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited
   Domain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited
   Domain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited
   Name Server: NS1.GOOGLE.COM
   Name Server: NS2.GOOGLE.COM
   Name Server: NS3.GOOGLE.COM
   Name Server: NS4.GOOGLE.COM
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2024-12-26T05:22:41Z <<<

For more information on Whois status codes, please visit https://icann.org/epp

NOTICE: The expiration date displayed in this record is the date the
registrar's sponsorship of the domain name registration in the registry is
currently set to expire. This date does not necessarily reflect the expiration
date of the domain name registrant's agreement with the sponsoring
registrar.  Users may consult the sponsoring registrar's Whois database to
view the registrar's reported date of expiration for this registration.

Domain Name: google.com
Registry Domain ID: 2138514_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.markmonitor.com
Registrar URL: http://www.markmonitor.com
Updated Date: 2024-08-02T02:17:33+0000
Creation Date: 1997-09-15T07:00:00+0000
Registrar Registration Expiration Date: 2028-09-13T07:00:00+0000
Registrar: MarkMonitor, Inc.
Registrar IANA ID: 292
Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
Registrar Abuse Contact Phone: +1.2086851750
Domain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)
Domain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)
Domain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)
Domain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)
Domain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)
Domain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)
Registrant Organization: Google LLC
Registrant State/Province: CA
Registrant Country: US
Registrant Email: Select Request Email Form at https://domains.markmonitor.com/whois/google.com
Admin Organization: Google LLC
Admin State/Province: CA
Admin Country: US
Admin Email: Select Request Email Form at https://domains.markmonitor.com/whois/google.com
Tech Organization: Google LLC
Tech State/Province: CA
Tech Country: US
Tech Email: Select Request Email Form at https://domains.markmonitor.com/whois/google.com
Name Server: ns3.google.com
Name Server: ns4.google.com
Name Server: ns1.google.com
Name Server: ns2.google.com
DNSSEC: unsigned
URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/
>>> Last update of WHOIS database: 2024-12-26T05:20:12+0000 <<<

For more information on WHOIS status codes, please visit:
  https://www.icann.org/resources/pages/epp-status-codes

If you wish to contact this domain’s Registrant, Administrative, or Technical
contact, and such email address is not visible above, you may do so via our web
form, pursuant to ICANN’s Temporary Specification. To verify that you are not a
robot, please enter your email address to receive a link to a page that
facilitates email communication with the relevant contact(s).

Web-based WHOIS:
  https://domains.markmonitor.com/whois

If you have a legitimate interest in viewing the non-public WHOIS details, send
your request and the reasons for your request to whoisrequest@markmonitor.com
and specify the domain name in the subject line. We will review that request and
may ask for supporting documentation and explanation.

The data in MarkMonitor’s WHOIS database is provided for information purposes,
and to assist persons in obtaining information about or related to a domain
name’s registration record. While MarkMonitor believes the data to be accurate,
the data is provided "as is" with no guarantee or warranties regarding its
accuracy.

By submitting a WHOIS query, you agree that you will use this data only for
lawful purposes and that, under no circumstances will you use this data to:
  (1) allow, enable, or otherwise support the transmission by email, telephone,
or facsimile of mass, unsolicited, commercial advertising, or spam; or
  (2) enable high volume, automated, or electronic processes that send queries,
data, or email to MarkMonitor (or its systems) or the domain name contacts (or
its systems).

MarkMonitor reserves the right to modify these terms at any time.

By submitting this query, you agree to abide by this policy.

MarkMonitor Domain Management(TM)
Protecting companies and consumers in a digital world.

Visit MarkMonitor at https://www.markmonitor.com
Contact us at +1.8007459229
In Europe, at +44.02032062220
--
```


# NSLookup 🖥️

### Basic NSLookup
### Reverse DNS Lookup
### Query specific DNS record (A, MX, CNAME, etc.)
### test Result with google.com (TXT record)
```sh

NSLookup Options:
1. Basic NSLookup
2. Reverse DNS Lookup
3. Query specific DNS record (A, MX, CNAME, etc.)
4. Return to Main Menu
Choose an option: 3
Enter domain: google.com
Enter DNS record type (e.g., A, MX, CNAME): txt
;; Truncated, retrying in TCP mode.
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
google.com      text = "google-site-verification=4ibFUgB-wXLQ_S7vsXVomSTVamuOXBiVAzpR5IZ87D0"
google.com      text = "MS=E4A68B9AB2BB9670BCE15412F62916164C0B20BB"
google.com      text = "google-site-verification=wD8N7i1JTNTkezJ49swvWW48f8_9xveREV4oB-0Hf5o"
google.com      text = "apple-domain-verification=30afIBcvSuDV2PLX"
google.com      text = "globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8="
google.com      text = "docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e"
google.com      text = "cisco-ci-domain-verification=479146de172eb01ddee38b1a455ab9e8bb51542ddd7f1fa298557dfa7b22d963"
google.com      text = "v=spf1 include:_spf.google.com ~all"
google.com      text = "docusign=1b0a6754-49b1-4db5-8540-d2c12664b289"
google.com      text = "facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95"
google.com      text = "google-site-verification=TV9-DBe4R80X4v0M4U_bd_J9cpOJM0nikft0jAgjmsQ"
google.com      text = "onetrust-domain-verification=de01ed21f2fa4d8781cbc3ffb89cf4ef"
```
# Port Scanning (Nmap) ⚡
### Root User Commands
```sh
--- Root User Commands ---
1. Full Scan (All ports and services)
2. Vulnerability Scan (Find vulnerabilities)
3. OS Detection (Operating system details)
4. Aggressive Scan (Comprehensive scan)
5. UDP Scan (Scan for UDP services)
6. Script Scan (Run custom Nmap scripts)
7. Firewall Evasion (Bypass firewalls)
8. Stealth Scan (Avoid detection)
9. Traceroute Analysis (Identify route to target)

```
### Non-Root User Commands
```sh


--- Non-Root User Commands ---
1. Quick Scan (Fast scan for common ports)
2. Service Version Scan (Detect service versions)
3. Host Discovery (Find live hosts)
4. Port Scan (Scan specific ports)
5. Top Ports Scan (Scan the most used ports)
6. Ping Sweep (Ping multiple hosts)
7. No DNS Resolution (Skip DNS resolution)
8. Scan a Specific Range (Define a port range)
9. Scan a List of Targets (File input)

```



# Banner Grabbing 🚩


# Usage 🚀
To run the WebRecon Toolkit, simply execute the script:
```sh
python3 webrecon_advanced.py
```

# Main Menu 📋
## The main menu provides the following options:
![image](https://github.com/user-attachments/assets/825e0890-a724-443d-bafa-724a77f98dda)


##  Each main menu option leads to a sub-menu with specific functionalities.
```sh
Ping Test Options 🏓
Ping a domain or IP
Continuous Ping Test
Ping with specific packet size
Return to Main Menu
Whois Lookup Options 🔎
Domain Whois
IP Whois
Whois with full output
Return to Main Menu
NSLookup Options 🖥️
Basic NSLookup
Reverse DNS Lookup
Query specific DNS record (A, MX, CNAME)
Return to Main Menu
Nmap Scanning Menu ⚡
Root User Commands
Non-Root User Commands
Back to Main Menu
Root User Commands 🔒
Full Scan (All ports and services)
Vulnerability Scan (Find vulnerabilities)
OS Detection (Operating system details)
Aggressive Scan (Comprehensive scan)
UDP Scan (Scan for UDP services)
Script Scan (Run custom Nmap scripts)
Firewall Evasion (Bypass firewalls)                  
Stealth Scan (Avoid detection)
Traceroute Analysis (Identify route to target)
Non-Root User Commands 🔓
Quick Scan (Fast scan for common ports)
Service Version Scan (Detect service versions)
Host Discovery (Find live hosts)
Port Scan (Scan specific ports)
Top Ports Scan (Scan the most used ports)
Ping Sweep (Ping multiple hosts)
No DNS Resolution (Skip DNS resolution)
Scan a Specific Range (Define a port range)
Scan a List of Targets (File input)
```
# Author ✍️
Lokesh Kumar

# YouTube  [Termux Vibes](https://www.youtube.com/@TermuxVibes)



# License 📜
## This project is licensed under the MIT License.
