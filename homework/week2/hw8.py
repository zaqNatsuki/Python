import math
def getAnswer(a,b,c,D):
    sqrtD=math.sqrt(abs(D))
    if(D>=0):
        x1=(-b+sqrtD)/(2*a)
        x2=(-b-sqrtD)/(2*a)
        return x1, x2;
    else:
        x11=x21=-b/(2*a)
        x12=x22=sqrtD/(2*a)
        #x22=-sqrtD/(2*a)
        return x11,x12,x21,x22;

def main():
    a=int(input())
    b=int(input())
    c=int(input())
    D=(b*b-4*a*c)
    if(D>=0):
        x1,x2=getAnswer(a,b,c,D)
        print("%.1f"%x1)
        print("%.1f"%x2)
    else:
        x11,x12,x21,x22=getAnswer(a,b,c,D)
        print("%.1f+%.1fi"%(x11,x12))
        print("%.1f-%.1fi"%(x21,x22))

main()
