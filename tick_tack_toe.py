from IPython.display import clear_output
import random
test_board = ['#'," "," "," "," "," "," "," "," "," "]


def display_board(board):
    print('\n'*5)  # Remember, this only works in jupyter!
    
    print('   ||   ||')
    print(' ' + board[7] + ' || ' + board[8] + ' || ' + board[9])
    print('   ||   ||')
    print('---------------')
    print('   ||   ||')
    print(' ' + board[4] + ' || ' + board[5] + ' || ' + board[6])
    print('   ||   ||')
    print('---------------')
    print('   ||   ||')
    print(' ' + board[1] + ' || ' + board[2] + ' || ' + board[3])
    print('   ||   ||')






def choose_marker():
    mark = ''
    while not (mark == 'X' or mark == 'O'):
        mark = input("Player 1 Please pick a marker 'X' or 'O': ").upper()
    if mark == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,mark,position):
    board[position] = mark

def win_check(board,mark):
    mark = mark.upper()
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first_player():

    if random.randint(0,1) == 1 :
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    choice = input("WANNA PLAY AGAIN? : Enter 'yes' or 'no'")
    board = [" "]*10
    return choice == 'yes'

board = [" "]*10

while True:
    print('WELCOME TO TIC TAC TOE -')
    
    (player1_marker, player2_marker) = choose_marker()
    turn = choose_first_player()
    print(turn + ' Will Play First')
    play_game = input('Ready to play: Enter y or n')

    if play_game == 'y':
        game_on = True
    else :
        game_on = False    
    
    while game_on :
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)
            if win_check(board,player1_marker):
                display_board(board)
                print('Player 1 has won')
                game_on = False
            if full_board_check(board):
                display_board(board)
                print('This match was a Tie')
                game_on = False
            else:
                turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker,position)
            if win_check(board,player2_marker):
                display_board(board)
                print('Player 2 has won')
                game_on = False
            if full_board_check(board):
                display_board(board)
                print('This match was a Tie')
                game_on = False
            else:
                turn = 'Player 1'
    
    if not replay():
        break


    
