import sys, json

menu = {}
# format(', '.join(list(menu.keys())))

""" This runs the code
    ip is the IP/hostname of the server
"""
def main(ip, user):
    with open("/Users/daboss/Documents/Git/SmartHome/PhilipsHue/options.json",
        encoding='utf-8-sig') as json_file:
        text = json_file.read()
        menu = json.loads(text)
    lvl1=list(menu.keys())
    print(lvl1)
    choice = ""
    while choice.lower() != 'exit':
        print("Enter exit to quit.")
        # read std input for light, groups, config, schedules, scenes, rules, sensors
        ### MAKE A FUCNTION TO DO THIS, SUPPLY IT LIST TO PRINT OUT AND CHECK
        ### IF RESPONSE IS IN LIST.
        while True:
            print("Choose one of the following: {}".format(', '.join(lvl1)))
            choice = input("Enter choice:")
            if choice.lower() in lvl1:
                return;
        lvl2 = options(choice)


""" This function will print the options available to the user for their
    current screen.
    Returns path to requested item as a string """
def options(keyword):
    # /api/key/lvl1/lvl2/etc.
    # Light: list, pick number, state:on, state:bri, name, getStats
    # getStats: return state:on, state:bri, state:alert, type, name, modelid,
    # uniqueid
    if keyword.lower() == "light":
        path = "/lights"

    # Groups: list, pick room, roomStats
    # roomStats: list name, lights, type, class

    # config: info, time, version, whitelist
    # info: name, bridgeid, mac, dhcp, ipaddress, netmask, gateway, proxy
    # time: UTC, localtime, timezone
    # version: modelid, datastoreversion, swversion, apiversion
    # whitelist: id:name, id:last use date

    # schedules: list

    # scenes: list, id:info
    # list: id:name for each scene
    # id:info: name, lights, owner, locked, lastupdated

    # rules: list

    # sensors: list, #:state, #:config, info
    # info: name, type, modelid, manufacturername, swversion

    # resourcelinks: list

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Missing arguments, ./prog.py addr username")
    #     exit()
    # else:
    #     ip=sys.argv[1]
    #     user=sys.argv[2]
    #     main(ip, user)
    main("", "")
