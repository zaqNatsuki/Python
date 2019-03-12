def getAnswer(a,b,c,d,e):
    average=(a+b+c+d+e)/5
    Variance=((average-a)**2+(average-b)**2+(average-c)**2+(average-d)**2+(average-e)**2)/5
    Sd=Variance**0.5
    print("%.2f"%Variance)
    print("%.2f"%Sd)
    print("%.2f"%average)

def main():
    x=input()
    y=x.split(" ")
    a=int(y[0])
    b=int(y[1])
    c=int(y[2])
    d=int(y[3])
    e=int(y[4])
    getAnswer(a,b,c,d,e)

main()
