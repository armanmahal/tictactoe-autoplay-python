import random

print("\n                  ***TIC TAC TOE*** \n")

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
winnerFound = False
i = 0
x = -1

def board():
    print("                  | ", mat[0][0], " | ", mat[0][1], " | ", mat[0][2], " | ")
    print("                  | ", mat[1][0], " | ", mat[1][1], " | ", mat[1][2], " | ")
    print("                  | ", mat[2][0], " | ", mat[2][1], " | ", mat[2][2], " | ")

def winLogic():
    global winnerFound
    if (((mat[0][0] == 'X') and (mat[0][1] == 'X') and (mat[0][2] == 'X')) or ((mat[0][0] == 'O') and (mat[0][1] == 'O') and (mat[0][2] == 'O'))):
        winnerFound = True
    if (((mat[1][0] == 'X') and (mat[1][1] == 'X') and (mat[1][2] == 'X')) or ((mat[1][0] == 'O') and (mat[1][1] == 'O') and (mat[1][2] == 'O'))):
        winnerFound = True
    if (((mat[2][0] == 'X') and (mat[2][1] == 'X') and (mat[2][2] == 'X')) or ((mat[2][0] == 'O') and (mat[2][1] == 'O') and (mat[2][2] == 'O'))):
        winnerFound = True
    if (((mat[0][0] == 'X') and (mat[1][0] == 'X') and (mat[2][0] == 'X')) or ((mat[0][0] == 'O') and (mat[1][0] == 'O') and (mat[2][0] == 'O'))):
        winnerFound = True
    if (((mat[0][1] == 'X') and (mat[1][1] == 'X') and (mat[2][1] == 'X')) or ((mat[0][1] == 'O') and (mat[1][1] == 'O') and (mat[2][1] == 'O'))):
        winnerFound = True
    if (((mat[0][2] == 'X') and (mat[1][2] == 'X') and (mat[2][2] == 'X')) or ((mat[0][2] == 'O') and (mat[1][2] == 'O') and (mat[2][2] == 'O'))):
        winnerFound = True
    if (((mat[0][0] == 'X') and (mat[1][1] == 'X') and (mat[2][2] == 'X')) or ((mat[0][0] == 'O') and (mat[1][1] == 'O') and (mat[2][2] == 'O'))):
        winnerFound = True
    if (((mat[0][2] == 'X') and (mat[1][1] == 'X') and (mat[2][0] == 'X')) or ((mat[0][2] == 'O') and (mat[1][1] == 'O') and (mat[2][0] == 'O'))):
        winnerFound = True

def auto_play_random():
    bool = True
    while( bool == True):
        x = random.randint(0,2)
        y = random.randint(0,2)
        if (mat[x][y] != 'X') and (mat[x][y] != 'O'):
            mat[x][y]  = 'O'
            bool = False

def autoPlay():
    if ((mat[1][1] != 'X') and (mat[1][1] != 'O')):
        mat[1][1] = 'O'

    elif ((((mat[0][0] == 'O') and (mat[0][1] == 'O')) or ((mat[2][0] == 'O') and (mat[1][1] == 'O')) or (
            (mat[2][2] == 'O') and (mat[1][2] == 'O'))) and ((mat[0][2] != 'X') and (mat[0][2] != 'O'))):
        mat[0][2] = 'O'

    elif ((((mat[1][0] == 'O') and (mat[1][2] == 'O')) or ((mat[0][2] == 'O') and (mat[2][2] == 'O')) or (
            (mat[1][0] == 'O') and (mat[1][1] == 'O'))) and ((mat[1][2] != 'O') and (mat[1][2] != 'X'))):
        mat[1][2] = 'O'

    elif ((((mat[2][0] == 'O') and (mat[2][1] == 'O')) or ((mat[0][0] == 'O') and (mat[1][1] == 'O')) or (
            (mat[0][2] == 'O') and (mat[1][2] == 'O'))) and ((mat[2][2] != 'X') and (mat[2][2] != 'O'))):
        mat[2][2] = 'O'

    elif ((((mat[0][1] == 'O') and (mat[0][2] == 'O')) or ((mat[1][0] == 'O') and (mat[2][0] == 'O')) or (
            (mat[2][2] == 'O') and (mat[1][1] == 'O'))) and ((mat[0][0] != 'X') and (mat[0][0] != 'O'))):
        mat[0][0] = 'O'

    elif ((((mat[2][1] == 'O') and (mat[2][2] == 'O')) or ((mat[0][0] == 'O') and (mat[1][0] == 'O')) or (
            (mat[0][2] == 'O') and (mat[1][1] == 'O'))) and ((mat[2][0] != 'X') and (mat[2][0] != 'O'))):
        mat[2][0] = 'O'

    elif ((((mat[1][1] == 'O') and (mat[1][2] == 'O')) or ((mat[0][0] == 'O') and (mat[2][0] == 'O'))) and (
            (mat[1][0] != 'O') and (mat[1][0] != 'X'))):
        mat[1][0] = 'O'

    elif ((((mat[0][1] == 'O') and (mat[1][1] == 'O')) or ((mat[2][2] == 'O') and (mat[2][0] == 'O'))) and (
            (mat[2][1] != 'O') and (mat[2][1] != 'X'))):
        mat[2][1] = 'O'

    elif ((((mat[2][1] == 'O') and (mat[1][1] == 'O')) or ((mat[0][2] == 'O') and (mat[0][0] == 'O'))) and (
            (mat[0][1] != 'O') and (mat[0][1] != 'X'))):
        mat[0][1] = 'O'

    elif ((((mat[1][0] == 'O') and (mat[1][2] == 'O')) or ((mat[0][1] == 'O') and (mat[2][1] == 'O')) or (
            (mat[2][2] == 'O') and (mat[0][0] == 'O')) or ((mat[2][0] == 'O') and (mat[0][2] == 'O'))) and (
                  (mat[1][1] != 'O') and (mat[1][1] != 'X'))):
        mat[1][1] = 'O'

    elif ((((mat[0][0] == 'X') and (mat[0][1] == 'X')) or ((mat[2][0] == 'X') and (mat[1][1] == 'X')) or (
            (mat[2][2] == 'X') and (mat[1][2] == 'X'))) and ((mat[0][2] != 'O') and (mat[0][2] != 'X'))):
        mat[0][2] = 'O'

    elif ((((mat[1][0] == 'X') and (mat[1][2] == 'X')) or ((mat[0][2] == 'X') and (mat[2][2] == 'X'))) and (
            (mat[1][2] != 'O') and (mat[1][2] != 'X'))):
        mat[1][2] = 'O'

    elif ((((mat[2][0] == 'X') and (mat[2][1] == 'X')) or ((mat[0][0] == 'X') and (mat[1][1] == 'X')) or (
            (mat[0][2] == 'X') and (mat[1][2] == 'X'))) and ((mat[2][2] != 'O') and (mat[2][2] != 'X'))):
        mat[2][2] = 'O'

    elif ((((mat[0][1] == 'X') and (mat[0][2] == 'X')) or ((mat[1][0] == 'X') and (mat[2][0] == 'X')) or (
            (mat[2][2] == 'X') and (mat[1][1] == 'X'))) and ((mat[0][0] != 'O') and (mat[0][0] != 'X'))):
        mat[0][0] = 'O'

    elif ((((mat[2][1] == 'X') and (mat[2][2] == 'X')) or ((mat[0][0] == 'X') and (mat[1][0] == 'X')) or (
            (mat[0][2] == 'X') and (mat[1][1] == 'X'))) and ((mat[2][0] != 'O') and (mat[2][0] != 'X'))):
        mat[2][0] = 'O'

    elif ((((mat[1][1] == 'X') and (mat[1][2] == 'X')) or ((mat[0][0] == 'X') and (mat[2][0] == 'X'))) and (
            (mat[1][0] != 'O') and (mat[1][0] != 'X'))):
        mat[1][0] = 'O'

    elif ((((mat[0][1] == 'X') and (mat[1][1] == 'X')) or ((mat[2][2] == 'X') and (mat[2][0] == 'X'))) and (
            (mat[2][1] != 'O') and (mat[2][1] != 'X'))):
        mat[2][1] = 'O'

    elif ((((mat[2][1] == 'X') and (mat[1][1] == 'X')) or ((mat[0][2] == 'X') and (mat[0][0] == 'X'))) and (
            (mat[0][1] != 'O') and (mat[0][1] != 'X'))):
        mat[0][1] = 'O'

    elif ((((mat[1][0] == 'X') and (mat[1][2] == 'X')) or ((mat[0][1] == 'X') and (mat[2][1] == 'X')) or (
            (mat[2][2] == 'X') and (mat[0][0] == 'X')) or ((mat[2][0] == 'X') and (mat[0][2] == 'X'))) and (
                  (mat[1][1] != 'O') and (mat[1][1] != 'X'))):
        mat[1][1] = 'O'

    else:
        auto_play_random()

print("*** SEE THE GIVEN BOARD FOR REFERENCE OF INPUT POSITIONS ***\n")
board()     
print("\n ***STARTING*** \n")

while ((winnerFound == False) and (i<=8)):

    if ((i % 2) == 0):
        x = int(input("Player 1's turn, enter the input location 'X' : "))
        if((x<1) or (x>9)):
            print("Invalid input!")
            continue
        x = x - 1
        if((mat[int(x/3)][x%3] == 'X') or (mat[int(x/3)][x%3] == 'O')):
            print("Already filled here!")
            continue
        mat[int(x/3)][x%3] = 'X'
    else:
        print("COMPUTER's turn : ")

        if ((i == 1) and (x == 4)):
            mat[0][2] = 'O'

        elif ((i == 3) and (((mat[0][2] == 'X') and (mat[2][0] == 'X')) or ((mat[0][0] == 'X') and (mat[2][2] == 'X')))):
            mat[2][1] = 'O'

        else:
            autoPlay()

    board()
    winLogic()

    i = i + 1

if (winnerFound == False) :
    print('DRAW')
elif((i%2)==0):
    print("COMPUTER 'O'  WINS")
else:
    print("Player 1 'X'  WINS")
