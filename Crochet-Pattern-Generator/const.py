'''
author: Siena Landerkin
version: 1.0.1  September 2024
'''

welcome_msg = (
    "\n\n\t-~-~-~-Welcome to the Crochet Ball Pattern Generator-~-~-~-\n\n"
    '\033[1m' + "\n\t\tNote: this program uses US terms!" + '\033[0m'
    "\n\t\tGeneric Crochet Ball Size Options:\n\n\t\t\tLarge (max 36 st)\n\t\t\tMedium (max 30 st)\n\t\t\tSmall (max 24 st)"
    '\033[1m' + "\n\n\tFor help with the program or understanding the pattern, enter 'help'" + '\033[0m'
    )
    
help_msg = (
    "\n\n\t-~-~-~-Help Menu-~-~-~-\n\n"
    "\n\tFor an explanation of commands and values, enter 'cmd'"
    "\n\tFor pattern help, enter 'read'"
    "\n\tFor an explanation of the different patterns, enter 'pat'"
    "\n\tTo exit the help menu, enter 'quit'"
    )
    
cmd = (
    "\n\n\t--------------------------------------------------------------------------------------------"
    "\n\tMax Stitch Count:"
    "\n\t\tThis describes the circumference of your ball at its largest point. This is measured "
    "\n\t\tin terms of stitches rather than a conventional measurement such as inches or "
    "\n\t\tcentimeters. This allows the pattern to apply to any weight of yarn and hook size."
    "\n\t\t\t- Value entered numerically: e.g. 36"
    "\n\n\tBall Size:"
    "\n\t\tThis describes preset size options if you do not have a specific size in mind. The "
    "\n\t\tterms \"large\", \"medium\", and \"small\" are arbitrarily defined and serve as" 
    "\n\t\tbasic starting points rather than firm guidlines on size."
    "\n\t\t\t- Value entered alphabetically (capitalization does not matter): e.g. large"
    "\n\t--------------------------------------------------------------------------------------------"
    )
    
pattern_notes = (
    "\n\n\t--------------------------------------------------------------------------------------------"
    "\n\n\t This adaptive crochet pattern assumes you know the following basic crochet techniques:"
    "\n\t\tMagic Ring\n\t\tSingle Crochet\n\t\tIncrease\n\t\tDecrease"
    "\n\t- Your project will be worked \"in the round\", so the use of stitch markers is helpful "
    "\n\t  (but not required)."
    "\n\t- Instructions inside of [square brackets] are to be repeated as indicated by the pattern."
    "\n\t- If you prefer, you can chain 2 and slip stitch to the first chain instead of using a "
    "\n\t  magic ring."
    "\n\t- Invisible decreases are recommended (but not required) for amigurumi as they look more "
    "\n\t  seamless."
    "\n\t--------------------------------------------------------------------------------------------"
    )
    
alg_notes = (
    "\n\n\t--------------------------------------------------------------------------------------------"
    "\n\n\t- This program uses two separate algorithms -- basic and shift\n"
    "\n\t- The basic algorithm produces a typical, straightforward crochet pattern for a ball. The "
    "\n\t  \"shift\" algorithm, however, uses incremental shifts to offset the placement of increases. "
    "\n\t  While the basic algorithm works just fine, it will produce noticeable \"points\" because "
    "\n\t  every increase is made at the same interval in every round. This is especially noticeable "
    "\n\t  when creating a circle of single crochets, or when you are in the \"circle\" phase of the "
    "\n\t  pattern.\n\n\tThe shift algorithm corrects this issue by shifting the repeated "
    "\n\t  increases/decreases in every single even-numbered round of increases/decreases. "
    "\n\t  The difference is particularly noticable with smaller weights of yarn, and may not be very "
    "\n\t  noticable when using bulky or velvet yarns.\n"
    "\n\t- This difference is also useful if you intend to use this program as a reference to "
    "\n\t  crochet circles using single crochets or half-double crochets."
    "\n\t--------------------------------------------------------------------------------------------"
    )     
    
pattern_header = (
    "\n\n\t------------------------------------------------------------------------------------------"
    '\033[1m' + "\n\n\t\tTerms (US):"  + '\033[0m'
    "\n\n\t\t\tmagic ring*\n\t\t\tsingle crochet -- sc\n\t\t\tincrease -- inc\n\t\t\tdecrease -- dec"
    "\n\n\t\t\t*alternative methods like the"
    "\n\t\t\tchain ring can be used here!"
    )
    
options = ["help", "basic", "shift"]

sizes = { 'large':36 , 'medium':30 , 'small':24 }  

help_responses = {
    'cmd': cmd,
    'read': pattern_notes,
    'pat': alg_notes,
}