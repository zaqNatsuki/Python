bigthenten=['A','B','C','D','E','F']
def main():
    _input=input()
    try:
        base,number=_input.split(" ")
        if(base.isdigit() and number.isdigit()):
            base=int(base)
            number=int(number)
            if(not(2<=base<=16 and 0<=number<=1000000000)):
               print("E")
               return 0;
            convert=baseConvert(base,number)
            output(convert)
        else:
            print("E")
    except:
        print("E")

def baseConvert(base,number):
    convert=[]
    _convert=[]
    while(number>0):
        n=number%base
        if(n<10):
            convert.append(n)
        else:
            convert.append(bigthenten[n-10])
        number=number//base
    for i in range(len(convert)-1,-1,-1):
        _convert.append(convert[i])
    return _convert;

def output(convert):
    for i in convert:
        print(i,end='')

main()
