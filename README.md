# WebRecon

![Language](https://img.shields.io/badge/Language-Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux_|_Windows_|_Termux-555555?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-0052cc?style=for-the-badge)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![Size](https://img.shields.io/badge/Repo_Size-Lightweight-orange?style=for-the-badge)

## Description

![Category](https://img.shields.io/badge/Category-Reconnaissance-blueviolet?style=flat-square)
![Type](https://img.shields.io/badge/Type-CLI_Tool-important?style=flat-square)

WebRecon is a lightweight, dependency-free reconnaissance framework designed for security professionals and ethical hackers. It is built entirely using Python's standard libraries, ensuring maximum portability across restricted environments like Termux, Windows CMD, and minimal Linux servers.

This tool eliminates the need for `pip install` or external package managers, focusing on core functionality and speed. It aggregates multiple reconnaissance techniques into a single, unified command-line interface.

## Functionality Overview

![Modules](https://img.shields.io/badge/Modules-9_Active-informational?style=flat-square)
![Networking](https://img.shields.io/badge/Networking-Socket_&_Subprocess-lightgrey?style=flat-square)
<img width="726" height="298" alt="image" src="https://github.com/user-attachments/assets/b0ece6db-18f0-4122-a6c7-631b21b8b9c4" />

| Module | Status | Description |
| :--- | :--- | :--- |
| **Ping Target** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Checks host availability with OS-adaptive ICMP packets. |
| **Whois Lookup** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Fetches domain registration and registrar data. |
| **Port Scanner** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Multi-threaded native Python scanner for critical ports. |
| **DNS Lookup** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Retrieves standard DNS records (A, MX, NS). |
| **GeoIP Tracker** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Locates target coordinates, ISP, and Region via API. |
| **Admin Finder** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Scans for administrative login paths (Handles 200/403 codes). |
| **Subdomain Hunter** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Enumerates subdomains via Certificate Transparency logs. |
| **WAF Detector** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Identifies Firewalls via HTTP Header analysis. |
| **Robots Reader** | ![Active](https://img.shields.io/badge/Status-Active-brightgreen) | Extracts and displays robots.txt content directly. |

## Installation

![Install](https://img.shields.io/badge/Install-Fast-green?style=flat-square)
![Dependencies](https://img.shields.io/badge/Dependencies-None-red?style=flat-square)

### Linux / Termux

No external libraries required.

1.  **Update Environment**
    ```bash
    pkg update && pkg upgrade -y
    ```
2.  **Install Python & Git**
    ```bash
    pkg install python git -y
    ```
3.  **Clone Repository**
    ```bash
    git clone https://github.com/trmxvibs/webrecon.git
    ```
4.  **Run Tool**
    ```bash
    cd webrecon
    python main.py
    ```

### Windows

1.  Download Python 3.x from [python.org](https://www.python.org/).
2.  Clone or Download this repository.
3.  Open Command Prompt (CMD) in the folder.
4.  Execute:
    ```cmd
    python main.py
    ```

<img width="1821" height="528" alt="image" src="https://github.com/user-attachments/assets/11a3f30f-2ea1-4378-8c07-027d9aa14312" />

## Usage

![Interface](https://img.shields.io/badge/Interface-CLI-black?style=flat-square)
![User](https://img.shields.io/badge/User-Root/Admin-red?style=flat-square)

Launch the tool and select a module by entering the corresponding index number.

```python
--- WebRecon Functional Toolkit ---
System: Linux | User: root

1. Ping Target
2. Whois Lookup
3. Port Scanner
4. DNS Lookup
5. GeoIP Tracker
6. Admin Finder
7. Subdomain Hunter
8. WAF/Header Detector
9. Robots.txt Reader
0. Exit
```

### Configuration
- Port Scanner: Configured to scan the top 15 most common ports for speed optimization.

- Timeouts: Network requests default to a 5-second timeout to prevent hanging.

- User-Agent: Uses a standard Mozilla user-agent to bypass basic bot filters.

## Legal Disclaimer
**This tool is developed for educational purposes and authorized security testing. The author makes no warranties regarding the tool's performance or suitability for any specific purpose.**
**Do not scan targets without explicit permission. The user is solely responsible for compliance with all applicable local, state, and federal laws.**

Author & Support
YouTube: [Termux Vibes](https://youtube.com/@termux2)













