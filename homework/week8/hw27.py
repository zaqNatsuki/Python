def main():
    _input=input()
    n1,n2=map(int,_input.split(" "))
    if(n2<=10):
        print('0')
    else:
        li=compute(n1,n2)
        output(li)
    return;

def compute(n1,n2):
    li=[]
    for i in range(n1,n2+1):
        no=0
        s=str(i)
        _len=len(s)
        for j in range(_len//2):
            if(not(s[j]==s[0-j-1])):
                no+=1
                break;
        if(no==0):
            li.append(i)
    return li;

def output(li):
    for i,x in enumerate(li):
        if(i==0):
            print(x,end='')
        else:
            print(" %d"%x,end='')

main()
