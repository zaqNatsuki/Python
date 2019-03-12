def main():
    s=input()
    try:
        x1,y1,x2,y2=map(int,s.split(' '))
        if(x1==x2 and y1==y2):
            print("Error!")
            return;
        f1(x1,y1,x2,y2)
        f2(x1,y1,x2,y2)
    except:
        print("Error!")
    return;

def output(key,m1=0,b1=0,m2=0,b2=0):
    if(m1>0 and m2<0):
        m1=-m1
        m2=-m2
    if(b1>0 and b2<0):
        b1=-b1
        b2=-b2
    if(m1%m2==0):
        if(int(m1/m2)==1):
            if(b1%b2==0):
                print("y=x%+d"%(int(b1/b2)))
            else:
                if(key==1):
                    print("y=x%+.2f"%(b1/b2))
                else:
                    print("y=x+%d/%d"%(b1,b2))
        elif(int(m1/m2)==-1):
            if(b1%b2==0):
                print("y=-x%+d"%(int(b1/b2)))
            else:
                if(key==1):
                    print("y=-x%+.2f"%(b1/b2))
                else:
                    print("y=-x+%d/%d"%(b1,b2))
        else:
            if(b1%b2==0):
                print("y=%dx%+d"%(int(m1/m2),int(b1/b2)))
            else:
                if(key==1):
                    print("y=%dx%+.2f"%(int(m1/m2),b1/b2))
                else:
                    print("y=%dx+%d/%d"%(int(m1/m2),b1,b2))
    else:
        if(b1%b2==0):
            if(key==1):
                print("y=%.2fx%+d"%(m1/m2,int(b1/b2)))
            else:
                print("y=%d/%dx%+d"%(m1,m2,int(b1/b2)))
        else:
            if(key==1):
                print("y=%.2fx%+.2f"%(m1/m2,b1/b2))
            else:
                print("y=%d/%dx%+d/%d"%(m1,m2,b1,b2))
    return;

def f1(x1,y1,x2,y2):
    if(y1==y2):
        print("y=%d"%y1)
    elif(x1==x2):
        print("x=%d"%x1)
    else:
        m1=y1-y2
        m2=x1-x2
        b1=x2*y1-x1*y2
        b2=x2-x1
        output(1,m1,b1,m2,b2)
    return;

def f2(x1,y1,x2,y2):
    if(y1==y2):
        print("y=%d"%y1)
    elif(x1==x2):
        print("x=%d"%x1)
    else:
        m1=y1-y2
        m2=x1-x2
        b1=x2*y1-x1*y2
        b2=x2-x1
        output(2,m1,b1,m2,b2)
    return;

main()
