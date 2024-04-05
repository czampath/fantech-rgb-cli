import usb.core
import os
import json
from constants.hex_constants import ControlDataPoint, SpecialDataPoint
from constants.hid_constants import HID_Data
from config import get_vendor_product_ids, update_vendor_product_ids

# Vendor and Product IDs of your Fantech RGB gaming keyboard

isDeviceInfoFound = False
device = None

# config the device
while(not isDeviceInfoFound):
    result = get_vendor_product_ids()
    if result is not None:
        vendor_id_str, product_id_str = result
        # Convert hexadecimal strings to integers
        vendor_id = int(vendor_id_str, 16)
        product_id = int(product_id_str, 16)
        device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
        isDeviceInfoFound = True
    else:
        print("WARNING: Device Info not found. Applying auto-configs for OPTILUXS_MK884")
        update_vendor_product_ids('0x0C45','0x8006')

# Check if the device is found
if device is None:
    print("Device not found.")
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
        print("Available FX:")
        for effect in effects:
            print(effect)
        
        return effects

    except FileNotFoundError:
        print("Error: JSON file not found at the specified path.")

def get_value_from_json(filename):
    # Define the output JSON file path
    output_json_file_path = "data.json"

    # Check if the JSON file exists
    if not os.path.exists(output_json_file_path):
        print("ERROR: JSON file does not exist.")
        return None

    # Load existing data from the output JSON file
    with open(output_json_file_path, 'r') as file:
        data = json.load(file)

    # Check if the node exists for the given filename
    if filename in data.get("OPTILUXS_MK884", {}).get("hex", {}).get("rgb", {}).get("fx", {}):
        return data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"][filename]
    else:
        print("ERROR: FX not recognized")
        return None


# list available FX
# list_filenames_from_json()

# Draw FX directly form the data.json
filename = "sample" # Name of the effect to activate
value = get_value_from_json(filename)
dataLen = len(value)
if value is not None:
    print("Retrieved", filename, "with", dataLen ,"frames")

# Iterate through the setup data and send the requests
for data in value:
    try:
        hexData = bytes.fromhex(data)
        device.ctrl_transfer(HID_Data.BmRequestType.TO_DEVICE, HID_Data.BRequest.SET_REPORT, HID_Data.wValue, HID_Data.wIndex, hexData)
        
        # Send GET_REPORT after each data point
        if data in [SpecialDataPoint.static, ControlDataPoint.INIT_COMM, ControlDataPoint.END_TRANSFER, ControlDataPoint.BEGIN_DATA_TRANSFER]:
            device.ctrl_transfer(HID_Data.BmRequestType.TO_HOST, HID_Data.BRequest.GET_REPORT, HID_Data.wValue, HID_Data.wIndex, HID_Data.wLength)

    except usb.core.USBError as e:
        print("Error sending SET_REPORT request:", e)

print("Request sent successfully.")