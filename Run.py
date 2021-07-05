from Minesweep import board

def menu(): 
	print(" Welcome to Cheeper !")

menu()

size = [int(i) for i in input("Please Enter size: ").split()]

MS = board(size)

MS.showboard_m()
MS.showboard_wm()