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
        a=ba=bg=0
        for j in range(4):
            if(li[i][j]==li[0][j]):
                a+=1
            if(li[i][j] in li[0]):
                bg+=1
            if(li[0][j] in li[i]):
                ba+=1
        if(ba>bg):
            print("%dA%dB"%(a,bg-a))
        else:
            print("%dA%dB"%(a,ba-a))
    return;

main()
