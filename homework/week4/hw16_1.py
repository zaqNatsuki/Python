def main():
    n=int(input())
    draw(n)

def drawLeft(n):
    for i in range(n):
        print('#',end='')
    return;

def drawRight(i,n):
    print((n-i)*'#',end='')
    for i in range(i,0,-1):
        print(i,end='')
    return;

def draw(n):
    for i in range(n,0,-1):
        drawLeft(n)
        drawRight(i,n)
        print('')
    return;

main()
