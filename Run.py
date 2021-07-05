from Minesweep import board
from pprint import pprint
import os

def menu(): 
	pprint(" Welcome to Cheeper !")

menu()

size = [int(i) for i in input("Please Enter size: ").split()]
level = int(input("Please Enter a level : "))

MS = board(size,level)

MS.showboard_m()
os.system('clear')
MS.showboard_wm()
