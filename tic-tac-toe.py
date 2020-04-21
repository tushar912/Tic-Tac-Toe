board =[' ' for x in range(10)]
def insertletter(letter,pos):
    board[pos]=letter

def isSpacefree(pos):
    return b[pos]==' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isFull(board):
    if ' ' in board:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run =True
    while run:
        move =input("tell the position")
        try:
            move=int(move)
            if(move >0 and move<10):
                if(isSpacefree):
                    run=False
                    insertletter('X',move)
                else:
                    print("no space")
            else:
                print("enter between 1 and 10")

        except:
            print("enter number")

def computerMove():
    possiblemoves=[x for x,letter in enumerate(board) if letter==' ' and x!=0]

    for let in ["0","X"]:
        for i in possiblemoves:
            bcopy=board[:]
            bcopy[i]=let
            if IsWinner(bcopy,let):
                move =i
                return move

    corners=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            corners.append(i)
    
    if len(corners)>0:
        move =r(corners)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
def r(l):
    import random
    c=len(l)
    r=random.randrange(0,c)
    return l[r]

def main():
    print("welcome gamer")

    printBoard(board)
    while not(isFull(board)):
        if not (IsWinner(board,'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry u lose")
            break
        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertletter('O' , move)
                print('computer placed an o on position' , move , ':')
                printBoard(board)
        else:
            print("you win!")
            break

if isFull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break



