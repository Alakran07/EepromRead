EEPROM Firmware Upgrade Simulator
This project is a Python-based simulation of an industrial firmware upgrade process for Power Supply Units (PSUs). It automates the verification of EEPROM data structures and handles logic-based version patching.
Features
EEPROM Validation: Scans the eeprom.txt file to ensure the required "FW VERSION" field exists.

Automatic Field Insertion: Dynamically appends missing data fields to the EEPROM file if they are absent.

Smart Version Comparison: Compares the current firmware version against a target version (e.g., 1.5 vs 1.8) and triggers an upgrade only when necessary.

In-Place File Updating: Replaces specific lines in the text-based storage without corrupting existing hardware metadata.

Modular Architecture: Separates file I/O, upgrade logic, and system orchestration for high maintainability.

Project Structure
main.py: The central controller (orchestrator) that manages the workflow.

eeprom_read.py: Library for reading, validating, and initializing the EEPROM file.

fw_upgrade.py: Contains the logic for version comparison and the simulation of the flashing process.

eeprom.txt: A mock storage file representing the PSU hardware memory.

How to Run
Ensure you have Python 3.x installed.

Clone this repository:

Bash
git clone https://github.com/Alakran07/EepromRead.git
Run the simulation:

Bash
python main.py

Example Output
Plaintext
System Starting...
--- Phase 1: Validating EEPROM Structure ---
EEPROM structure is valid.

--- Phase 2: Checking for Upgrades ---
DEBUG: Upgrading 1.5 -> 1.8
Simulation of FW upgrade...
Success!
System Shutdown.
