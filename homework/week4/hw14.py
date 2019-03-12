def main():
    en1=input()             #enter
    le1=input()             #leave
    en2=input()
    le2=input()
    en3=input()
    le3=input()
    c1=check(en1,le1)      #correct
    c2=check(en2,le2)
    c3=check(en3,le3)
    if(c1!=-1):
        fee1=payFee(en1,le1)
        print(fee1)
    else:
        print("error")
    if(c2!=-1):
        fee2=payFee(en2,le2)
        print(fee2)
    else:
        print("error")
    if(c3!=-1):
        fee3=payFee(en3,le3)
        print(fee3)
    else:
        print("error")

def check(*_input):
    correct=1
    li=[]
    for i in _input:
        li.append(i.split(":"))
    for i in li:
        if(int(i[0])<0 or int(i[0])>23):
            #print("error")
            return -1;
        elif(int(i[1])<0 or int(i[1])>59):
            #print("error")
            return -1;
    #print("correct")
    return correct;

def payFee(enter,leave):
    fee=0
    en=enter.split(":")
    le=leave.split(":")
    for i in range(2):
        en[i]=int(en[i])
        le[i]=int(le[i])
    mn=le[1]-en[1]
    if(mn<0):
        hr=le[0]-en[0]-1
        mn=60+mn
    else:
        hr=le[0]-en[0]
    if(hr<2 or (hr==2 and mn==0)):
        fee=hr*60+mn//30*30
        return fee;
    elif((hr==2 and mn>0)or 2<hr<4):
        if(mn==0):
            fee=120+(hr-2)*80
        elif(mn==30):
            fee=120+(hr-2)*80+40
        else:
            fee=120+(hr-2)*80+(mn//30+1)*40
        return fee;
    elif(hr>=4):
        if(mn==0):
            fee=120+160+(hr-4)*120
        elif(mn==30):
            fee=120+160+(hr-4)*120+60
        else:
            fee=120+160+(hr-4)*120+(mn//30+1)*60
        return fee;

main()
