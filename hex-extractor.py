import os
import json

input_json_file_path = r"hex\raw-data\sample.json"

init_comm = '04ab0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
end_comm = '04f00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

def extract_data_from_packets(packets):
    # Extracting 'data_fragment' from each dictionary and creating a list
    extracted_data = []

    # Flag to indicate whether to start/stop extraction
    start_extraction = False
    for packet in packets:

        data_fragment = packet['_source']['layers']['Setup Data']['usb.data_fragment']
        formatted_data = data_fragment.replace(':', '')

        # Start extraction when specific data is encountered
        if formatted_data == init_comm:
            start_extraction = True
        
        # Append data to the list if extraction flag is True
        if start_extraction:
            extracted_data.append(formatted_data)

        # Stop extraction when specific data is encountered
        if formatted_data == end_comm:
            start_extraction = False
    
    return extracted_data

def update_or_create_output_json(input_json_file_path, extracted_data):
    # Extract the filename from the provided input file path
    filename = os.path.splitext(os.path.basename(input_json_file_path))[0]

    # Define the output JSON file path
    output_json_file_path = "hex\data.json"

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

    print("Data extracted and saved successfully to:", output_json_file_path)

with open(input_json_file_path, 'r') as file:
    packets = json.load(file)

extracted_data = extract_data_from_packets(packets)

preCount = len(packets)
postCount = len(extracted_data)

if(postCount == 24):
    print('Extraction successful')
    print("pre-extractions frame count: ", preCount)
    print("post-extractions frame count: ", postCount)
    update_or_create_output_json(input_json_file_path, extracted_data)
else:
    print('ERROR: Extraction failed!')
    print("pre-extractions frame count: ", preCount)
    print("post-extractions frame count: ", postCount)
    print("first byte = ",extracted_data[0])
    print("last byte = ",extracted_data[-1])