import usb.core
import usb.util

# USB device Vendor ID and Product ID (replace with your keyboard's IDs)
VENDOR_ID = 0x0C45  # Replace with your keyboard's vendor ID VID_0C45&PID_8006&MI_01&Col03
PRODUCT_ID = 0x8006  # Replace with your keyboard's product ID

# Find USB device
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device is None:
    raise ValueError("Device not found")

# Set configuration (if needed)
device.set_configuration()

# USB endpoint for data transfer
endpoint = device[0][(0, 0)][0]

# USB packet capture
while True:
    try:
        # Read USB packet
        data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        # Process captured packet here
        print("Captured packet:", data)
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue
