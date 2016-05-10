class tic_tac_toe():
	'''|1|2|3| [][][]
	   |4|5|6| [][][]
	   |7|8|9| [][][]'''
	
	GRID_SIZE = 3

	def __init__(self):
		self.grid = [[" "] for x in range(self.GRID_SIZE ** 2)]
		self.columns = []
		self.rows = []
		self.diagonals = []
		self.moves = [[],[]]


	# def create_grid(self):
	# 	GRID_SIZE = 3

	# 	for a in range(GRID_SIZE):
	# 		self.grid.append([[], [], []])

	def display_grid(self):
		for x in range(len(self.grid)):

			print(self.grid[x], end="")
			
			if (x+1) % self.GRID_SIZE == 0:
				print(" ")

	def place_x_at(self, x):
		self.grid[x-1] = ["X"]
		self.moves[0].append(x-1)

	def place_o_at(self, o):
		self.grid[o-1] = ["O"]
		self.moves[1].append(o-1)

	def get_columns(self):
		temp = ""
		for x in range(self.GRID_SIZE):
			temp += self.grid[x][0] + self.grid[x + self.GRID_SIZE][0] + self.grid[x + 2*self.GRID_SIZE][0]
			self.columns.append(temp)
			temp = ""

		print(self.columns)

	def get_rows(self):
		temp = ""
		for x in range(len(self.grid)):
			temp += self.grid[x][0]

			if (x+1) % self.GRID_SIZE == 0:
				self.rows.append(temp)
				temp = ""

		print(self.rows)

	def get_diagonals(self):
		temp = ""
		temp2 = ""
		counter1 = 0
		counter2 = 0
		for x in range(self.GRID_SIZE):
			if x == 0:
				temp += self.grid[x][0]
				temp2 += self.grid[self.GRID_SIZE][0]
				counter1, counter2 = 0, 2
			else:
				counter1, counter2 = counter1 + 3, counter2 + 2
				temp += self.grid[counter1][0]
				temp2 += self.grid[counter2][0]
		self.diagonals.append(temp)
		self.diagonals.append(temp2)

		print(self.diagonals)




		pass

	def check_for_win(self):
		pass


if __name__ == "__main__":
	a = tic_tac_toe()
	print(a.grid)
	print("")
	a.display_grid()
	a.place_x_at(4)
	a.place_x_at(1)
	a.place_x_at(7)
	print("")
	a.display_grid()
	a.place_o_at(5)
	print("")
	a.display_grid()
	print("")
	print(a.grid)
	print("")
	a.get_columns()
	print("")
	a.get_diagonals()
	input()