# Burp Suite Professional Launcher

<p align="center">
  <img src="logo.png" alt="Burp Suite Pro Launcher Logo" width="128" height="128">
</p>

An automated, lightweight utility to configure, integrate, and launch Burp Suite Professional on Kali Linux and Debian-based systems. This tool streamlines launcher script generation, Java environment detection, and desktop environment menu integration.

<p align="center">
  <a href="#detailed-installation-guide"><b>Quick Installation Guide</b></a> •
  <a href="#requirements-and-preparation"><b>System Requirements</b></a> •
  <a href="#troubleshooting-guide"><b>Troubleshooting Help</b></a>
</p>

---

## Key Features

* **Automated Script Generation**: Creates a robust, relocatable launcher script (`burp.sh`) automatically.
* **Java Runtime Detection**: Scans and verifies local Java installations to ensure compatibility.
* **Kali and GNOME Desktop Integration**: Adds Burp Suite Professional to your system application menus.
* **Custom Branding**: Seamlessly integrates custom application icons (`logo.png`) into desktop files.
* **Zero Manual Path Mapping**: Calculates absolute system paths dynamically during setup.
* **Simplified Installer**: Run one script to initialize, verify, and register the application.

---

## Supported Environments

* **Operating System**: Kali Linux, Debian, or other GNOME-based Debian derivatives.
* **Runtime Environment**: Java Runtime Environment (OpenJDK 21 recommended).
* **Dependencies**: Python 3.x (for setup and integration automation).

---

## Repository Structure

```text
BurpSuitePro/
├── setup.py             # Automates launcher generation and desktop integration
├── loader.jar           # Required launcher helper (User-provided)
├── burpsuite_pro.jar    # Burp Suite Professional application binary (User-provided)
├── logo.png             # Icon for application menu integration
└── README.md            # Project documentation and guide
```

---

## Requirements and Preparation

### 1. Python Environment

Ensure Python 3 is installed:

```bash
python3 --version
```

If Python 3 is missing, install it using:

```bash
sudo apt update
sudo apt install python3 -y
```

### 2. Java Development Kit (JDK 21)

Burp Suite Professional requires a compatible Java environment.

Verify your installed Java version:

```bash
java --version
```

If Java is not installed, set up OpenJDK 21:

```bash
sudo apt update
sudo apt install openjdk-21-jdk -y
```

If OpenJDK 21 is installed but is not set as the default active runtime, configure it using the system alternative selection utility:

```bash
sudo update-alternatives --config java
```

Select the menu path corresponding to OpenJDK 21 from the presented list.

---

## Detailed Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/lucifer046/BurpSuitePro.git
```

### Step 2: Navigate to the Directory

```bash
cd BurpSuitePro
```

### Step 3: Add Required Binaries

To complete the setup, place your legally obtained Java binaries directly inside the repository directory:
* `loader.jar`
* `burpsuite_pro.jar`

Ensure `logo.png` remains in the folder to serve as the launcher's desktop icon.

> [!IMPORTANT]
> Do not upload, commit, or distribute licensed or proprietary JAR files (`loader.jar` or `burpsuite_pro.jar`) to public repositories.

> [!TIP]
> **Getting the Latest Version of Burp Suite**:
> If you want to run the latest version of Burp Suite Professional, follow these steps:
> 1. Visit the official PortSwigger Releases page: https://portswigger.net/burp/releases
> 2. Download the latest release of the Professional version in **JAR** format.
> 3. Copy the downloaded JAR file directly into the repository workspace.
> 4. Rename this file to exactly: `burpsuite_pro.jar`
> 5. Complete the license activation manually upon first execution.

---

## Running the Automated Setup

Execute the installation script:

```bash
python3 setup.py
```

The script will automatically perform the following steps:
1. Detect and validate the Java runtime path.
2. Build the executable wrapper script (`burp.sh`).
3. Set execution permissions for the runner scripts.
4. Construct a custom desktop entry file (`burpsuitepro.desktop`).
5. Register the application with the desktop environment.

---

## Execution Methods

Once the installation is complete, you can launch the application in two ways:

### Method 1: System Application Menu

1. Open your system's application launcher.
2. Search for `Burp Suite Professional`.
3. Click the icon to start.

### Method 2: Command Line Terminal

Run the generated shell script from the repository folder:

```bash
./burp.sh
```

---

## System Integration Paths

The installer registers files to the following paths on your system:

* **Launcher Executable Wrapper**: `burp.sh` (Within your cloned repository directory)
* **Desktop Application Entry**: `~/.local/share/applications/burpsuitepro.desktop`

---

## Maintenance and Updates

### Rebuilding the Launcher

If you move the repository folder, update Java, or replace the JAR binaries, regenerate the launcher by running the installer again:

```bash
python3 setup.py
```

### Uninstallation

To remove desktop menu integration and clean up the repository:

1. Delete the desktop entry file:

   ```bash
   rm ~/.local/share/applications/burpsuitepro.desktop
   ```

2. Remove the project directory:

   ```bash
   rm -rf BurpSuitePro
   ```

---

## Troubleshooting Guide

### Error: Java Not Found or Incorrect Version Active

Ensure that OpenJDK 21 is correctly installed and configured in your system's PATH variable:

```bash
sudo apt update && sudo apt install openjdk-21-jdk -y
```

If OpenJDK 21 is installed but another Java version remains selected as the default, configure OpenJDK 21 as active:

```bash
sudo update-alternatives --config java
```

### Error: Permission Denied on Launch

If the generated wrapper script cannot be executed, manually grant execute permissions:

```bash
chmod +x burp.sh
```

### Issue: Desktop Icon is Missing

If the application menu does not display the icon immediately, rebuild the desktop database:

```bash
update-desktop-database ~/.local/share/applications
```

Alternatively, log out and log back into your desktop session to refresh the menu system.

---

## Installer Process Preview

Here is an example output from running the setup script successfully:

```text
██████╗ ██╗   ██╗██████╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██╔══██╗
██████╔╝██║   ██║██████╔╝██████╔╝
██╔══██╗██║   ██║██╔══██╗██╔═══╝ 
██████╔╝╚██████╔╝██║  ██║██║     
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     

  Burp Suite Professional Launcher - Automatic Setup Utility
  Developer: github.com/lucifer046

  ┌── [ Step 1: Environment Verification ] ──────────────────────
  │
  │  [✓] Workspace Path   : /home/kali/BurpSuitePro
  │  [✓] Target Platform  : Linux (Debian/Kali)
  │  [✓] Java Path        : /usr/bin/java
  │
  └────────────────────────────────────────────────────────────

  ┌── [ Step 2: Launcher Generation ] ──────────────────────────
  │
  │  [✓] Script Target    : /home/kali/BurpSuitePro/burp.sh
  │  [✓] Permissions      : Executable (chmod +x)
  │  [✓] Status           : Launcher script generated
  │
  └────────────────────────────────────────────────────────────

  ┌── [ Step 3: Desktop Integration ] ──────────────────────────
  │
  │  [✓] Desktop Entry    : /home/kali/.local/share/applications/burpsuitepro.desktop
  │  [✓] Custom Icon      : /home/kali/BurpSuitePro/logo.png
  │  [✓] Categories       : Development;Security;
  │  [✓] Status           : Application shortcut registered
  │
  └────────────────────────────────────────────────────────────

  ════════════════════════════════════════════════════════════════
                        INSTALLATION COMPLETE
  ════════════════════════════════════════════════════════════════

  You can now launch the application in two ways:

  Method 1 : Search for Burp Suite Professional in your application menu.
  Method 2 : Run ./burp.sh from your terminal.

  [!] Note:
  Place your legitimate loader.jar and burpsuite_pro.jar files
  directly in the install directory before attempting to launch.

  [✓] Setup completed successfully. Enjoy hacking!
```

---

## Legal and Security Disclaimer

This software utility is designed solely for automation, deployment customization, and workflow enhancement purposes on local systems. It does not contain, distribute, or license proprietary software or activation components. Users must secure appropriate authorization, licenses, and rights to run Burp Suite Professional.

---

## Reference Layout

```text
screenshots/
├── installer.png
├── kali-menu.png
└── burp-running.png
```
