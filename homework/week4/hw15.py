def main():
    shape=int(input())
    line=int(input())
    drawShape(shape,line)

def drawShape(shape,line):
    x=0
    _max=line//2+1
    if(shape==1):
        for i in range(line):
            if(i<_max):
                x+=1
            else:
                x-=1
            print(x*"*",end='')
            print()
    elif(shape==2):
        for i in range(line):
            if(i<_max):
                x+=1
            else:
                x-=1
            print((_max-x)*'.',end='')
            print(x*"*",end='')
            print() 
    elif(shape==3):
        x=-1
        dot=_max
        for i in range(line):
            if(i<_max):
                x+=2
                dot-=1
            else:
                x-=2
                dot+=1
            print(dot*".",end='')
            print(x*"*",end='')
            print()

main()
