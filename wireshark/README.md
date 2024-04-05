## Wireshark USB Traffic Capture Guide

**Note:** This guide is specifically tailored for FANTECH RGB devices that are non-AuraSync-compatible.

1. **Install Wireshark with USBPcap:**
   Ensure you have Wireshark installed with USBPcap support. USBPcap enables Wireshark to capture USB traffic on Windows.

2. **Import Colorizing Rule:**
   In the current folder, locate the file named `colorizing_rule` and import it into Wireshark. This file provides colorization to USB traffic, highlighting the beginning of the transmission in **<font color="red">RED</font>** and the end in **<font color="dodgerblue">BLUE</font>**.

3. **Identify USBPcap Interface:**
   From the welcome page in Wireshark, identify the related USBPcap interface. This may appear as USBPcap1, USBPcap2, USBPcap3, and so on. (Unplug and re-plug the device to notice the changes in interface)

4. **Configure Interface Options:**
   Access the interface options and make the following adjustments:
   - Uncheck "Capture from all devices connected"
   - Check "Capture from newly connected devices"
   - Uncheck "Inject already connected devices descriptors into capture data"

5. **Initiate Capture:**
   Open the USBPCap interface.
   Re-plug the USB device to start capturing packets.

6. **Perform RGB Changes:**
   Use the manufacturer's application and perform the desired RGB effect. Once RGB effect has been commenced, wireshark will be capturing packets. Please ensure at least one frame appears in **<font color="red">RED</font>**, followed by a frame that appears in **<font color="dodgerblue">BLUE</font>** during capture.

7. **End Wireshark Capture:**
   Once the desired USB traffic has been captured (frame in **<font color="dodgerblue">BLUE</font>**), end the Wireshark capture session.

8. **Apply Filter:**
   Apply the following filter; Replace `<lowBound>` with a frame number less than of the **<font color="red">RED</font>** frame and `<UpperBound>` with a frame number higher than of the **<font color="dodgerblue">BLUE</font>** frame.

```
usb.bmRequestType == 0x21 && frame.number >= <lowBound> && frame.number <= <UpperBound> && usbhid.setup.wLength == 64
```

9. **Export Packet Dissections:**
Go to `File` > `Export Packet Dissections` > `As JSON` and save the file with the same name as the ID to be used for this effect in the future.

10. **Next Step - HEX Extraction:**
With the Wireshark packet capture complete, proceed to HEX - Extraction for data refinements.

By following these steps, you can effectively capture and analyze USB traffic using Wireshark with USBPcap.
