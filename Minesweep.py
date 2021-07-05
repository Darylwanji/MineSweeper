import numpy as np

class board:
	sboard_wm = []
	board_w_mask = []
	""" Size E.g 8x8 """

	def __init__(self,size):
		self.board_wm = np.zeros(size)
		self.board_w_mask = np.full(size,"X")
		
	def showboard_wm(self):
		""" Shows the board without mask """
		print(self.board_wm)
	def showboard_m(self):
		""" Shows the board with mask """
		print(self.board_w_mask)
	