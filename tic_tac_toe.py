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
		self.gameover = False
		self.players = 2

	def display_grid(self):
		for x in range(len(self.grid)):

			print(self.grid[x], end="")
			
			if (x+1) % self.GRID_SIZE == 0:
				print(" ")

	def place_x_at(self, x):
		self.grid[x-1] = ["X"]
		self.moves[0].append(x-1)
		self.check_for_win()

	def place_o_at(self, o):
		self.grid[o-1] = ["O"]
		self.moves[1].append(o-1)
		self.check_for_win()

	def mark(self, pos, symbol):
		self.grid[pos-1] = [symbol]
		self.moves[0].append(pos-1)
		self.check_for_win()

	def get_columns(self):
		temp = ""
		for x in range(self.GRID_SIZE):
			temp += self.grid[x][0] + self.grid[x + self.GRID_SIZE][0] + self.grid[x + 2*self.GRID_SIZE][0]
			self.columns.append(temp)
			temp = ""

	def get_rows(self):
		temp = ""
		for x in range(len(self.grid)):
			temp += self.grid[x][0]

			if (x+1) % self.GRID_SIZE == 0:
				self.rows.append(temp)
				temp = ""


	def get_diagonals(self):
		temp = ""
		temp2 = ""
		counter1 = 0
		counter2 = 0

		for x in range(self.GRID_SIZE):
			if x == 0:
				temp += self.grid[x][0]
				temp2 += self.grid[self.GRID_SIZE - 1][0]
				counter1, counter2 = 0, 2
			else:
				counter1, counter2 = counter1 + (self.GRID_SIZE + 1), counter2 + (self.GRID_SIZE - 1)
				temp += self.grid[counter1][0]
				temp2 += self.grid[counter2][0]
		self.diagonals.append(temp)
		self.diagonals.append(temp2)

	def check_for_win(self):
		self.get_columns()
		self.get_rows()
		self.get_diagonals()
		x = 'XXX'
		o = 'OOO'

		if x in self.diagonals or x in self.rows or x in self.columns:
			self.display_grid()
			print("X WON!")
			self.gameover = True
		elif o in self.diagonals or o in self.rows or o in self.columns:
			self.display_grid()
			print("O WON!")
			self.gameover = True

	def run(self):
		sym = 'O'

		while not self.gameover:
			sym = 'X' if sym == 'O' else 'O'
			self.display_grid()
			a = int(input("{}'s Turn".format(sym)))
			self.mark(a, sym)

if __name__ == "__main__":
	a = tic_tac_toe()
	a.run()