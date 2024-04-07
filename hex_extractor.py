import os
import json
import logging
from constants.hex_constants import ControlDataPoint, SpecialDataPoint
from config import DATA_STORE

# Configure logging to write messages at the INFO level or higher to both the console and a file
logging.basicConfig(level=logging.INFO, filename='fantech.log', format='%(levelname)s - %(message)s')

frame_threashold = 24

def extract_data_from_packets(packets):
    global frame_threashold
    # Extracting 'data_fragment' from each dictionary and creating a list
    extracted_data = []

    # Flag to indicate whether to start/stop extraction
    start_extraction = False
    for packet in packets:

        data_fragment = packet['_source']['layers']['Setup Data']['usb.data_fragment']
        formatted_data = data_fragment.replace(':', '')

        logging.debug(formatted_data)

        # Start extraction when specific data is encountered
        if formatted_data == ControlDataPoint.INIT_COMM:
            start_extraction = True
        
        # Append data to the list if extraction flag is True
        if start_extraction:
            extracted_data.append(formatted_data)
            
            found = any(formatted_data == getattr(SpecialDataPoint, attr) for attr in dir(SpecialDataPoint) if not attr.startswith('__'))
            if found:
                logging.info("Special data Point detected")
                frame_threashold += 1

        # Stop extraction when specific data is encountered
        if formatted_data == ControlDataPoint.END_COMM:
            start_extraction = False
    
    return extracted_data

def update_or_create_output_json(fx_name, extracted_data):
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

def remove_node_from_json(input_json_file_path):
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

def do_extract(input_file_path):
    global frame_threashold

    with open(input_file_path, 'r') as file:
        extracted_data = json.load(file)

    filename = os.path.splitext(os.path.basename(input_file_path))[0]

    logging.info("Initiating Data extraction : [%s]", filename)
    extracted_data = extract_data_from_packets(extracted_data)

    pre_count = len(extracted_data)
    post_count = len(extracted_data)

    if(post_count == frame_threashold):
        logging.info('Data extracted successfully')
        logging.debug("pre-extractions frame count: %d", pre_count)
        logging.debug("post-extractions frame count: %d", post_count)
        update_or_create_output_json(filename, extracted_data)
    else:
        logging.error('Extraction failed!')
        logging.debug("pre-extractions frame count: %d", pre_count)
        logging.debug("post-extractions frame count: %d", post_count)
        logging.debug("first byte = %s",extracted_data[0])
        logging.debug("last byte = %s",extracted_data[-1])