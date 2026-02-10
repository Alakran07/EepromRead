
import eeprom_add_field as reader
import fw_upgrade as upgrader
from products import products_dicts as product_info
target_file = None
new_version = None

def product_selector(product):
    if product == "pwr":
        target_file = "ps_eeprom.txt"
        new_version = "1.88"
    if product == "fan":
        target_file = "fan_eeprom.txt"
        new_version = "1.99"
    return target_file, new_version

def start_firmware_process(product,target_file,new_version):
    field_name = 'FW VERSION'
    #print(product_info[product])
    fw_ver = product_info[product][field_name]
    print("--- Phase 1: Validating EEPROM Structure ---")
    # Check if FW VERSION field exists
    if not reader.read_prom(target_file, field_name):
        print("Field missing. Adding FW VERSION field...")
        reader.add_fw_ver(target_file, fw_ver)  # Default start version
    else:
        print("EEPROM structure is valid.")

    print("\n--- Phase 2: Checking for Upgrades ---")
    # Get the current version from the file
    current_ver = upgrader.fw_version_read(target_file)

    # Run the upgrade logic
    upgrader.fw_upgrade(sim_file, target_file, current_ver, new_version)


if __name__ == "__main__":
    sim_file = "fw_sim_file.txt"
    print("System Starting...")
    target_file, new_version = product_selector("pwr")
    start_firmware_process("pwr", target_file, new_version)
    target_file, new_version = product_selector("fan")
    start_firmware_process("fan", target_file,new_version)
    print("System Shutdown.")