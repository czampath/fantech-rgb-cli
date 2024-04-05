import usb.core
import os
import json
import logging
import datetime
from constants.hex_constants import ControlDataPoint, SpecialDataPoint
from constants.hid_constants import HID_Data
from config import get_vendor_product_ids, update_vendor_product_ids
from hex_extractor import do_extract

# Configure logging to write messages at the INFO level or higher to both the console and a file
logging.basicConfig(level=logging.INFO, filename='fantech.log', format='%(levelname)s - %(message)s')

# Create a stream handler to log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)

logging.info("Execution started at %s", datetime.datetime.now())

# auto-config flags
is_device_info_found = False 
config_attempt_limit = 2
config_attempts = 0
device = None

# desired RGB effect
effect_name = "default"

# config the device
while(not is_device_info_found):
    result = get_vendor_product_ids()
    if result is not None:
        vendor_id_str, product_id_str = result
        # Convert hexadecimal strings to integers
        vendor_id = int(vendor_id_str, 16)
        product_id = int(product_id_str, 16)
        device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
        is_device_info_found = True
    else:
        config_attempts += 1
        if config_attempts >= config_attempt_limit:
            logging.error("FATAL: Maximun auto-configuration attempts reached")
            exit()
        logging.warning("Applying auto-configs for OPTILUXS_MK884")
        update_vendor_product_ids('0x0C45','0x8006')

# Check if the device is found
if device is None:
    logging.error("FATAL: Device not found.")
    exit()

# Set configuration
device.set_configuration()

def list_effects_from_json():
    json_file_path = "data.json"
    try:
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Extract filenames from the JSON data
        effects = data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"].keys()
        
        # Print the list of filenames
        logging.info("Available FX:")
        for effect in effects:
            logging.debug(effect)
        
        return effects

    except FileNotFoundError:
        logging.error("JSON file not found at the specified path.")

def get_hex_from_json(filename):
    # Define the output JSON file path
    output_json_file_path = "data.json"

    # Check if the JSON file exists
    if not os.path.exists(output_json_file_path):
        logging.error("JSON file does not exist.")
        return None

    # Load existing data from the output JSON file
    with open(output_json_file_path, 'r') as file:
        data = json.load(file)

    # Check if the node exists for the given filename
    if filename in data.get("OPTILUXS_MK884", {}).get("hex", {}).get("rgb", {}).get("fx", {}):
        return data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"][filename]
    else:
        logging.error("FX not recognized")
        return None

# Check if Effects are available
effects = list_effects_from_json()
if not effects:
    logging.warning("No FX found, falling back to default FX")
    alternate_data_path = r"hex\raw-data\default.json"
    effect_name = "default"
    do_extract(alternate_data_path)

# Draw FX form the data.json
hex_array = get_hex_from_json(effect_name)
if hex_array is not None:
    data_len = len(hex_array)
    logging.info("Retrieved %s with %d frames", effect_name, data_len)
else:
    logging.error("FATAL: Failed to retrieve effect %s", effect_name)
    exit()

# Iterate through the setup data and send the requests
for data in hex_array:
    try:
        hex_data = bytes.fromhex(data)
        device.ctrl_transfer(HID_Data.BmRequestType.TO_DEVICE, HID_Data.BRequest.SET_REPORT, HID_Data.wValue, HID_Data.wIndex, hex_data)
        
        # Send GET_REPORT after each data point
        if data in [SpecialDataPoint.static, ControlDataPoint.INIT_COMM, ControlDataPoint.END_TRANSFER, ControlDataPoint.BEGIN_DATA_TRANSFER]:
            device.ctrl_transfer(HID_Data.BmRequestType.TO_HOST, HID_Data.BRequest.GET_REPORT, HID_Data.wValue, HID_Data.wIndex, HID_Data.wLength)

    except usb.core.USBError as e:
        logging.error("Sending request failed")
        logging.debug(e)

logging.info("Request sent successfully.")

logging.info("Execution ended at %s", datetime.datetime.now())