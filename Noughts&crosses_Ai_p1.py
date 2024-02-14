import random

options=[1,2,3,4,5,6,7,8,9]#computer avaliable numbers
board=[[1,2,3],[4,5,6],[7,8,9]]

gridX=3
gridY=3
#change these to change theoretical grid size

def output():
    for i in range(gridX):
        print("\n-------------")
        print ("|",end="")
        for j in range(gridY):
            print("",board[i][j],end=" |")#loops through 2D array to create boardgame table
    print("\n-------------")
    winCheck()
    #checks if either has player has won before asking player for their next move

def move():
    taken=0
    #tracks if space is avaliable to take

    playInp=input("please select the postition you would like")
    try:
        inp1=int(playInp)#converts to integer so program doesnt crash on input of Char
    except:
        print("ERROR:invalid input")
        move()

    if(inp1>9 or inp1<1):
        print("ERROR:out of bounds")#restarts after out of bounds input
        move()

    for i in range(gridX):
        for j in  range(gridY):
            if(inp1==board[i][j]):
                board[i][j]="X"
                #replaces position of 2D array with X
                taken=1
                #logged as not taken
    
    for i in range(len(options)):
        if inp1==options[i]:
            options[i]="X"
            #updates computers avaliable numbers

    if (taken==0):
        print("Space occupied")
        move()
    elif(taken==1):
        compPick()
        #computers turn


def compPick():
    rand_num=random.randrange((len(options)))
    rand=options[rand_num]
    #picks random number in array
    if rand=="X":
        compPick()
    elif rand =="O":
        compPick()
        #restarts if position is taken
    print(rand)
    for i in range(gridX):
        for j in  range(gridY):
            if(rand==board[i][j]):
                board[i][j]="O"
                #displays computers pick
    
    for i in range(len(options)):
        if rand==options[i]:
            options[i]="O"
            #takes chosen number out of computer's 'options' to pick

    output()#displays game with new player and computer spots

def winCheck():
    check=0
    count=0

    while count<3:
        if board[0][count]==board[1][count]==board[2][count]:
            if board[0][count]=="X":
                playerVic()
            elif board[0][count]=="O":
                CompVic()
        count=count+1
    count =0
    #cycles through horizontal coloumns to check for victory

    while count<3:
        if board[count][0]==board[count][1]==board[count][2]:
            if board[count][0]=="X":
                playerVic()
            elif board[count][0]=="O":
                CompVic()
        count=count+1
    count=0
    #cycles through vertical coloumns to check for victory

    if board[count][count]==board[count+1][count+1]==board[count+2][count+2]:
            if board[count][count]=="X":
                playerVic()
            elif board[count][count]=="O":
                CompVic()
    elif board[count][count+2]==board[count+1][count+1]==board[count+2][count]:
            if board[count][count+2]=="X":
                playerVic()
            elif board[count][count+2]=="O":
                CompVic()
    #checks diagonals for victory
                
    move()

def playerVic():
    restart=input("You win,type Rematch to play again")
    inp2=restart.upper()
    if inp2=="REMATCH":
        reset()
    else:
        exit()
    #allows player to play multiple times or close terminal
    
def CompVic():
    restart=print("You have lost, type Rematch to play again")
    inp2=restart.upper()
    if inp2=="REMATCH":
        reset()
    else:
        exit()
    

def reset():
    reOps=1
    for i in range(len(options)):
        options[i]=reOps
    #resets options array from 1 unitl array length
    
    reBoard=1
    for i in range(gridX):
        for j in range(gridY):
            board[i][j]=reBoard
    #resets board array from 1 until array length
    move()


move()
#starts game