def main():
    li=[]
    again=1
    while(again!=-1):
        _input=input()
        try:
            if(int(_input)==-1):
                break;
        except:
            li.append(list(map(int,_input.split(" "))))
    checkAndDraw(li)

def checkAndDraw(lis):
    for i in range(len(lis)):
        shape=lis[i][0]
        line=lis[i][1]
        if(shape==1):
            if(1<=line<=18 and line%2==1):
                for i in range(line):
                    drawdot(shape,line,i)
                    drawnum(shape,line,i)
                print('')
            else:
                print("E")
                continue;
        elif(shape==2):
            if(1<=line<=5):
                for i in range(line):
                    drawdot(shape,line,i)
                    drawnum(shape,line,i)
                print('')
            else:
                print("E")
                continue;
        else:
            print("E")
            continue;

def drawdot(shape,_line,i):
    if(shape==1):
        _line=_line//2
        if(i<=_line):
            print((_line-i)*'.',end='')
        else:
            print((i-_line)*'.',end='')
    else:
        print(i*'.',end='')
    
def drawnum(shape,line,i):
    if(shape==1):
        _line=(line//2)
        if(i<=_line):
            for x in range(i+1):
                print(x+1,end='')
            for x in range(i,0,-1):
                print(x,end='')
            print("")
        else:
            for x in range(line-i):
                print(x+1,end='')
            for x in range(line-1,i,-1):
                print(x-i,end='')
            print("")
    else:
        n=2*(line-i)-1
        for x in range(line-i):
            print(n,end='')
            n-=2
        n=1
        for x in range(line-i-1):
            n+=2
            print(n,end='')
        print('')

main()
