class TicTacToe():

    # constructor for TicTacToe class
    def __init__(self, grid_size=3, starting_player='X'):
        # creates a grid with numbered spaces from 0 to (grid_size**2)-1
        self.grid = [['{}'.format((y*grid_size)+x) for x in range(grid_size)] for y in range(grid_size)]
        self.current_turn = starting_player
        self.grid_size = grid_size
        self.turn_count = 0
        
        # lambda function to check if all elements in a list are the same
        self.all_same = lambda x : len(set(x)) == 1

    # alternates the current turn
    def alternate_turn(self):
        self.current_turn = 'X' if self.current_turn == 'O' else 'O'

    # used to mark a location on the board with the current_turn
    def mark_board(self, x, y):
        self.grid[y][x] = self.current_turn

    # pretty print for the board
    def display_board(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                print(self.grid[i][j], end = ' | ' if j != self.grid_size-1 else '\n')
            if i != self.grid_size-1:
                print('-' * (4*(self.grid_size-1)+1))

    # checks to make sure a move is valid, returns a boolean
    def valid_move(self, x, y):
        if x < self.grid_size and y < self.grid_size and x >= 0 and y >= 0:
            if self.grid[y][x].isnumeric():
                return True
        return False

    # handles turn processing given a move in x, y coordinates
    def execute_turn(self, x, y):
        if self.valid_move(x, y):
            self.mark_board(x, y)
            self.alternate_turn()
            self.turn_count += 1
            return True
        return False

    # shows output to user, takes input, translates user move to x, y coordinates
    def display_turn(self):
        self.display_board()
        while True:
            move = ' ';
            while not move.isnumeric():
                print("{}'s turn!\nPick a numeric location to place your piece: ".format(self.current_turn), end = '')
                move = input()
            move = int(move)
            if self.execute_turn(move%self.grid_size, move//self.grid_size):
                break
        print()

    # checks for a game winner or tie or nothing
    def check_winner(self):
        if self.turn_count >= (self.grid_size*2)-1:
            # check diagonal from top left
            if self.all_same([self.grid[i][i] for i in range(self.grid_size)]):
                return self.grid[0][0]
            # check diagonal from top right
            if self.all_same([self.grid[i][((-1)*(i+1))] for i in range(self.grid_size)]):
                return self.grid[0][self.grid_size-1]
            for i in range(self.grid_size):
                # check rows
                if self.all_same(self.grid[i]):
                    return self.grid[i][0]
                # check columns
                if self.all_same([self.grid[j][i] for j in range(self.grid_size)]):
                    return self.grid[0][i]
            # if no winner and max turn_count is reached, it's a tie
            if self.turn_count == self.grid_size**2:
                return "Nobody"
        return None

    # run function to handle top level console game processing
    def run(self):
        # while loop runs until the game ends, indicated by the "winner" variable
        while True:
            winner = self.check_winner()
            if not winner:
                self.display_turn()
            else:
                self.display_board()
                print("{} wins!\n".format(winner))
                break

if __name__ == "__main__":
    print("Starting program.\n")
    game = TicTacToe()
    game.run()
    print("Ending program.")
