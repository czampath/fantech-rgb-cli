import usb.core
import time

# Vendor and Product IDs of your Fantech RGB gaming keyboard
VENDOR_ID = 0x0C45  # Replace with your keyboard's vendor ID VID_0C45&PID_8006&MI_01&Col03
PRODUCT_ID = 0x8006  # Replace with your keyboard's product ID

# Find the device
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

# Check if the device is found
if device is None:
    print("Device not found.")
    exit()

# Set configuration
device.set_configuration()

# Define the list of setup data for the requests
setup_data_list_off = [
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0x0000,
        'wLength': 64,
        'data': bytes.fromhex('04ab0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0xa1,
        'bRequest': 0x01,
        'wValue': 0x0300,
        'wIndex': 0x0000,
        'wLength': 64
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('f269c4e1abdad6b84302d3a50b39bf713c26b39be9e3789d315c5571b9f824545a7cabca162c2ae2513331bb3d44b4479782614f919d31b70f3e3e0415a6d41b')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('04020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0xa1,
        'bRequest': 0x01,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('04130000000000001200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0xa1,
        'bRequest': 0x01,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('0000000000000000000000000000aa55000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('04020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    },
    {
        'bmRequestType': 0xa1,
        'bRequest': 0x01,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': bytes.fromhex('04f00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
    }
]

# Iterate through the setup data and send the requests
for setup_data in setup_data_list:
    try:
        bmRequestType = setup_data['bmRequestType']
        bRequest = setup_data['bRequest']
        wValue = setup_data['wValue']
        wIndex = setup_data['wIndex']
        wLength = setup_data['wLength']
        data = setup_data.get('data', None)



        # Use control transfer to send the request
        # device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, data, timeout=1000)
        # print("SET_REPORT request sent successfully.")
        
        # Use control transfer to send the request
        if data is not None:
            device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, data)
        else:
            device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
        
        print("SET_REPORT request sent successfully.")


    except usb.core.USBError as e:
        print("Error sending SET_REPORT request:", e)
