def main():
    num=input()
    num=convert(num)
    if(num!=0.1):
        prime=getPrime(num)
        output(prime)
    else:
        print("Error!")
    return;
        
def getPrime(num):
    prime=2
    for i in range(2,num):
        count=0
        for j in range(2,i):
            if(i%j==0):
                count+=1
                break;
        if(count==0):
            prime=i
    return prime;

def convert(num):
    try:
        num=int(num)
        if(2<=num<=1000):
            return num;
        elif(num==0 or num==1):
            return 1000;
        elif(num<0):
            return num*-11;
        else:
            return 0.1;
    except:
        if(num.count('.')==1):
            if(eval(num)>=0):
                return int(eval(num));
            else:
                x=num.find('.')
                num=int(num[x+1:])
                return num;
        else:
            return 0.1;

def output(num):
    print(num)

main()
