import random

options=[1,2,3,4,5,6,7,8,9]#computer avaliable numbers-seperate for random
board=[[1,2,3],[4,5,6],[7,8,9]]
gridX=3
gridY=3
#change these to change theoretical grid 


def start():
    global playLet
    global compLet
    global playerGo

    xO=input("Type X or O to decide which letter to play ")
    playLetter=xO.upper()
    match playLetter:
        case "X":
            playLet="X"
            compLet="O"
        case "O":
            playLet="O"
            compLet="X"
        case _ :
            print("ERROR-Unrecognised Response")
            start()
        #used to determine decsion of player letter

    firstGoInp=input("Type Me or Computer to decide who plays first ")
    firstGo=firstGoInp.upper()
    match firstGo:
        case "ME":
            playerGo=True
            output()
        case "COMPUTER":
            playerGo=False
            output()
        case _ :
            print("ERROR-Unrecognised Response")
            start()


def output():
    
    for i in range(gridX):
        print("\n-------------")
        print ("|",end="")
        for j in range(gridY):
            print("",board[i][j],end=" |")#loops through 2D array to create boardgame table
    print("\n-------------")
    #checks if either has player has won before asking player for their next move
    if playerGo==1:
        move()
    elif playerGo==0:
        compPick()
    else:
        print("oh no its broken")

def move():
    taken=0
    #tracks if space is avaliable to take(0 is taken, 1 is not taken)

    playInp=input("please select the postition you would like ")
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
                board[i][j]=playLet
                #replaces position of 2D array with X
                taken=1
                #logged as not taken
    
    for i in range(len(options)):
        if inp1==options[i]:
            options[i]=playLet
            #updates computers avaliable numbers

    if (taken==0):
        print("Space occupied")
        move()
    elif(taken==1):
        winCheck()
        #computers turn


def compPick():
    midTile=round(len(options)/2)
    #finds the midpoint of the array options

    if options[midTile]==(midTile+1):
        options[midTile]=compLet#checks if middle tile is taken
        for i in range(gridX):
            for j in range(gridY):
                if(board[i][j]==5):
                    board[i][j]=compLet
        winCheck()
        
    else:
        try:
        #try function to counter game crashing-computer tries generating a number but cant as all are taken
            rand_num=random.randrange((len(options)))
            rand=options[rand_num]
            #picks random number in array
            if rand=="X":
                compPick()
            elif rand =="O":
                compPick()
                #restarts if position is taken

            for i in range(gridX):
                for j in  range(gridY):
                    if(rand==board[i][j]):
                        board[i][j]=compLet
                        #displays computers pick
    
            for i in range(len(options)):
                if rand==options[i]:
                    options[i]=compLet
                    #takes chosen number out of computer's 'options' to pick
            winCheck()#displays game with new player and computer spots
        except:
            winCheck()

def winCheck():
    count=0
    global playerGo#needed to edit value of global variable

    if playerGo==False:#switches between player turn and computer turn
        playerGo=True
    elif playerGo==True:
        playerGo=False


    while count<3:
        if board[0][count]==board[1][count]==board[2][count]:
            if board[0][count]==playLet:
                playerVic()
            elif board[0][count]==compLet:
                CompVic()
        count=count+1
    count =0
    #cycles through horizontal coloumns to check for victory

    while count<3:
        if board[count][0]==board[count][1]==board[count][2]:
            if board[count][0]==playLet:
                playerVic()
            elif board[count][0]==compLet:
                CompVic()
        count=count+1
    count=0
    #cycles through vertical coloumns to check for victory

    if board[count][count]==board[count+1][count+1]==board[count+2][count+2]:
            if board[count][count]==playLet:
                playerVic()
            elif board[count][count]==compLet:
                CompVic()
    elif board[count][count+2]==board[count+1][count+1]==board[count+2][count]:
            if board[count][count+2]==playLet:
                playerVic()
            elif board[count][count+2]==compLet:
                CompVic()
    #checks diagonals for victory

    limitcheck=0        
    for i in range (len(options)):
        if options[i]=="X" or options[i]=="O":
            limitcheck=limitcheck+1
            if limitcheck==9:
                CompVic()
                #checks if all tiles are taken and ends the game if the program determines they are
    output()

def playerVic():
    restart=input("You win,type Rematch to play again ")
    inp2=restart.upper()
    if inp2=="REMATCH":
        reset()
    else:
        exit()
    #allows player to play multiple times or close terminal
    
def CompVic():
    restart=input("You have lost, type Rematch to play again ")
    inp2=restart.upper()
    if inp2=="REMATCH":
        reset()
    else:
        exit()
    

def reset():
    reOps=1
    for i in range(len(options)):
        options[i]=reOps
        reOps=reOps+1
    #resets options array from 1 unitl array length
    
    reBoard=1
    for i in range(gridX):
        for j in range(gridY):
            board[i][j]=reBoard
            reBoard=reBoard+1
    #resets board array from 1 until array length
    move()


start()
#starts game