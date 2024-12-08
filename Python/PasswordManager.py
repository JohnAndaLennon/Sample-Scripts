#########################################################################
# Password Generator Project:                                           #
#  Generates a default password using upper, lower, numbers and symbols.#
#  I hope to make this a command that can accept arguments and adjust   #
#  as needed to be able to generate different passwords in different    #
#  use cases.                                                           #
# Version: 1.0                                                          #
# Revision Date: 05/31/2024                                             #
# Creator: John Andalora                                                #
#########################################################################

#!/usr/bin/env python

#Imports
import string
import random
import argparse

#Establishes the Parser for creating additional arguments
parser = argparse.ArgumentParser(description="Creates a random password, can add numbers and symbols")

#Adding Arguments
parser.add_argument('-l','--length', type=int, help='Determines length of password, default is 12')
parser.add_argument('-n','--number', help='Adds numbers, default uses no numbers', action="store_true")
parser.add_argument('-s','--symbol', help='Adds symbols, default uses no symbols', action="store_true")

# Setting up Variables for the arguments
args= parser.parse_args()
len_arg = args.length
num_arg = args.number
sym_arg = args.symbol

if len_arg is None:
    passwordSize = 12
else:
    passwordSize = len_arg

password = ""

if num_arg is True and sym_arg is True:
    for i in range(passwordSize):
        password = password + random.choice(string.ascii_letters + string.digits + string.punctuation)
elif num_arg is True and sym_arg is False:
    for i in range(passwordSize):
        password = password + random.choice(string.ascii_letters + string.digits)
elif num_arg is False and sym_arg is True:
    for i in range(passwordSize):
        password = password + random.choice(string.ascii_letters + string.punctuation)
else:
    for i in range(passwordSize):
        password = password + random.choice(string.ascii_letters)

print(password)