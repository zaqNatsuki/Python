def main():
    c1=int(input())
    h1=int(input())
    if(h1!=2):
        t1=int(input())
        cn1=check(c1,h1,t1)
    elif(h1==2):
        t11=int(input())
        t12=int(input())
        cn1=check2(c1,h1,t11,t12)
    c2=int(input())
    h2=int(input())
    if(h2!=2):
        t2=int(input())
        cn2=check(c2,h2,t2)
    elif(h2==2):
        t21=int(input())
        t22=int(input())
        cn2=check(c2,h2,t21,t22)
    correct=1
    if(cn1!=-1 and cn2!=-1 ):
        if(h1==1):
            if(h2==1):
                if(t1==t2):
                    print("%d,%d,%d"%(c1,c2,t1))
                    correct=0
            elif(h2==2):
                if(t1==t21):
                    print("%d,%d,%d"%(c1,c2,t21))
                    correct=0
                elif(t1==t22):
                    print("%d,%d,%d"%(c1,c2,t22))
        elif(h1==2):
            ...
    else:
        print(-1)
    if(correct==1):
        print("correct")

def check(c,h,t):#c=課堂編號 h=小時數 t=上課時間
    if(c>=1000 and c<10000):#課堂編號4位數
        if(h==1):#if(小時數==1)
            if(t<60 and t>10 and t%10<9 and t%10>0):#先判斷是否介於10和60之間
                return 1;                           #是的話就能確定是星期一~五
            else:                                   #再判斷他是不是介於1~8節課之間
                return -1;
    
def check2(c,h,t1,t2):
    li=_input
    if(li[0]>=1000 and li[0]<10000):#課堂編號4位數
        if(h==2):#if(小時數==2)
            if(t1<60 and t1>10 and t1%10<9 and t1%10>0):
                if(t2<60 and t2>10 and t2%10<9 and t2%10>0):
                    return 1;
                else:
                    return -1;
            else:
                return -1;
        else:
            return -1;
    else:
        return -1;

def sameTime()
