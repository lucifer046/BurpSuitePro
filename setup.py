import os
import stat
import shutil
import time

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
DARK_GRAY = "\033[90m"
RESET = "\033[0m"

# Banner with developer attribution
banner = f"""
{CYAN}██████╗ ██╗   ██╗██████╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██╔══██╗
██████╔╝██║   ██║██████╔╝██████╔╝
██╔══██╗██║   ██║██╔══██╗██╔═══╝ 
██████╔╝╚██████╔╝██║  ██║██║     
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     {RESET}

{WHITE}  Burp Suite Professional Launcher - Automatic Setup Utility{RESET}
{DARK_GRAY}  Developer: github.com/lucifer046{RESET}
"""

def print_card(title, items):
    print(f"\n  {CYAN}┌── [ {title} ] ──────────────────────────────────────────{RESET}")
    print(f"  {CYAN}│{RESET}")
    for key, value, status in items:
        if status == "success":
            symbol = f"{GREEN}[✓]{RESET}"
        elif status == "info":
            symbol = f"{BLUE}[*]{RESET}"
        elif status == "warning":
            symbol = f"{YELLOW}[!]{RESET}"
        else:
            symbol = f"{RED}[✗]{RESET}"
        print(f"  {CYAN}│{RESET}  {symbol} {WHITE}{key:<16}{RESET} : {WHITE}{value}{RESET}")
    print(f"  {CYAN}│{RESET}")
    print(f"  {CYAN}└────────────────────────────────────────────────────────────{RESET}")

print(banner)
time.sleep(0.5)

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Step 1: Environment Verification
java_path = shutil.which("java")

if not java_path:
    print_card("Java Verification Failed", [
        ("Error", "Java runtime environment was not found", "fail"),
        ("Resolution", "Install OpenJDK 21 on your system", "warning"),
        ("Command", "sudo apt update && sudo apt install openjdk-21-jdk -y", "info")
    ])
    exit()

print_card("Step 1: Environment Verification", [
    ("Workspace Path", current_dir, "success"),
    ("Target Platform", "Linux (Debian/Kali)", "success"),
    ("Java Path", java_path, "success")
])
time.sleep(0.8)

# Step 2: Launcher Generation
burp_script_path = os.path.join(current_dir, "burp.sh")

burp_script = f"""#!/bin/bash

SCRIPT_DIR="{current_dir}"

"{java_path}" -jar "$SCRIPT_DIR/loader.jar"
"""

try:
    with open(burp_script_path, "w") as f:
        f.write(burp_script)

    st = os.stat(burp_script_path)
    os.chmod(burp_script_path, st.st_mode | stat.S_IEXEC)
    
    print_card("Step 2: Launcher Generation", [
        ("Script Target", burp_script_path, "success"),
        ("Permissions", "Executable (chmod +x)", "success"),
        ("Status", "Launcher script generated", "success")
    ])
except Exception as e:
    print_card("Launcher Generation Failed", [
        ("Error", str(e), "fail"),
        ("Status", "Could not write launcher script", "fail")
    ])
    exit()

time.sleep(0.8)

# Step 3: Desktop Integration
desktop_entry_path = os.path.expanduser(
    "~/.local/share/applications/burpsuitepro.desktop"
)
icon_path = os.path.join(current_dir, "logo.png")

desktop_entry = f"""[Desktop Entry]
Version=1.0
Type=Application
Name=Burp Suite Professional
Comment=Burp Suite Launcher
Exec={burp_script_path}
Icon={icon_path}
Terminal=false
Categories=Development;Security;
StartupNotify=true
"""

try:
    os.makedirs(os.path.dirname(desktop_entry_path), exist_ok=True)

    with open(desktop_entry_path, "w") as f:
        f.write(desktop_entry)

    os.chmod(desktop_entry_path, 0o755)
    
    print_card("Step 3: Desktop Integration", [
        ("Desktop Entry", desktop_entry_path, "success"),
        ("Custom Icon", icon_path, "success"),
        ("Categories", "Development;Security;", "success"),
        ("Status", "Application shortcut registered", "success")
    ])
except Exception as e:
    print_card("Desktop Integration Failed", [
        ("Error", str(e), "fail"),
        ("Status", "Shortcut registration incomplete", "warning")
    ])

time.sleep(0.8)

# Final Success Output
print(f"""
  {GREEN}════════════════════════════════════════════════════════════════{RESET}
                        {GREEN}INSTALLATION COMPLETE{RESET}
  {GREEN}════════════════════════════════════════════════════════════════{RESET}

  {WHITE}You can now launch the application in two ways:{RESET}

  {CYAN}Method 1{RESET} : Search for {WHITE}Burp Suite Professional{RESET} in your application menu.
  {CYAN}Method 2{RESET} : Run {WHITE}./burp.sh{RESET} from your terminal.

  {YELLOW}[!] Note{RESET}:
  Place your legitimate {WHITE}loader.jar{RESET} and {WHITE}burpsuite_pro.jar{RESET} files
  directly in the install directory before attempting to launch.

  {GREEN}[✓]{RESET} Setup completed successfully. Enjoy hacking!
""")
