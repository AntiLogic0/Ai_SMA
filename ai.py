# Global Variables
board = []
player = "X"

# Copy your functions from the previous activities here:
# print_board, is_valid_move, place_player, take_turn
def print_board():
    for i, row in enumerate(board):
        print(f"{i} ", end ="")
        for cel in row:
            print(f"{cel} ", end ="")
        print("\n")

def is_valid_move(row, col):
    if row < 0 or col < 0 or row > 2 or col > 2:
        return False
    if board[row][col] != '-':
        return False
    return True

def place_player(player, row, col):
    board[row][col] = player

def take_turn(player):
    valid_move = False
    while not valid_move:
        print(f"{player}'s Turn")
        row = int(input('Enter a row: '))
        col = int(input('Enter a column: '))
        if is_valid_move(row, col):
            place_player(player, row, col)
            valid_move = True
        else:
            print("Place your item properly.")
    print_board()

# Write your check win functions here:
def check_col_win(player):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    return False

def check_row_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    return False

def check_diag_win(player):
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_win(player):
    return check_col_win(player) or check_row_win(player) or check_diag_win(player)

def check_tie():
    for row in board:
        for cel in row:
            if cel == '-':
                return False
    return not (check_win("X") or check_win("O"))

# Start of program
print("\t\tWelcome to Tic Tac Toe!")
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
print_board()

'''
DO NOT CHANGE: Tests
each test should print true if your function is written correctly:
'''
# Check row win
place_player(player, 0, 1)
place_player(player, 0, 2)
place_player(player, 0, 0)
print_board()
print("Check Row Win: ", check_win(player))  # Should print True

# Check col win
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
place_player(player, 1,0)
place_player(player, 2,0)
place_player(player, 0,0)
print_board()
print("Check Col Win: ", check_win(player))  # Should print True

# Check diag win
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
place_player(player, 0,0)
place_player(player, 1,1)
place_player(player, 2,2)
print_board()
print("Check Diag Win: ", check_win(player))  # Should print True

# Check Tie
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
place_player("X", 1,1)
place_player("X", 0,2)
place_player(player, 0,0)
place_player("O", 0,1)
place_player("O", 2,2)
place_player("O", 1,0)
place_player("X", 1,2)
place_player("X", 2,1)
place_player("O", 2,0)
print_board()
print("Check Tie: ", check_tie())  # Should print True
