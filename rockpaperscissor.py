# ### rock paper scisoor game
# rps = input('enter a value:\n')
# print(rps)

import sys
import random
from enum import Enum

class rps(Enum):
    ROCK = 1
    PAPER = 2
    SCI = 3

playerchoice = input('enter  \n 1 for rock \n 2 for paper \n 3 for scissors: \n\n')

p = int(playerchoice)

if  p < 1 or p > 3:
    sys.exit("enter 1, 2 or 3, nothing else accepted")

computerchoice = random.choice("1 2 3")
computer = float(computerchoice)

print("")

print(" you chose " + str(rps(p)).replace('rps.' , '') + "." )
print("computer's choice " + str(rps(computer)).replace('rps.','') + "." ) 

if playerchoice == 1 and computerchoice == 3:
    print("you win")
elif playerchoice == 2 and computerchoice == 1:
    print("you win")
elif playerchoice == 3 and computerchoice == 2:
    print("you win")
elif playerchoice == computerchoice :
    print("tie")
else:
    print("computer wins")
    
    