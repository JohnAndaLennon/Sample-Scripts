#################################################################################################################
# HIDE AND SEEK                                                                                                 #
# This project performs a rousing game of Hide and Seek. The Player chooses a hiding spot while the seeker      #
# attempts to find them within 2-3 chances. The number of chances and locations are chosen randomly, and        #
# the AI will exclude options they already searched. If not found, the Player wins!                             #
# Version: 2                                                                                                    #
# Version Date: 12/8/2024                                                                                       #
# Creator: John Andalora                                                                                        #
#################################################################################################################

#!/usr/bin/env python3
import random

def hideSeek():
    #Initialization of game assets
    foundBool = 1 #1 if not found, 0 if found
    seeker = -1 #Choice that NPC makes for seeking
    scriptTalk = -1 #For additional lines of speaking

    #Dictionary for hiding spots
    hidingDict = {
        1: "Under the bed.",
        2: "In the closet.",
        3: "Behind the drapes.",
        4: "Under the bedsheets.",
        5: "Under a lamp shade",
        6: "In the pillow case",
        7: "Behind the door",
        8: "Under the carpet"
    }

    #Dictionary for additional lines of dialogue
    scriptDict = {
        0: "Let's see, where to try next?...",
        1: "* Scratches head *",
        2: "Could've sworn you would have been there...",
        3: "You picked a good spot!",
        4: "I'm getting warmer!"
    }

    #Dictionary for rewards for player if they win
    winDict = {
        0: "a slightly used Lollipop!",
        1: "a sandwich bag filled with beans!",
        2: "an iPod shuffle with no charger!",
        3: "a bright, shiny nickel!"
    }

    #Dictionary for rewards seeker can win
    loseDict = {
        0: "$20 and some ice cream.",
        1: "your left shoe.",
        2: "your iPhone 14 with a cracked screen.",
        3: "the shirt off your back."
    }

    #Setup numbers for Dictionaries
    dictLength = len(hidingDict)
    scriptNum = len(scriptDict) * 2
    winNum = len(winDict)
    #loseNum = len(loseDict) (((Not currently used, should wins and losses be of different sizes it would make sense)))
    rangeRandom = random.randrange(2,5)

    #Setup of the game and options available
    print("Here are your spot choices:")

    #Runs through hidingDict to list choices
    for i,j in hidingDict.items():
        print(i,j)

    #Input for where the Player will hide
    hidingSpot = input("Choose your hiding Spot: ")

    #This allows the hidingSpot to be checked for a digit and compared to the items in the Dictionary Keys
    if hidingSpot.isdigit() and int(hidingSpot) in hidingDict.keys():
        print("You hid " + hidingDict[int(hidingSpot)])

        #Iterates through 2-5 times (number of attempts to seek the player)
        for x in range(rangeRandom):

            #Makes sure that the AI chooses a number inside the options available
            while seeker not in hidingDict.keys():
                seeker = random.randrange(1,dictLength)

            #Shows the player where the AI seeked
            print("I searched " + hidingDict[seeker])

            #If Player is found, breaks the for
            if hidingSpot == str(seeker):
                foundBool = 0
                break
            hidingDict.pop(seeker)

            #If not the last loop, sets a random number and if it equals a key it prints the script
            if x + 1 != rangeRandom:
                scriptTalk = random.randint(0, scriptNum)
                if scriptTalk in scriptDict:
                    print(scriptDict[scriptTalk])

    #Any input not within the available options
    else:
        print("You didn't choose a hiding spot.")
        foundBool = 0

    #Endgame content, random int for winning or losing
    prize = random.randint(0,winNum - 1)
    #Test for if the player was found
    if (foundBool == 0):
        print("I found you!")
        print("You gave the seeker " + loseDict[prize])
    else:
        print("You win! I didn't find you!")
        print("You received " + winDict[prize])

def main():
    playAgain = 'yes'
    print("Hello! Welcome to Hide and Seek!")


    #While for the game to run, allows player to input option
    while playAgain == 'yes':
        hideSeek()
        print("Would you like to play again? (Type \'yes\' to play again)")
        playAgain = input().lower()
    print("Goodbye! Have a good day!")


if __name__=="__main__":
    main()