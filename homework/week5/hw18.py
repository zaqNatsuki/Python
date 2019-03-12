def main():
    total=0
    li=[]
    _input=input()
    try:
        num=int(_input)
        if(num>=0):
            li=getPrimeFactor(num)
            for i in li:
                answer=getFactorial(i)
                total+=answer
                output(i,answer)
            print("%d"%total)
        else:
            print("E")
    except:
        print("E")
    
def getPrimeFactor(num):                    #取質因數
    lis=[]
    for i in range(2,num+1):
        count=0
        if(num%i==0):
            if(i==2):
                lis.append(i)
            else:
                for j in range(2,i):
                    if(i%j==0):
                        count+=1
                        break;
                if(count==0):
                    lis.append(i)
    return lis;

def getFactorial(num):                      #算階乘
    f=1
    for i in range(1,num+1):
        f*=i
    return f;

def output(num,answer):
    print("%d,%d"%(num,answer))
    
main()
