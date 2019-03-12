def main():
    num=int(input())
    draw(num)
def drawSignal(x,n):
    for i in range(0,x):
        print("#",end='')

def drawNumber(x,n):
    for i in range(2*n-x,0,-1):
        print(i,end='')

def draw(n):
    i=n
    while(i<2*n):
        drawSignal(i,n)
        drawNumber(i,n)
        print()
        i+=1

main()
