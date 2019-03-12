def main():
    li=[]
    while(1):
        _input=input()
        try:
            if(int(_input)==-1):
                break;
        except:
            li.append(list(map(int,_input.split(" "))))
    guess(li)

def guess(li):
    for i in range(1,len(li)):
        a=b1=b2=c=0
        for j,xj in enumerate(li[i]):
            if(li[0][j] in li[i]):
                b1+=1
            if(li[0][j]==xj):
                a+=1
        for j,xj in enumerate(li[i]):
            if(xj in li[0]):
                if(li[0].count(xj)!=li[i].count(xj)):
                    c=abs(li[0].count(xj)-li[i].count(xj))
                b2+=1          
        if(b1>b2):
            print("%dA%dB"%(a,b2-a))
        elif(b1<b2):
            print("%dA%dB"%(a,b1-a))
        else:
            print("%dA%dB"%(a,b1-a-c))
        
main()
