## Wireshark USB Traffic Capture Guide

1. **Install Wireshark with USBPcap:**
   Ensure you have Wireshark installed with USBPcap support. USBPcap enables Wireshark to capture USB traffic on Windows.

2. **Identify USBPcap Interface:**
   From the welcome page in Wireshark, identify the related USBPcap interface. This may appear as USBPcap1, USBPcap2, USBPcap3, and so on.

3. **Configure Interface Options:**
   Access the interface options and make the following adjustments:
   - Uncheck "Capture from all devices connected"
   - Check "Capture from newly connected devices"
   - Uncheck "Inject already connected devices descriptors into capture data"

4. **Import Colorizing Rule:**
   In the current folder, locate the file named `colorizing_rule` and import it into Wireshark. This file provides colorization to USB traffic, highlighting the beginning in red and the end in blue.

5. **Perform RGB Changes:**
   Use the manufacturer's application to make RGB changes. Ensure that at least one frame appears in red and another later frame appears in blue during the RGB change process.

6. **End Wireshark Capture:**
   Once the desired USB traffic has been captured, end the Wireshark capture session.

7. **Apply Filter:**
   Apply the following filter, replacing `<lowBound>` and `<UpperBound>` with appropriate frame numbers:

```
usb.bmRequestType == 0x21 && frame.number >= <lowBound> && frame.number <= <UpperBound> && usbhid.setup.wLength == 64
```

8. **Export Packet Dissections:**
Go to `File` > `Export Packet Dissections` > `As JSON` and save the file with the same name as the ID for this effect.

9. **HEX Data Extraction:**
With the Wireshark packet capture complete, proceed to extract HEX data for further analysis.

By following these steps, you can effectively capture and analyze USB traffic using Wireshark with USBPcap.
