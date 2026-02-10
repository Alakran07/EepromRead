# This code reads eeprom from eeprom.txt file
# and add PWR firmware version.
# TODO: Add eeprom informaiton validation, match model with power
#
#-----------------------------------------------------------------
from products import products_dicts as product_info

def read_prom (filename, field_name):
    found = False
    with open(filename, 'r') as f:
        for line in f:
            print(line)
            if field_name in line:
                print("{}: FIELD EXIST".format(field_name))
                found = True
                return found
    print("{}: FIELD DOES NOT EXIST TO BE ADDED".format(field_name))
    return found

def write_prom (filename, data):
    print("Debug: Writing {}.".format(data))
    with open(filename, 'a') as f:
        f.write(data)

def add_fw_ver(file_name_eeprom,field_name,file_value):
    new_value = field_name + ":" + file_value
    write_prom(file_name_eeprom,new_value)

