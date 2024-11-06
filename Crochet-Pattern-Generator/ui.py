'''
author: Siena Landerkin
version: 1.0.1  September 2024
'''

import const

#supplies information about program and inputs at user's request
def help_menu():
    print(const.help_msg)
    
    quit = False
    query = "".casefold()
    
    while not quit:
        query = input("\n\tWhat do you need help with? ")
        if query ==  "cmd" or query == "read" or query == "pat":
            print('\033[1m' + const.help_responses[query] + '\033[0m')
            continue
        elif query == "quit":
            quit = True
    return "Done"