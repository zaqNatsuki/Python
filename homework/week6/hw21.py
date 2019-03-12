def main():
    answer=[]
    num=int(input())
    for i in range(num):
        line=int(input())
        li=[]
        if(line<=5000):
            for j in range(line):
                _input=input()
                li.append(list(map(int,_input.split(" "))))
        else:
            print("E")
            return;
        answer.append(check(li,line))
    for i in answer:
        print(i)

def check(li,line):
    li.sort()
    total=0
    n=0
    for i in li:
        for j in i:
            if(0<=j<=60000):
                continue;
            else:
                return "E";
        if(n<line-1):
            if(li[n][1]>=li[n+1][1]):
                li.remove(li[n+1])
            elif(li[n+1][0]<=li[n][1]<=li[n+1][1]):
                li[n][1]=li[n+1][1]
                li.remove(li[n+1])
            elif(li[n][1]<li[n+1][0]):
                n+=1
    for i in li:
        total+=(i[1]-i[0])
    return total;
main()
