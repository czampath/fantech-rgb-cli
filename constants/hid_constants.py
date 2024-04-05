class HID_Data:
    wIndex = 0
    wLength = 64
    wValue = 0x0300

    class BRequest:
        GET_REPORT = 0x01
        SET_REPORT = 0x09

    class BmRequestType:
        TO_DEVICE = 0x21
        TO_HOST = 0xa1