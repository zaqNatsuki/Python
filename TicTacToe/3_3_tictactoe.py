import os
import random

def main():
    while True:
        mode,player,position,first,tictac=initialize()
        mode=gameMode()
        if(mode=='3'): break;
        elif(mode=='2'):
            first=getFirst()
        while True:
            if(mode=='1'):          #人vs人
                position=getInput(player)
                if(CheckPosition(tictac,position)):
                    place(tictac,player,int(position))
                    draw(tictac)
                    if(checkWin(tictac,first,mode)):
                        break;
                    player+=1
            elif(mode=='2'):        #人vs電腦
                if(first==1):       #人先
                    position=getInput(0)
                    if(CheckPosition(tictac,position)):
                        place(tictac,0,int(position))
                        draw(tictac)
                        if(checkWin(tictac,first,mode)):
                            break;
                        computer(tictac,first)
                        if(checkWin(tictac,first,mode)):
                            break;
                elif(first==2):     #電腦先
                    computer(tictac,first)
                    if(checkWin(tictac,first,mode)):
                        break;
                    position=getInput(1)
                    if(CheckPosition(tictac,position)):
                        place(tictac,1,int(position))
                        draw(tictac)
                        if(checkWin(tictac,first,mode)):
                            break;
            else:
                print("input Error")
                break;
    return;

def initialize():
    tictac=[' ' for i in range(9)]
    return 0,0,0,0,tictac;

def getFirst():
    print("1-->人先、2-->電腦先")
    first=int(input())
    return first;

def getInput(player):
    if(player%2==0):
        print("O: ",end='')
        position=input()
    else:
        print("X: ",end='')
        position=input()
    return position;

def gameMode():
    print("1=人vs人、2=人vs電腦、3=離開")
    print("請輸入遊戲模式:",end='')
    mode=input()
    return mode;

def CheckPosition(tictac,position):
    if(position>'9' or position<'1'):
        print("Input Error")
        return 0;
    elif(tictac[int(position)-1]!=' '):
        print("Same position Error")
        return 0;
    return 1;

def place(tictac,player,position):
    if(player%2==0):
        tictac[position-1]='O'
    else:
        tictac[position-1]='X'
    return;

def draw(tictac):
    os.system("cls")
    for i in range(2,-1,-1):
        li=[tictac[i*3+j] for j in range(3)]
        for j in li:
            print("|",j," ",sep='',end='')
        print("|")
    print()
    return;

def checkWin(tictac,first,mode):
    for i in range(3):
        row=[tictac[i*3+j] for j in range(3)]
        column=[tictac[i+j*3] for j in range(3)]
        if(checkLine(row,first,mode)):
            return 1;
        if(checkLine(column,first,mode)):
            return 1;
        slide=[tictac[4*i] for i in range(3)]
        if(checkLine(slide,first,mode)):
            return 1;
        slide=[tictac[2*i] for i in range(1,4)]
        if(checkLine(slide,first,mode)):
            return 1;
    if(tictac.count(' ')==0):
        print("Draw")
        return 1;
    return 0;

def checkLine(line,first,mode):
    numO=line.count('O')
    numX=line.count('X')
    if(mode=='1'):
        if(numO==3):
            print("Player O Win.")
            return 1;
        elif(numX==3):
            print("Player X Win.")
            return 1;
    elif(mode=='2'):
        if(first==1):       #人先
            if(numO==3):    #人贏
                print("Player Win.")
                return 1;
            elif(numX==3):  #電腦贏
                print("Computer Win.")
                return 1;
        elif(first==2):
            if(numO==3):    #電腦贏
                print("Computer Win.")
                return 1;
            elif(numX==3):  #人贏
                print("Player Win.")
                return 1;
    return 0;

def computer(tictac,first):
    corner=[1,3,7,9]
    unPlace=[]
    for i,xi in enumerate(tictac):
        if(xi==' '):
            unPlace.append(i+1)
        else:
            if(i+1 in corner):
                corner.remove(i+1)
    if(first==1):       #人先
        if(readyWin(tictac,first)):
            draw(tictac)
            return;
        elif(tictac[4]==' '):
            place(tictac,first,5)
        elif(len(corner)>0):
            place(tictac,first,random.choice(corner))
        else:
            place(tictac,first,random.choice(unPlace))
    elif(first==2):
        if(tictac[4]==' '):
            place(tictac,first,5)
        elif(readyWin(tictac,first)):
            draw(tictac)
            return;
        elif(len(corner)>0):
            place(tictac,first,random.choice(corner))
        else:
            place(tictac,first,random.choice(unPlace))
    draw(tictac)
    return;

def readyWin(tictac,first):
    for i in range(3):
        row=[tictac[i*3+j] for j in range(3)]
        column=[tictac[i+j*3] for j in range(3)]
        ready,position=readyLine(row,first)
        if(ready):
            position+=i*3+1
            place(tictac,first,position)
            return 1;
        ready,position=readyLine(column,first)
        if(ready):
            position=position*3+i+1
            place(tictac,first,position)
            return 1;
    slide=[tictac[4*i] for i in range(3)]
    ready,position=readyLine(slide,first)
    if(ready):
        position=position*4+1
        place(tictac,first,position)
        return 1;
    slide=[tictac[2*i] for i in range(1,4)]
    ready,position=readyLine(slide,first)
    if(ready):
        position=(position+1)*2+1
        place(tictac,first,position)
        return 1;
    return 0;

def readyLine(line,first):
    numO=line.count('O')
    numX=line.count('X')
    if(first==2):       #電腦先
        if(numO==2 and numX==0):
            return 1,line.index(' ');
        elif(numX==2 and numO==0):
            return 1,line.index(' ');
        else:
            return 0,0;
    elif(first==1):     #人先
        if(numX==2 and numO==0):
            return 1,line.index(' ');
        elif(numO==2 and numX==0):
            return 1,line.index(' ');
        else:
            return 0,0;

main()
