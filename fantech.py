import usb.core
import os
import json
from constants.hex_constants import ControlDataPoint, SpecialDataPoint
from constants.hid_constants import HID_Data

# Vendor and Product IDs of your Fantech RGB gaming keyboard
VENDOR_ID = 0x0C45  # Replace with your keyboard's vendor ID
PRODUCT_ID = 0x8006  # Replace with your keyboard's product ID

# Find the device
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

# Check if the device is found
if device is None:
    print("Device not found.")
    exit()

# Set configuration
device.set_configuration()


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