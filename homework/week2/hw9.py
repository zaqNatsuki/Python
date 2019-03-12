def getDisCount(x,y,z):
    if(x>0 and x<=10):
        disA=1.00
    elif(x>10 and x<=20):
        disA=0.90
    elif(x>20 and x<=30):
        disA=0.85
    else:
        disA=0.80
    if(y>0 and y<=10):
        disB=1.00
    elif(y>10 and y<=20):
        disB=0.95
    elif(y>20 and y<=30):
        disB=0.85
    else:
        disB=0.80
    if(z>0 and z<=10):
        disC=1.00
    elif(z>10 and z<=20):
        disC=0.85
    elif(z>20 and z<=30):
        disC=0.80
    else:
        disC=0.70
    return disA,disB,disC;

def main():
    x=int(input())
    y=int(input())
    z=int(input())
    disA,disB,disC=getDisCount(x,y,z)
    total=disA*x*380+disB*y*1200+disC*z*180
    print("%d"%total)

main()
