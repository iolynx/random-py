#connect 4
from keyboard import play

#player 1 = O
#player 2 = X

def get_input(counter):
    if counter % 1 == 0:
        playerInp = int(input("Enter a Column number (0 - 7), player 1 (O):"))
        if playerInp > -1 and playerInp < 8:
            return playerInp - 1
        else:
            return get_input(counter)
    else:
        playerInp = int(input("Enter a Column number (0 - 7), player 2 (X):"))
        if playerInp > -1 and playerInp < 8:
            return playerInp - 1
        else:
            return get_input(counter)


def update_board(board, counter, playerInp):
    done = False
    if counter % 2 == 0:
        character = "X"
    else: 
        character = "O"    
    for i in range(5, 0, -1):
        if board[i][playerInp] == ' ':
            board[i][playerInp] = character
            done = True
            return
    if not done:
        playerInp = int(input("Invalid choice. Try again. (1 - 7):"))
        update_board(board, counter, playerInp)
        return

def print_board(board):
    print("-------------")
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end = ' ')
        print(" ")
    print("-------------")
    print("1 2 3 4 5 6 7")    

board = [None]*6 
for i in range(len(board)):
    board[i] = [' '] *7 


counter = 1
gameOver = False
while not gameOver:
    print_board(board)
    inp = get_input(counter)
    update_board(board, counter, inp)
    counter += 1
