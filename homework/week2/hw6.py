def getTriangle(a, b, c):
    if(a<=0 or b<=0 or c<=0 or a+b<=c or b+c<=a or a+c<=b):
        return 1;
    elif(a==b==c):
        return 2;
    elif(a==b or a==c or b==c):
        return 3;
    else:
        return 4;

def output(t):
    if(t==1):
        print("not triangle")
    elif(t==2):
        print("equilateral triangle")
    elif(t==3):
        print("isosceles triangle")
    else:
        print("triangle")

def main():
    x=input()
    y=x.split(" ")
    a=int(y[0])
    b=int(y[1])
    c=int(y[2])
    t=getTriangle(a,b,c)
    output(t)

main()
