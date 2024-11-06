'''
author: Siena Landerkin
version: 1.0.1  September 2024
'''

import time
import algorithm1
import algorithm2
import ui
import const
    
def main():
    print(const.welcome_msg)
    
    validInput = False
    stchMax = "".casefold()
    initInput = "".casefold()
    
    #checks what user wants to do
    while initInput not in const.options:
        initInput = input("\n\tTo begin, enter your designed pattern type (i.e. 'basic' or 'shift'): ")
        if initInput == "help":
            ui.help_menu()
            initInput = ""
        elif initInput not in const.options:
            print('\033[1m' + "\n\t\tPlease enter a valid command!" + '\033[0m')
            continue
    
    #check for proper ball size
    while not validInput:
        stchMax = input(
        "\n\n\tPlease input your desired ball size, or custom size of max circumference (multiple of 6)."
        "\n\t~Note! Smallest ball size is 18!~ "
        )
        
        if (stchMax.isnumeric()):
            if int(stchMax) < 18:
                print('\033[1m' + "\t\tError: Enter a value of at least 18!" + '\033[0m')
                continue
            elif int(stchMax) % 6 != 0:
                print('\033[1m' + "\t\tError: Enter a multiple of 6!" + '\033[0m')
                continue
            elif int(stchMax) > 1000:
                print('\033[1m' + "\t\tError: Enter a smaller value!" + '\033[0m')
                continue
        elif stchMax not in const.sizes:
            print('\033[1m' + "\t\tError: Not a valid input! If using defined sizes, \n\t\tplease enter only small, medium, or large.\n" + '\033[0m')
            continue
        
        validInput = True
          
    print(const.pattern_header)
    
    #starts program based on user input
    if initInput == "basic":   
        if stchMax.isnumeric():
            print(algorithm1.beginning)
            algorithm1.pattern(int(stchMax), int(stchMax)//2, 1, 3, algorithm1.pattern_string)
        else:
            print(algorithm1.beginning)
            algorithm1.pattern(const.sizes[stchMax], const.sizes[stchMax]//2, 1, 3, algorithm1.pattern_string)
    elif initInput == "shift":
        if stchMax.isnumeric():
            print(algorithm2.beginning)
            algorithm2.pattern(int(stchMax), int(stchMax)//2, 2, 4, algorithm2.even_round, algorithm2.odd_round)
        else:
            print(algorithm2.beginning)
            algorithm2.pattern(const.sizes[stchMax], const.sizes[stchMax]//2, 2, 4, algorithm2.even_round, algorithm2.odd_round)
        
if __name__ == '__main__':
    main()
    













