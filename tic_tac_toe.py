# SETP 1
# TO DIPLAY THE PLAY BOARD

def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

# test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]



# STEP 2
# TO TAKE PLAYER INPUT AS MARKER
def player_input():
    marker = " "

    while marker != "X" and marker != "O":
        marker = input("Do you want me to play X or O? ").upper()

        if marker == "X":
            return ("X", "O")
        else:
            return ("O", "X")



# STEP 3
# PUT THE MARKER AT DESIRED POSITION ON THE BOARD
def place_marker(board, marker, position):
    board[position] = marker
    return board[position]

# test_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]



# STEP 4
# WIN CHECK
def win_check(board, marker):
    return (board[7] == marker and board[8] == marker and board[9] == marker or
    board[4] == marker and board[5] == marker and board[6] == marker or
    board[1] == marker and board[2] == marker and board[3] == marker or
    board[7] == marker and board[4] == marker and board[1] == marker or
    board[8] == marker and board[5] == marker and board[2] == marker or
    board[9] == marker and board[6] == marker and board[3] == marker or
    board[7] == marker and board[5] == marker and board[3] == marker or
    board[9] == marker and board[5] == marker and board[1] == marker)


# STEP 5
# TO CHOOSE WHO PLAYS FIRST
import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 2"
    else:
        return "Player 1"

# STEP 6
# TO CHECK IF THERE IS FREE SPACE IN THE BOARD
def space_check(board, position):
    board[position] = ' '

# SETP 7
# TO CHECK IF THE BOARD IS FULL
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# STEP 8
# ASK PLAYER TO CHOOSE A POSITION
def player_choice(board):
    position = 0
    
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose a position 1 -9: "))

    return position



# STEP 9
# TO ASK PLAYER TO PLAY AGAIN
def replay():
    choice = input("Do you want to play again? YES or NO ").lower().startswith('y')
    return choice

# STEP 10
# TO RUN THE GAME

print("WELCOME TOP TIC TAC TOE")

while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will choose first')

    play_game = input("Are you ready to play?  Enter YES or NO ")
    if play_game.startswith('y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            print(position)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw")
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            print(position)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 2 has won!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a draw")
                    break
                else:
                    turn = 'Player 1'

        
    if not replay():
        break

