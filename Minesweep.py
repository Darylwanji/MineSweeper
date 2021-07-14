import numpy as np

class Player: 
	name = " "
	score = 0
	def __init__(self,name):
		self.name = name
	def who(self):
		print(" Player : " + self.name)
	def update_score(self):
		self.score =+ 2

class board:
	sboard_wm = []
	board_w_mask = []
	size = None
	MINES = '**'
	EMPTY = '--'
	FLAGS = 'P'

	""" Size E.g 8x8 """
	def __init__(self,size, level):
		self.board_wm = np.full(size,"--")
		self.size = size

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
		self.numbering_mines()
		
	def showboard_wm(self):
		""" Shows the board without mask """
		print(self.board_wm)

	def showboard_m(self):
		""" Shows the board with mask """
		print(self.board_w_mask)

		""" Numbers all grids of the board with numbers of Mines in surrounding """ 
	def numbering_mines(self):
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				position = [i,j]
				if self.board_wm[i][j] == self.EMPTY:
					self.board_wm[i][j] = " "+str(self.check_surrounding(position))
				else:
					pass

	def check_surrounding(self,position):
		count = 0
		neighbors = lambda x,y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= self.size[0] and
                                   -1 < y <= self.size[0] and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 < self.size[0]) and
                                   (0 <= y2 < self.size[0]))]
		#print(neighbors(position[0],position[1]))
		for all_n in neighbors(position[0],position[1]):
			if self.board_wm[all_n[0]][all_n[1]] == self.MINES:
				count += 1 
			else:
				pass
		return count

	