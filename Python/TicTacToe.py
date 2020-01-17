import random

def display_board(board):
    print('\n' * 100)

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------'
          '')
    print(board[4] +  '|' + board[5] + '|' + board[6])
    print('------')
    print(board[1] +  '|' + board[2] + '|' + board[3])

test_board = [' ','X','X','X','O','X','X','X',' ','X']



def player_input():
    marker = ''

    while not(marker == 'X' or marker == 'O'):#while the input is not X or O,keep asking for input

        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O','X')



def place_marker(board, marker, position):

          board[position] = marker



def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark))




def choose_first():

   num = random.randint(1,2)
   print(num)
   if num%2 == 0:
       return 'Player1'
   else:
       return 'Player2'





def space_check(board, position):
    if board[position] ==  ' ':
        return True
    return False



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):

    position = 0

    while space_check(board,position) != True or position not in [1,2,3,4,5,6,7,8,9]:
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    decision =  input('Do you want to play again? Y for yes or N for no  ')

    if decision.lower().startswith('y'):
        return True
    elif decision.lower().startswith('n'):

        return False
    else:
        return 'Please give a valid answer'




############################## The Game #########################################

print('Welcome to Tic Tac Toe!')

while True:
    new_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] =='y':
        game_on =True
    else:
        game_on = False

    while game_on == True:

        if turn == 'Player 1':

            display_board(new_board)
            #choose a positon
            place_marker(new_board,player1_marker,player_choice(new_board))

            if win_check(new_board, player1_marker):
                display_board(new_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(new_board):

                    display_board(new_board)

                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2's turn
                display_board(new_board)
                # choose a positon
                place_marker(new_board, player2_marker, player_choice(new_board))

                if win_check(new_board, player2_marker):
                    display_board(new_board)
                    print('Player 2 has won')
                    game_on = False
                else:
                    if full_board_check(new_board):

                        display_board(new_board)

                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'




    if not replay():
        break




