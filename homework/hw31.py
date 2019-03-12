def main():
    li=getInput()
    out(li)
    return;

def getInput():
    li=[]
    li=input().split()
    return li;

def out(li):
    ans=[]
    for i in li:
        if(i=='.'):
            break;
        ans.append(check(i))
    for i in range(len(ans)):
        print("%s - %s"%(li[i],ans[i]))
    return;

def check(s):
    if('0'<=s[0]<='9'):
        for i in s:
            if(not('0'<=i<='9')):
                return 'Invalid ';
        return 'Number ';
    elif('a'<=s[0]<='z' or 'A'<=s[0]<='Z' or s[0]=='_'):
        for i in s:
            if(not('a'<=i<='z' or 'A'<=i<='Z' or i=='_' or '0'<=i<='9')):
                return 'Invalid ';
        return 'Identifier ';
    else:
        return 'Invalid ';
        
main()
