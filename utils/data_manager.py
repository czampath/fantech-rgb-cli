import os
import json
import logging
from config import DATA_STORE

logging.basicConfig(level=logging.INFO, filename='fantech.log', format='%(levelname)s - %(message)s')

def get_effect_by_name(filename):
    global DATA_STORE
    # Define the output JSON file path
    output_json_file_path = DATA_STORE

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

def get_all_effects_data():
    global DATA_STORE
    json_file_path = DATA_STORE

    if not os.path.exists(json_file_path):
        # If data.json file is not found, create it and copy data from data.py
        try:
            from data import data
            with open(json_file_path, 'w') as file:
                json.dump(data, file)
        except ImportError:
            logging.error("data.py not found. Unable to create data.json.")
            return []

    try:
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        # Extract filenames from the JSON data
        effects = data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"].keys()
        
        # Print the list of filenames
        logging.debug("Available FX:")
        for effect in effects:
            logging.debug(effect)
        
        return effects

    except FileNotFoundError:
        logging.error("JSON file not found at the specified path.")
        return []

def store_fx(fx_name, extracted_data):
    global DATA_STORE
    # Extract the filename from the provided input file path
    # filename = os.path.splitext(os.path.basename(input_json_file_name))[0]
    logging.info("Storing [%s] Data",fx_name)
    # Define the output JSON file path
    output_json_file_path = DATA_STORE

    # Create the data structure if it doesn't exist
    if not os.path.exists(output_json_file_path):
        data = {
            "OPTILUXS_MK884": {
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

    # Update or add the extracted data for the filename
    data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"][fx_name] = extracted_data

    # Save the updated data to the output JSON file
    with open(output_json_file_path, 'w') as file:
        json.dump(data, file)

    logging.info("Data stored successfully")

def remove_fx_from_data(input_json_file_path):
    global DATA_STORE
    # Extract the filename from the provided input file path
    filename = os.path.splitext(os.path.basename(input_json_file_path))[0]
    logging.info("Removing node for %s", filename)
    
    # Define the output JSON file path
    output_json_file_path = DATA_STORE

    # Check if the output JSON file exists
    if os.path.exists(output_json_file_path):
        # Load existing data from the output JSON file
        with open(output_json_file_path, 'r') as file:
            data = json.load(file)

        # Remove the node corresponding to the filename
        if "OPTILUXS_MK884" in data and "hex" in data["OPTILUXS_MK884"] and "rgb" in data["OPTILUXS_MK884"]["hex"] and "fx" in data["OPTILUXS_MK884"]["hex"]["rgb"] and filename in data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"]:
            del data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"][filename]
            logging.info(f"Node for '{filename}' removed successfully.")

            # Save the updated data to the output JSON file
            with open(output_json_file_path, 'w') as file:
                json.dump(data, file)
        else:
            logging.error(f"Node for '{filename}' not found.")
    else:
        logging.error("Output JSON file not found.")