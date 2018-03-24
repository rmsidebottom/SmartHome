""" Philips Hue Bridge program to access the API remotely and manage it through
    a more user friendly interface.

    Author: Ryan Sidebottom
    Date: 3/24/17
"""

import sys, json

# menu = {}
body = {}
# format(', '.join(list(menu.keys())))

"""
    At the last level in a dictionary, only values can be changed.
    Get data to be changed (in json format), get request type, or do nothing
"""
def lastlLevel(dct):
    print("Options: get, put, post, exit")
    act = input("Enter choice: ")

    while act.lower() != 'exit':
        if act.lower() == 'get':
            req = ''
            return req
        elif act.lower() == 'put':
            # ask user for data to put
            while True:
                print("Enter data in json format to be changed.")
                print("Values that can be changed are: \
                    {}".format(', '.join(list(dct))))
                data = input("Enter data: ")
                if type(data) == type(dct):
                    body = data
                    return ''
        elif act.lower() == 'post':
            req = ''
            break
        # they enter something that isn't valid
        else:
            print("Options: get, put, post, exit")
            act = input("Enter choice: ")
    return ''

""" Function takes a list of options, displays them, accepts input and
    checks the input to ensure it is valid.
    Sets the global variable body to the body of the message if there is a body.
    Returns the path of the object.
    Returns '' when exit pressed.
"""
def runList(keyDict):
    choice=""
    req=""
    opts=['get', 'put', 'post', 'deeper', 'exit']
    subDict = False
    for val in keyDict.values():
        # print("{0}:::{1}".format(type(val), val))
        if type(val) == type({"":""}):
            subDict = True

    if not subDict:
        # call function to get values or set get request, can't traverse any
        # lower
        req = lastlLevel(keyDict)
        return req

    while choice.lower() != 'exit':
        # prompt user to pick one of the keys at the nth level
        print("Choose one of the following: {}".format(', '.join(list(keyDict.keys()))))
        choice = input("Enter choice:")
        if choice.lower() in [x.lower() for x in list(keyDict.keys())]:
            #prompt user for actions based on choice
            print("What do you want to do with {0}: {1}".format(choice,
            ', '.join(opts)))
            act = input("Enter choice: ")

            # loop through options, prompt user to finish the options
            # options refer to all of the keys at the current level
            # one request to the API can support changing multiple values
            while act.lower() != 'exit':
                if act.lower() == 'get':
                    req = choice
                    return req
                elif act.lower() == 'put':
                    # ask user for data to put
                    # TODO
                    break
                elif act.lower() == 'post':
                    req = ''
                    return req
                elif act.lower() == 'deeper':
                    # go one level deeper
                    req = choice +"/"+ runList(keyDict[choice])
                    return req
                else:
                    print("Please choose an option {1}".format(choice, \
                    ', '.join(opts)))
                    act = input("Enter choice: ")
                # prompt the user for any other values here
                print("What do you want to do with {0}: {1}".format(choice,
                ', '.join(opts)))
                act = input("Enter choice: ")

    return req;

""" This runs the code
    ip: the IP/hostname of the server
    user: username required for access to the API
"""
def main(ip, user):
    with open("/Users/daboss/Documents/Git/SmartHome/PhilipsHue/options.json",
        encoding='utf-8-sig') as json_file:
        text = json_file.read()
        menu = json.loads(text)
    print(type(menu))
    req = "/api/"+user+"/"+runList(menu)

    print(req)

if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Missing arguments, ./prog.py addr username")
    #     exit()
    # else:
    #     ip=sys.argv[1]
    #     user=sys.argv[2]
    #     main(ip, user)
    main("", "")
