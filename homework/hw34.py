def main():
    li=[]
    li=getInput()
    error=check(li)
    out(error)
    return;

def getInput():
    li=[]
    for i in range(9):
        li.append(list(map(int,input().split())))
    return li;

def check(li):
    error=0
    row=column=0
    for i in range(9):
        num=[x for x in range(1,10)]
        num1=[x for x in range(1,10)]
        for j in range(9):
            if(li[i][j] in num):
                num.remove(li[i][j])
            else:
                return -1;
        for j in range(9):
            if(li[j][i] in num1):
                num1.remove(li[j][i])
            else:
                return -1;
        num2=[x for x in range(1,10)]
        row=i//3
        column=i%3
        for j in range(row*3,3*(row+1)):
            for k in range(column%3*3,3*(column%3+1)):
                if(li[j][k] in num2):
                    num2.remove(li[j][k])
                else:
                    return -1;
    return 1;

def out(error):
    if(error==-1):
        print('No')
    else:
        print('Yes')
    return;

main()
