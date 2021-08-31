from IPython.display import clear_output

# A function that can print out a board. Set up your board as a list, 
# where each index 1-9 corresponds with a number on a number pad, 
# so you get a 3 by 3 board representation.
def display_board(board):
    clear_output()
    print('  |   |')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   |')
    print('----------')
    print('  |   |')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   |')
    print('----------')
    print('  |   |')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   |')

# A function that can take in a player input and assign 
# their marker as 'X' or 'O'. Think about using while loops to 
# continually ask until you get a correct answer.
def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# A function that takes in the board list object, 
# a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    
    board[position] = marker

# A function that takes in a board and a mark (X or O) 
# and then checks to see if that mark has won. 

def win_check(board, mark):
    
    # Win Tic Tac Toe?
    
    # All rows, and check to see if they all share the same marker?
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    # All columns, check to see if marker matches
    
    # 2 diagonals, check to see match

# A function that uses the random module to randomly 
# decide which player goes first. You may want to lookup random.randint() 
# Return a string of which player went first.
import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# A function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    
    return board[position] == ' '

# A function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    # Board is full is we return true
    return True

# A function that asks for a player's next position (as a number 1-9) and 
# then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
    return position

# A function that asks the player if they want to play again and returns a boolean True 
# if they do want to play again.

def replay():
    
    choice = input("Play again? Enter Yes or No: ")
    
    return choice == 'Yes'


# MAIN FUNCTION

print('Welcome to Tic Tac Toe!')

# While Loop to keep running the game
while True:
    
    #Play the game
    
    # Set the game up here(Board, whos first, choose markers X,O)
    #pass
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? y or n: ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    ## Game Play
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            # Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                # Or check if ther is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    # No tie and no win? Then next player's turn
                    turn = 'Player 2'
        elif turn == 'Player 2' :
            # Player2's turn.
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            # Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                # Or check if ther is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    # No tie and no win? Then next player's turn
                    turn = 'Player 1'
           
             #pass

    if not replay():
        break
    # BREAK OUT OF THE WHILE LOOP ON replay()