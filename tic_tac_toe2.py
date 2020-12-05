import random
board = ["-"] * 10

def dispaly_board(board):
    print(' ' + board[7] + " | " + board[8] + " | " + board[9])
    print(' ' + board[4] + " | " + board[5] + " | " + board[6])
    print(' ' + board[1] + " | " + board[2] + " | " + board[3])

# dispaly_board(board)

def player_input(board, pos):
    board[pos] = "X"

pos = int(input())
player_input(board, pos)
dispaly_board(board)
