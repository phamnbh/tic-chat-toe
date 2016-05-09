class tic_tac_toe():
	'''|1|2|3|
	   |4|5|6|
	   |7|8|9| '''
	def __init__(self):
		self.grid = []


	def create_grid(self):
		GRID_SIZE = 3

		for a in range(GRID_SIZE):
			temp = []
			for b in range((2*GRID_SIZE) + 1): # | | | |
				if b % 2 == 0:
					temp.append("|")
				else:
					temp.append(" ")
			self.grid.append(temp)


	def display_grid(self):
		
		for a in range(len(self.grid)):
			temp = ""
			for b in self.grid[a]:
				temp += b
			print(temp)

	def place_x_at(self, x):

		




if __name__ == "__main__":
	print("Hello tic tac toe")
	a = tic_tac_toe()
	a.create_grid()
	a.display_grid()
	input()