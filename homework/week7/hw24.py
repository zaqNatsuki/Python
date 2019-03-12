def main():
    num1=input()
    num2=input()
    n1,d1=map(int,num1.split('/'))      #n=分子
    n2,d2=map(int,num2.split('/'))      #d=分母
    if(n1==0 or d1==0 or n2==0 or d2==0):
        print("ERROR\nERROR\nERROR\nERROR")
        return;
    add(n1,d1,n2,d2)
    minus(n1,d1,n2,d2)
    multiply(n1,d1,n2,d2)
    divided(n1,d1,n2,d2)

def add(n1,d1,n2,d2):
    gcd=getGCD(d1,d2)
    if(gcd==1):
        d=d1*d2
        n=n1*d2+n2*d1
        output(n,d)
    else:
        if(d1==d2):
            d=d1
            n=n1+n2
            output(n,d)
        else:
            d=(d1/gcd)*d2
            n=n1*(d/d1)+n2*(d/d2)
            output(n,d)
    return;
            
def minus(n1,d1,n2,d2):
    gcd=getGCD(d1,d2)
    if(gcd==1):
        d=d1*d2
        n=n1*d2-n2*d1
        output(n,d)
    else:
        if(d1==d2):
            d=d1
            n=n1-n2
            output(n,d)
        else:
            d=(d1/gcd)*d2
            n=n1*(d/d1)-n2*(d/d2)
            output(n,d)
    return;

def multiply(n1,d1,n2,d2):
    n=n1*n2
    d=d1*d2
    output(n,d)
    return;

def divided(n1,d1,n2,d2):
    n=n1*d2
    d=d1*n2
    output(n,d)
    return;

def getGCD(d1,d2):
    if(d1<d2):
        temp=d1
        d1=d2
        d2=temp
    while(d2>0):
        temp=d2
        d2=d1%d2
        d1=temp
    return d1;

def output(n,d):
    if(n==0 or d==0):
        print(0)
    else:
        gcd=getGCD(abs(n),abs(d))
        n=n/gcd
        d=d/gcd
        if(abs(n)>abs(d)):
            if(n<0):
                print("-%d(%d/%d)"%(abs(n)//d,n%d,d))
            elif(n>0):
                print("%d(%d/%d)"%(n//d,n%d,d))
        elif(abs(n)<abs(d)):
            print("%d/%d"%(n,d))
        else:
            print("%d"%(n/d))

main()
