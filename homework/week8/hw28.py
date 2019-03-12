def main():
    guess,A,B=getInput()
    ans=judge(guess,A,B)
    output(ans)
    
def getInput():
    guess=[]
    A=[]
    B=[]
    for i in range(5):
        _input=input()
        g,AB=_input.split(',')
        guess.append(g)
        A.append(int(AB[0]))
        B.append(int(AB[2]))
    return guess,A,B;

def Fguess(data,guess,A,B):
    ans=[]
    for i in data:
        a=bg=bd=0
        for k in range(4):
            if(i[k]==guess[k]):
                a+=1
            if(i[k] in guess):
                bg+=1
            if(guess[k] in i):
                bd+=1
        if(bg>bd):
            if(a==A and bd-a==B):
                ans.append(i)
        else:
            if(a==A and bg-a==B):
                ans.append(i)
    return ans;
    
def judge(guess,A,B):
    n=0
    data=[str(i//1000)+str((i//100)%10)+str((i//10)%10)+str(i%10) for i in range(10000)]
    while(len(data)>1):
        n+=1
        data=Fguess(data,guess[n],A[n],B[n])
        if(n>=len(guess)):
            break;
    return data;

def output(ans):
    for i in ans:
        print(int(i))
    return;

main()
