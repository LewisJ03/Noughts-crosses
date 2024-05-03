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
            print("",board[i][j],end=" |")  #loops through 2D array to create boardgame table
    print("\n-------------")    #checks if either has player has won before asking player for their next move
    if playerGo==1:
        move()
    elif playerGo==0:
        compPick()
    else:
        print("oh no its broken")

def move():
    taken=0 #tracks if space is avaliable to take(0 is taken, 1 is not taken)
    playInp=input("please select the postition you would like ")
    try:
        inp1=int(playInp)   #converts to integer so program doesnt crash on input of Char
    except:
        print("ERROR:invalid input")
        move()

    if(inp1>9 or inp1<1):
        print("ERROR:out of bounds")    #restarts after out of bounds input
        move()

    for i in range(gridX):
        for j in  range(gridY):
            if(inp1==board[i][j]):
                board[i][j]=playLet #replaces position of 2D array with X
                taken=1    #logged as not taken
    
    for i in range(len(options)):
        if inp1==options[i]:
            options[i]=playLet  #updates computers avaliable numbers

    if (taken==0):
        print("Space occupied")
        move()
    elif(taken==1):
        winCheck()  #computers turn


def compPick():
    rows=[[0,0],[1,0],[2,0]]#rows correlate with number:0-top,1-middle,2-bottom
    columns=[[0,0],[1,0],[2,0]]#0-left,1-middle,2-right
    diagonal=[[0,0],[1,0]]#0-top left to  bottom right,1 top right to bottom left
    #second number realtes to weight of row/column

    loop=0
    loopRow=0
    weight=0

    for x in range(len(options)):#checks weight of rows
        if options[x]==playLet:
            weight -=5
        elif options[x]==compLet:
            weight+=1
        loop+=1
        if loop==3:
            rows[loopRow][1]=weight
            loopRow+=1
            loop=0
            weight=0
    
    for y in range(gridY):#checks weight of columns
        pointer=y
        for c in range(gridY):
            if options[pointer]==playLet:
                weight-=5
            elif options[pointer]==compLet:
                weight+=1
            pointer+=3
        columns[y][1]=weight
        weight=0

    diagLoop=0
    for x in range(gridX):#checks weight of top left to bottom right
        if options[diagLoop]==playLet:
            weight-=5
        elif options[diagLoop]==compLet:
            weight+=1
        diagLoop=diagLoop+(gridX+1)
    diagonal[0][1]=weight
    weight=0

    diagLoop=gridX-1#-1 otherwise would read options[3] which is 4
    for x in range(gridX):#checks weight of bottom left to top right
        if options[diagLoop]==playLet:
            weight-=5
        elif options[diagLoop]==compLet:
            weight+=1 
        diagLoop=diagLoop+(gridX-1)
    diagonal[1][1]=weight
    weight=0

    midpoint=(round(gridX/2))-1
    #sets midpoint of row/column if perfect square

    if (rows[midpoint][1]==0 or columns[midpoint][1]==0) and options[round(len(options)/2)]!=round(len(options)/2):
        options[round(len(options)/2)]=compLet
        board[midpoint][midpoint]=compLet#picks middle if not occupied
        winCheck()
    
    #if row or column has value 2 select
    for i in range(gridX):
        if rows[i][1]==2:
            rowInspect=i*gridX#gives 0,3,6
            for j in range(gridX):
                options[rowInspect]=compLet
                board[i][j]=compLet
                rowInspect+=1
            winCheck()

        elif columns[i][1]==2:
            columnInspect=i
            for j in range(gridY):
                options[columnInspect]=compLet
                board[j][i]=compLet
                columnInspect+=3
            winCheck()

        elif diagonal[0][1]==2:#sets all characters to computer letter if weight=2 during a diagonal
            diagLoop=0
            for x in range(gridX):
                options[diagLoop]=compLet
                board[x][x]=compLet
                diagLoop=diagLoop+(gridX+1)
            winCheck()
        elif diagonal[1][1]==2:
            diagLoop=gridX-1
            for j in range(gridX):
                options[diagLoop]=compLet
                rightLeft=gridX-1
                board[j][rightLeft]=compLet
                diagLoop=diagLoop+(gridX-1)
                rightLeft-=1
            winCheck()

    #if row or column has value -10 select
    for i in range(gridX):
        if rows[i][1]==-10:
            rowInspect=i*gridX#gives 0,3,6
            for j in range(gridX):
                if options[rowInspect]!=playLet:
                    options[rowInspect]=compLet
                    board[i][j]=compLet
                rowInspect+=1
            winCheck()

        elif columns[i][1]==-10:
            columnInspect=i
            for j in range(gridY):
                if options[columnInspect]!=playLet:
                    options[columnInspect]=compLet
                    board[j][i]=compLet
                columnInspect+=3
            winCheck()

        elif diagonal[0][1]==-10:
            diagLoop=0
            for x in range(gridX):
                if options[diagLoop]!=playLet:
                    options[diagLoop]=compLet
                    board[x][x]=compLet
                diagLoop=diagLoop+(gridX+1)
            winCheck()
        elif diagonal[1][1]==-10:
            diagLoop=gridX-1
            rightLeft=gridX-1
            for j in range(gridX):
                if options[diagLoop]!=playLet:
                    options[diagLoop]=compLet
                    board[j][rightLeft]=compLet
                diagLoop=diagLoop+(gridX-1)
                rightLeft-=1
            winCheck()

    #if row or column has value 1 select random of 2 remaning numbers
    #random number to select row or column then another for remaining spots
    for i in range(gridX):
        if rows[i][1]==1:
            added=False
            rowInspect=i*gridX
            for j in range(gridX):
                if added==False and options[rowInspect]!=compLet:
                    options[rowInspect]=compLet
                    board[i][j]=compLet
                    added=True
                rowInspect+=1
            winCheck()
            
        elif columns[i][1]==1:
            added=False
            columnInspect=i
            for j in range(gridY):
                if added==False and options[columnInspect]!=compLet:
                    options[columnInspect]=compLet
                    board[j][i]=compLet
                    added=True
                columnInspect+=3
            winCheck()
        
    if diagonal[0][1]==1:
        rand=random.randrange(0,gridX)
        diagRand=rand*(gridX+1)
        while options[diagRand]==compLet:#randomises which position is taken no matter which one already is
            rand=random.randrange(0,gridX)
        options[diagRand]=compLet
        board[rand][rand]=compLet
        winCheck()
        
    elif diagonal[1][1]==1:
        rand=random.randrange(0,gridX)
        diagPointer=(gridX+((gridX-1)*rand))-1
        while options[diagPointer]==compLet:
            rand=random.randrange(0,gridX)
        options[diagPointer]=compLet
        board[rand][gridX-rand]=compLet
        winCheck()

    #else select random(fail safe as shouldnt happen after first moves)
    #only happens if middle and middle has picked
    for i in range(gridX):
        rand=1
        rowInspect=i*gridX
        if rows[i][1]==0:
            #generate random numbewr between 0-2 and then assign that to the spot of the row
            while rand==1:#so that a corner is picked
                rand=random.randrange(0,gridX)
            options[(rowInspect+rand)]=compLet
            board[i][rand]=compLet
            winCheck()

        elif columns[i][1]==0:#failsafe as with 3x3 grid only middle already selected should lead to this option
            columnInspect=i
            while rand==1:
                rand=random.randrange(0,gridY)
            options[columnInspect+rand]=compLet
            board[rand][i]=compLet
            columnInspect+=3
            winCheck()

def winCheck():
    count=0
    global playerGo #needed to edit value of global variable

    if playerGo==False: #switches between player turn and computer turn
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
    count =0    #cycles through horizontal coloumns to check for victory

    while count<3:
        if board[count][0]==board[count][1]==board[count][2]:
            if board[count][0]==playLet:
                playerVic()
            elif board[count][0]==compLet:
                CompVic()
        count=count+1
    count=0    #cycles through vertical coloumns to check for victory

    if board[count][count]==board[count+1][count+1]==board[count+2][count+2]:
            if board[count][count]==playLet:
                playerVic()
            elif board[count][count]==compLet:
                CompVic()
    elif board[count][count+2]==board[count+1][count+1]==board[count+2][count]:
            if board[count][count+2]==playLet:
                playerVic()
            elif board[count][count+2]==compLet:
                CompVic()   #checks diagonals for victory

    limitcheck=0        
    for i in range (len(options)):
        if options[i]=="X" or options[i]=="O":
            limitcheck=limitcheck+1
            if limitcheck==9:
                draw()   #checks if all tiles are taken and ends the game if the program determines they are
    output()

def draw():
    for i in range(gridX):
        print("\n-------------")
        print ("|",end="")
        for j in range(gridY):
            print("",board[i][j],end=" |")
    print("\n-------------")
    restart=input("The game has come to a draw, type Rematch to play again ")
    inp2=restart.upper()
    if inp2=="REMATCH":
        reset()
    else:
        exit()
    

def playerVic():
    for i in range(gridX):
        print("\n-------------")
        print ("|",end="")
        for j in range(gridY):
            print("",board[i][j],end=" |")
    print("\n-------------")
    restart=input("You win,type Rematch to play again ")
    inp2=restart.upper()
    if inp2=="REMATCH":
        reset()
    else:
        exit()  #allows player to play multiple times or close terminal
    
def CompVic():
    for i in range(gridX):
        print("\n-------------")
        print ("|",end="")
        for j in range(gridY):
            print("",board[i][j],end=" |")
    print("\n-------------")
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
        reOps=reOps+1   #resets options array from 1 unitl array length
    
    reBoard=1
    for i in range(gridX):
        for j in range(gridY):
            board[i][j]=reBoard
            reBoard=reBoard+1   #resets board array from 1 until array length
    move()

start()