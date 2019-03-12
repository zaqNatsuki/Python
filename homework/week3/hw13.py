def main():
    r91=int(input())
    r92=int(input())
    #r9=getScore(r91,r92)
    r101=int(input())
    r102=int(input())
    #r10=getScore(r101,r102)
    if(r101==10):
        r11=int(input())
        total=r91+r92+r101+r102+r11
    else:
        total=r91+r92+r101+r102
    output(total)

def getScore(n1,n2):
    if(n1+n2)>10:
        n=10
    else:
        n=n1+n2
    return n;

def output(total):
    print(total)

main()
