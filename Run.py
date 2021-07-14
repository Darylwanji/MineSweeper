from Minesweep import board
from Minesweep import Player
import os

def menu(): 
	print(" Welcome to Cheeper !")

menu()

P1 = Player(input("Please Enter your name : "))
P1.who()

MS = board([int(i) for i in input("Please Enter size -  \n E.g 4 4, 8 8 or 16 16 \n Size : ").split()],
	int(input("Please Enter a level -  \n 6 < level > size^2 \n Level : ")))

#os.system('clear')
MS.showboard_wm()
