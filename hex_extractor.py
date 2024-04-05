import os
import json
import logging
from constants.hex_constants import ControlDataPoint, SpecialDataPoint

# Configure logging to write messages at the INFO level or higher to both the console and a file
logging.basicConfig(level=logging.INFO, filename='fantech.log', format='%(levelname)s - %(message)s')

raw_data_file_path = r"hex\raw-data\default.json"
isStaticEffect = False
frameThreashold = 24

def extract_data_from_packets(packets):
    global frameThreashold
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
                frameThreashold += 1

        # Stop extraction when specific data is encountered
        if formatted_data == ControlDataPoint.END_COMM:
            start_extraction = False
    
    return extracted_data

def update_or_create_output_json(input_json_file_path, extracted_data):
    # Extract the filename from the provided input file path
    filename = os.path.splitext(os.path.basename(input_json_file_path))[0]
    logging.info("Extracting %s",filename)
    # Define the output JSON file path
    output_json_file_path = "data.json"

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
    data["OPTILUXS_MK884"]["hex"]["rgb"]["fx"][filename] = extracted_data

    # Save the updated data to the output JSON file
    with open(output_json_file_path, 'w') as file:
        json.dump(data, file)

    logging.info("Data extracted and saved successfully")

def remove_node_from_json(input_json_file_path):
    # Extract the filename from the provided input file path
    filename = os.path.splitext(os.path.basename(input_json_file_path))[0]
    logging.info("Removing node for %s", filename)
    
    # Define the output JSON file path
    output_json_file_path = "data.json"

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

# with open(raw_data_file_path, 'r') as file:
#     packets = json.load(file)

# extracted_data = extract_data_from_packets(packets)

# preCount = len(packets)
# postCount = len(extracted_data)

# if(postCount == frameThreashold):
#     print('Extraction successful')
#     print("pre-extractions frame count: ", preCount)
#     print("post-extractions frame count: ", postCount)
#     update_or_create_output_json(raw_data_file_path, extracted_data)
# else:
#     print('ERROR: Extraction failed!')
#     print("pre-extractions frame count: ", preCount)
#     print("post-extractions frame count: ", postCount)
#     print("first byte = ",extracted_data[0])
#     print("last byte = ",extracted_data[-1])

def extract(input_file_path):
    global frameThreashold

    with open(input_file_path, 'r') as file:
        pData = json.load(file)

    extracted_data = extract_data_from_packets(pData)

    preCount = len(pData)
    postCount = len(extracted_data)

    if(postCount == frameThreashold):
        logging.info('Extraction successful')
        logging.debug("pre-extractions frame count: %d", preCount)
        logging.debug("post-extractions frame count: %d", postCount)
        update_or_create_output_json(input_file_path, extracted_data)
    else:
        logging.error('Extraction failed!')
        logging.debug("pre-extractions frame count: %d", preCount)
        logging.debug("post-extractions frame count: %d", postCount)
        logging.debug("first byte = %s",extracted_data[0])
        logging.debug("last byte = %s",extracted_data[-1])