# Edmund's Comments
# - add more to your readme, make it presentable, look online for templates and examples
# - add comments to your code, functions, and classes for better readbility
# - print it a bit more like a tic tac toe board, for example
#   X | O | X
#   ---------
#   O | X | O
#   ---------
#   X | O | X
# - make the interface more descriptive or more intuitive, I didn't know how to mark spaces on the board
# - add a way to restart the game and keep track of wins between X and O
# - slim down code, just do what you need to do

class tic_tac_toe():
	'''|1|2|3| [][][]
	   |4|5|6| [][][]
	   |7|8|9| [][][]'''
	
        # you can take this as a constructor argument defaulted to 3, i.e. def __init__(self, grid_size=3):
	GRID_SIZE = 3

	def __init__(self):

                # in the case of grid_size = 3, this makes an array of 9 [" "]s
                # this is kind of weird and may be better represented as an array of 3 [" ", " ", " "]s
                # making it a 3x3 grid instead of a 1x9 grid
		self.grid = [[" "] for x in range(self.GRID_SIZE ** 2)]
                # are the bottom 3 variables really necessary?
                self.columns = []
		self.rows = []
		self.diagonals = []
		# what is this for? no comments, not sure
                self.moves = [[],[]]
		self.gameover = False
		# is this necessary for your current implementation?
                self.players = 2

	def display_grid(self):
		for x in range(len(self.grid)):
			print(self.grid[x], end="")
			if (x+1) % self.GRID_SIZE == 0:
			    # don't need to put a space in there, just print() is fine
                            # also, you can do print(self.grid[x], end='\n' if not x % self.GRID_SIZE else '') 
                            # or something like that just for consistency
                            print(" ")

        # for placing, it's weird to assign a list with just one element
        # follow m advice above and make it a 3x3 array and just assign a letter 'X'
        # also the place/mark functions are redundant, write it as one function taking an argument for X or O
        # try not to copy and paste code (seems like you did this with mark, just clean the code up or use mark to implement place x and o)
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

        # for the get functions, temp can just be created once in the beginning of the for loop
        # these functions need to be changed after you implement the 3x3, I'll take a look again after it's done
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
                        # keep track of who's turn it is inside the class, don't do any game processing outside the class
                        sym = 'X' if sym == 'O' else 'O'
			self.display_grid()
			a = int(input("{}'s Turn".format(sym)))
			self.mark(a, sym)

if __name__ == "__main__":
	a = tic_tac_toe()
	a.run()
