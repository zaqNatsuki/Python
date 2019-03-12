def main():
    t1=t11=t12=t2=t21=t22=t3=t31=t32=0
    c1=int(input())
    h1=int(input())
    if(h1!=2):
        t1=int(input())
        cn1=check(c1,h1,t1)
    elif(h1==2):
        t11=int(input())
        t12=int(input())
        cn1=check(c1,h1,t11,t12)
    c2=int(input())
    h2=int(input())
    if(h2!=2):
        t2=int(input())
        cn2=check(c2,h2,t2)
    elif(h2==2):
        t21=int(input())
        t22=int(input())
        cn2=check(c2,h2,t21,t22)
    c3=int(input())
    h3=int(input())
    if(h3!=2):
        t3=int(input())
        cn3=check(c3,h3,t3)
    elif(h3==2):
        t31=int(input())
        t32=int(input())
        cn3=check(c3,h3,t31,t32)
    if(cn1!=-1 and cn2!=-1 and cn3!=-1):
        sameTime(c1,h1,t1,t11,t12,c2,h2,t2,t21,t22,c3,h3,t3,t31,t32)
    else:
        print(-1)

def check(*_input):
    li=_input
    if(li[0]>=1000 and li[0]<10000):
        if(li[1]==1):
            n=li[2]
            if(n<60 and n>10 and n%10<9 and n%10>0):
                return 1;                           
            else:                                   
                return -1;
        elif(li[1]==2):
            n=li[2]
            if(n<60 and n>10 and n%10<9 and n%10>0):
                n=li[3]
                if(n<60 and n>10 and n%10<9 and n%10>0):
                    return 1;
                else:
                    return -1;
            else:
                return -1;
        else:
            return -1;
    else:
        return -1;

def sameTime(*_input):
    correct=1
    li=_input
    tl1=[li[2],li[3],li[4]]
    tl2=[li[7],li[8],li[9]]
    tl3=[li[12],li[13],li[14]]
    for i in tl1:
        if(i!=0):
            for j in tl2:
                if(j!=0 and i==j):
                    correct=0
                    print("%d,%d,%d"%(li[0],li[5],i))
            for j in tl3:
                if(j!=0 and i==j):
                    correct=0
                    print("%d,%d,%d"%(li[0],li[10],i))
    for i in tl2:
        if(i!=0):
            for j in tl3:
                if(j!=0 and i==j):
                    correct=0
                    print("%d,%d,%d"%(li[5],li[10],i))
    if(correct==1):
        print("correct")

main()
