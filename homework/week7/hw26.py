def main():
    try:
        _input=int(input())
        if(_input>0):
            compute(_input)
        else:
            print("E")
            return;
    except:
        print("E")
        return;

def compute(num):
    for i in range(1,num+1):
        total=0
        li=[]
        for j in range(i,num+1):
            total+=j
            li.append(j)
            if(total==num):
                for k,xk in enumerate(li):
                    if(k==len(li)-1):
                        print(xk)
                    else:
                        print("%d+"%xk,end='')
                break;
            elif(total>num):
                break;
main()
