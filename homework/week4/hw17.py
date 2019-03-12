def main():
    month=int(input())
    ly=int(input())             #last year
    ty=int(input())             #this year
    fee=payFee(month,ly,ty)
    output(fee)

def output(fee):
    print("%.2f"%fee)

def payFee(month,ly,ty):
    fee=0
    if(ty>=ly):                 #沒有較節電
        if(7<=month<=9):
            if(ty<=120):
                fee=ty*2.10
            elif(ty<=330):
                fee=ty*3.02
            elif(ty<=500):
                fee=ty*4.39
            elif(ty<=700):
                fee=ty*4.97
            elif(ty>700):
                fee=ty*5.63
        else:
            if(ty<=120):
                fee=ty*2.10
            elif(ty<=330):
                fee=ty*2.68
            elif(ty<=500):
                fee=ty*3.61
            elif(ty<=700):
                fee=ty*4.01
            elif(ty>700):
                fee=ty*4.50
    else:                       #有較節電
        if(7<=month<=9):
            if(ty<=120):
                fee=ty*2.10
            elif(ty<=330):
                fee=ty*3.02
            elif(ty<=500):
                fee=ty*4.39
            elif(ty<=700):
                fee=ty*4.97
            elif(ty>700):
                fee=ty*5.63
        else:
            if(ty<=120):
                fee=ty*2.10
            elif(ty<=330):
                fee=ty*2.68
            elif(ty<=500):
                fee=ty*3.61
            elif(ty<=700):
                fee=ty*4.01
            elif(ty>700):
                fee=ty*4.50
        fee=fee-(ly-ty)*0.6
    return fee;

main()
