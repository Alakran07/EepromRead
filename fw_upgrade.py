#This is a simulation of FW upgrade process
# FW is going to be upgraded based on a Dic
#
#
#--------------------------------------------------
from time import sleep

sim_file = "fw_sim_file.txt"

fw_new_version = '1.8'

#Reading PWR FW version
def fw_version_read(filename):
    with open(filename,'r') as f:
        for line in f:
           # print(line)
            if "FW VERSION" in line:
                current_version = line.split(":")[-1].strip()
    return current_version

def sim_write_prom(file_sim_name):
    print("Simulation of FW upgrade")
    with open(file_sim_name, 'r') as f:
        for line in f:
            print(line)
            sleep(1)

def fw_upgrade(file_sim_name, filename, current_version, new_version):
    new_version = float(new_version)
    current_version = float(current_version)
    if new_version > current_version:
        print("DEBUG:FW UPGRADE REQUIRED ..")
        with open(filename, 'r') as f:
            data = f.readlines()
        sim_write_prom(file_sim_name)
        with open(filename, 'w') as f:
            for line in data:
                if "FW VERSION" in line:
                    new_line = "FW VERSION:{}\n".format(str(new_version))
                    print("DEBUG: New Line: new_line {}".format(new_line))
                    f.write(new_line)
                else:
                    f.write(line)
    else:
        print("DEBUG:FW UP TO DATE ..")
    pass
def dump_eeprom(filename):
    with open(filename, 'r') as f:
        for line in f:
            print(line)