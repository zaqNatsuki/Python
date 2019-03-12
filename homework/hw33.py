def main():
    li=getInput()
    answer=check(li)
    out(answer)
    return;

def getInput():
    li=[]
    for i in range(10):
        li.append(input().split())
    return li;

def check(li):
    ans=[]
    for row in range(10):
        for column in range(6):
            verify=[li[row][column+i] for i in range(5)]
            ans.extend(judge(verify,[row,column],1))        #horizontal
        for column in range(6):     #row column exchange
            verify=[li[column+i][row] for i in range(5)]
            ans.extend(judge(verify,[row,column],2))        #vertical
    for row in range(6):
        for column in range(6):
            verify=[li[row+i][column+i] for i in range(5)]
            ans.extend(judge(verify,[row,column],3))        #左上往右下
        for column in range(9,3,-1):
            verify=[li[row+i][column-i] for i in range(5)]
            ans.extend(judge(verify,[row,column],4))        #右上往左下
    ans.sort()
    return ans;

def judge(li,n,style):              #Vertical or Horizontal
    ans=[]
    if(li.count('1')==4):
        p=_find(li)
        if(style==1):           #horizontal
            ans.append([n[0],n[1]+p])
        elif(style==2):         #vertical
            ans.append([p+n[1],n[0]])
        elif(style==3):         #左上往右下
            ans.append([n[0]+p,n[1]+p])
        elif(style==4):         #右上往左下
            ans.append([n[0]+p,n[1]-p])
    return ans;

def _find(li):
    for i in range(5):
        if(li[i]=='0'):
            return i;

def out(ans):
    same=[]
    for i in ans:
        if(i!=[] and i not in same):
            same.append(i)
            for j in i:
                print(j,end=' ')
            print('')
    return;

main()
            
