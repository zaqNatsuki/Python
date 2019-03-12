def main():
    li,error,roll=getInput()
    if(error==-1):
        print("E")
    else:
        out(li,roll)
    return;

def getInput():
    li=[]
    column,row=map(int,input().split(' '))
    for i in range(column):
        li.append(list(input()))
    roll=list(input())
    for i in range(len(li)):
        if(len(li[i])!=row):
            return [],-1,[];
    if(not(1<=column<=10 and 1<=row<=10)):
        return [],-1;
    for i in roll:
        if(not(1<=int(i)<=3)):
            return [],-1,[];
    return li,1,roll;

def out(li,roll):
    for i in roll:
        column=len(li)
        row=len(li[0])
        li=Froll(i,li,column,row)
    for i in li:
        for j in i:
            print(j,end='')
        print('')
    return;

def Froll(mode,li,column,row):
    new=[]
    if(mode=='1'):#turn right 90 degree
        for i in range(row):
            r=[]
            for j in range(column-1,-1,-1):
                r.append(li[j][i])
            new.append(r)
        return new;
    elif(mode=='2'):#turn left 90 degree
        for i in range(row-1,-1,-1):
            r=[]
            for j in range(column):
                r.append(li[j][i])
            new.append(r)
        return new;
    else:#turn right 180 degree
        for i in range(column-1,-1,-1):
            r=[]
            for j in range(row-1,-1,-1):
                r.append(li[i][j])
            new.append(r)
        return new;
                
main()
