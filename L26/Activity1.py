"Tic Tac Toe in Python!"
Board = {'7': ' ', '8': ' ', '9': ' ', '4': ' ', '5': ' ', '6': ' ', '1': ' ', '2': ' ', '3': ' '}
board_keys = []

for key in Board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + ' |' + board['8' ] + ' |' + board['9' ])
    print(' -+--+-')
    print(board['4'] + ' |' + board['5'] + ' |' + board['6' ])
    print(' -+--+-')
    print(board['1'] +' |'+ board['2'] + ' |' + board['3' ])

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(Board)
        print("It's your turn, " + turn + ". Move to which position?")

        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which position?")
            continue

        if count >=5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break 
            elif Board['4'] == Board['5'] == Board['6'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break 
            elif Board['1'] == Board['2'] == Board['3'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break 
            elif Board['2'] == Board['5'] == Board['8'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break 
            elif Board['3'] == Board['6'] == Board['9'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break 
            elif Board['1'] == Board['5'] == Board['9'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break 
            elif Board['7'] == Board['5'] == Board['3'] != ' ':
                printBoard(Board)
                print("\n Game OVER \n")
                print(" **** " +turn + "won. ****")
                break 

#Tie logic:
        if count == 9: 
            print("Its a tie!!!")
            print("Ending game")
            break 

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'            

    restart = input("Try Again? (y/n)")
    if restart == "y" or restart == "Y":
        print("All RIGHT!")
        for key in board_keys:
            Board[key]

        game()

if __name__ == "__main__":
    game()