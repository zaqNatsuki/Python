def score(li):
    l0=li[0]
    l1=li[1]
    total=0
    mode=0
    if(l0[0]==10):
        if(l1[0]==10):
            total+=10+10+l1[2]
            total+=10+l1[2]+l1[3]
        elif(l1[0]+l1[1]==10):
            total+=10+l1[0]+l1[1]
            total+=10+l1[2]
        else:
            total+=10+l1[0]+l1[1]
            total+=l1[0]+l1[1]
    elif(l0[0]+l0[1]==10):
        if(l1[0]==10):
            total+=10+10
            total+=10+l1[2]+l1[3]
        elif(l1[0]+l1[1]==10):
            total+=10+l1[0]
            total+=10+l1[2]
        else:
            total+=10+l1[0]
            total+=l1[0]+l1[1]
    else:
        if(l1[0]==10):
            total+=l0[0]+l0[1]
            total+=10+l1[2]+l1[3]
        elif(l1[0]+l1[1]==10):
            total+=l0[0]+l0[1]
            total+=10+l1[2]
        else:
            total+=l0[0]+l0[1]+l1[0]+l1[1]
    print(total)
    return;

def main():
    li=[]
    for i in range(2):
        _input=input()
        li.append(list(map(int,_input.split(" "))))
    score(li)

main()
