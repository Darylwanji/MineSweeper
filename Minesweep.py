import numpy as np


class board:
	sboard_wm = []
	board_w_mask = []
	MINES = '**'
	FLAGS = 'P'

	""" Size E.g 8x8 """
	def __init__(self,size, level):
		self.board_wm = np.full(size,"--")

		# Creating Mines
		for i in range(level):
			x = np.random.randint(0,size[0])
			y = np.random.randint(0,size[0])

			if self.board_wm[x][y] == self.MINES:
				x = np.random.randint(0,size[0])
				y = np.random.randint(0,size[0])
				self.board_wm[x][y] = self.MINES
			else: 
				self.board_wm[x][y] = self.MINES


		self.board_w_mask = np.full(size," ")
		
	def showboard_wm(self):
		""" Shows the board without mask """
		print(self.board_wm)

	def showboard_m(self):
		""" Shows the board with mask """
		print(self.board_w_mask)
	