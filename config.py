import os
import json
import logging

# Configure logging to write messages at the INFO level or higher to both the console and a file
logging.basicConfig(level=logging.INFO, filename='fantech.log', format='%(levelname)s - %(message)s')


def update_vendor_product_ids(vendor_id, product_id):

    # Define the output JSON file path
    output_json_file_path = "data.json"

    # Check if data.json exists
    if not os.path.exists(output_json_file_path):
        # Create the data structure with vendor and product IDs
        data = {
            "OPTILUXS_MK884": {
                "VENDOR_ID": "your_vendor_id_here",
                "PRODUCT_ID": "your_product_id_here",
                "hex": {
                    "rgb": {
                        "fx": {}
                    }
                }
            }
        }
    else:
        # Load existing data from the output JSON file
        with open(output_json_file_path, 'r') as file:
            data = json.load(file)

    # Update/add the device info
    data["OPTILUXS_MK884"]["VENDOR_ID"] = vendor_id
    data["OPTILUXS_MK884"]["PRODUCT_ID"] = product_id

    # Save the updated data to the output JSON file
    with open(output_json_file_path, 'w') as file:
        json.dump(data, file)

    logging.info("Device info saved successfully")

def get_vendor_product_ids():
    config_file_path = "data.json"
    if not os.path.exists(config_file_path):
        logging.error("Config file does not exist. Please update the vendor and product IDs if auto-configuration fails")
        return None
    
    with open(config_file_path, 'r') as file:
        data = json.load(file)
    
    if "OPTILUXS_MK884" not in data:
        logging.error("Vendor and Product IDs not found in the config file.")
        return None
    
    vendor_id = data["OPTILUXS_MK884"].get("VENDOR_ID")
    product_id = data["OPTILUXS_MK884"].get("PRODUCT_ID")
    
    if vendor_id is None or product_id is None:
        logging.error("Vendor or Product ID is missing in the config file.")
        return None
    
    return vendor_id, product_id
