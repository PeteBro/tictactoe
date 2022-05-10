import time
import random

def gameon():
    choice = None
    choice = input('Would you like to keep playing? (Y/N):')
    print('\n')
    while choice not in ['Y', 'N']:
        choice = input("Sorry, I didn't understand that, please enter either Y or N:")
        print('\n')

    return choice == 'Y'



def getinfo():
    print('Welcome to tic-tac-toe!')
    p1 = input('Player 1, please enter your name:')
    print('\n')
    print(f'Hi {p1}!')
    print('\n')
    time.sleep(1)
    p2 = input('Player 2, please enter your name:')
    print('\n')
    print(f'Hi {p2}!')
    print('\n')
    time.sleep(1)
    print("Let's get started!")
    print('\n')

    return p1, p2



def whogoesfirst(p1, p2):
    outcomes = ['Heads', 'Tails']
    choice = None
    choice = input(f'{p1}, Heads or Tails? (H/T):')
    print('\n')
    while choice not in ['H', 'T']:
        choice = input("Sorry, I didn't understand that, please enter either H or T:")
        print('\n')
    print('Ok! Here we go...')
    print('\n')
    time.sleep(1)
    side = random.choice(outcomes)
    if side[0] == choice:
        starter = p1
    else:
        starter = p2
    print(f"It's {side}! {starter} goes first!")
    print('\n')

    return starter



def tictactoe():

    keep_playing = True
    p1, p2 = getinfo()
    time.sleep(1)
    players = [p1, p2]
    markers = ['O', 'X']
    winning_idcs = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    starter = whogoesfirst(p1, p2)
    time.sleep(1)

    print("Here's your board:")
    print('\n')
    time.sleep(1)
    print(f"{'   '.join(['-','-','-'])}\n\n{'   '.join(['-','-','-'])}\n\n{'   '.join(['-','-','-'])}")
    print('\n')
    time.sleep(1)

    print('To choose a place on the board, enter one of the corresponding labels:')
    print('\n')
    time.sleep(1)
    print(f"{'   '.join(['1','2','3'])}\n\n{'   '.join(['4','5','6'])}\n\n{'   '.join(['7','8','9'])}")
    print('\n')
    time.sleep(1)

    while keep_playing:

        winner = False
        board = ['-']*9
        time.sleep(1)

        turn = starter
        marker = markers[0]

        while True:

            stalemate = False

            pos = input(f'{turn}, where would you like to go?:')
            print('\n')

            while pos not in [str(i) for i in range(1,10)]:
                pos = input("Sorry, I didn't understand that, please enter a number between 1 and 9:")
                print('\n')

            while board[int(pos)-1] != '-':
                pos = input("That position's taken! Please choose another:")
                print('\n')

            while pos not in [str(i) for i in range(1,10)]:
                pos = input("Sorry, I didn't understand that, please enter a number between 1 and 9:")
                print('\n')
            
            pos = int(pos)
            board[pos-1] = marker

            print(f"{'   '.join(board[:3])}\n\n{'   '.join(board[3:6])}\n\n{'   '.join(board[6:9])}")
            print('\n')
            time.sleep(1)

            current_idcs = [idx for idx, value in enumerate(board) if value == marker]

            if True in list(map(lambda c: set(c).issubset(set(current_idcs)), winning_idcs)):
                print(f'{turn} wins!')
                print('\n')
                break

            if '-' not in board:
                print('Stalemate!')
                stalemate = True
                break
            

            turn = [p for p in players if p != turn][0]
            marker = [m for m in markers if m != marker][0]
        
        time.sleep(1)
        keep_playing = gameon()
        if keep_playing:
            if stalemate:
                starter = whogoesfirst(p1, p2)
            else:
                print(f'Since {turn} won last game, they go first.')
                print('\n')
                starter = turn

    print('Good Game!')


tictactoe()
