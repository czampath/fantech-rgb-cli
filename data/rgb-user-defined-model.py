# Define the list of setup data for the requests
setup_data_list_on = [
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0x0000,
        'wLength': 64,
        'data': '04ab0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '80e086718a5e75a9117c47f721a30b3be5e2e90c6d9c0907ae7eb067cbb4acd7935df3844a3c8775acb09c1f2fe6fd34894dacbd724ac868ab2eb4233f6576e9'
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '04020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '04130000000000001200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '01ff00000000000001100c000000aa550200ffff0000000001100c000000aa550300ffff0000000001100c000000aa55040000ff0000000001100c000000aa55' #67
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '050000ff0000000001100c000000aa55060000ff00000000011005000000aa550700ffff0000000000100c000000aa55080000ff0000000001100c000000aa55' #69
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '090000ff0000000001100c000000aa550a0000ff0000000001100c030000aa550b0000ff0000000001100c000000aa550c0000ff0000000001100c000000aa55' #71
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '0d0000ff0000000001100c000000aa550e0000ff0000000001100c000000aa550f0000ff0000000001100c000000aa55100000ff00000000011010000000aa55' #73
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '110000ff0000000001100c000000aa55120000ff0000000001100c000000aa55130000ff0000000001100c000000aa558000000000000000001000000000aa55' #75
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' #77
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' #79
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' #81
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '800000008026d8718000deff8000deff800000008000deff800000008000000080000000800000008000000080000000806ae5fe806ae5fe8000000080000000' #83
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '8000000080000000800000008000d8ff8000000080ff00008000000080ff00008000000080000000800000008000000080000000800000008000000080000000' #85
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '800000008000000080000000800000008000000080000000803ade00800000ff803ade008000000080ff0000800000008026d8718026d871800000008026d871' #87
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '8080008080800080800000008000000080000000800000008000000080000000800000ff800000ff800000ff800000ff8000000080ff000080ff00008026d871' #89
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '80000000800000008000000080000000800000008000000080000000800000008000000080ff00008026d871800000ff800000008026d8718026d8718026d871' #91
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '800000008000000080000000800000008000000080002525800000008000000080000000800000008000000080ff00008000000080ff000080ff000080000000' #93
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '80ecec00800000008000000080ff000080ff000080ff000080ff000080ff00008000000080000000800000008000000080000000800000008000000080000000' #95
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '8000000080000000800000008000000080000000800000008000000080000000800000008000000080000000806fe6ff80000000800000008000000080000000' #97
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '80000000800000008000000080000000800000008000000080000000800000008000000080000000800000008000000080000000800000008000000080000000' #99
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '8000000000000000001000000000aa55000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' #101
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '04020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' #103
    },
    {
        'bmRequestType': 0x21,
        'bRequest': 0x09,
        'wValue': 0x0300,
        'wIndex': 0,
        'wLength': 64,
        'data': '04f00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    }
]

# Extracting 'data' from each dictionary and creating a list
extracted_data = [data_dict['data'] for data_dict in setup_data_list_on]

count = len(extracted_data)
print("Count of items in the list:", count)
print(extracted_data)