def main():
    number=input()
    if(number.isdigit()):
        number=int(number)
        if(not(1<=number<=20)):
            print("E")
            return;
        array,error=getInput(number)
        if(error!=1):
            calculate(array)
            output(array)
        else:
            print("E")
            return;
    else:
        print("E")

def getInput(number):
    array=[]
    for i in range(number):
        _input=input()
        array.append(_input.split(" "))
    for i in range(len(array)):
        for j in range(len(array[i])):
            if(array[i][j].isdigit()):
                array[i][j]=int(array[i][j])
            else:
                return [],1;
    return array,0;

def calculate(array):
    temp=0
    li=[]
    for i in range(len(array)):
        for j in range(len(array[i])-1):
            if(array[i][j+1]-array[i][j]==array[i][j+2]-array[i][j+1]):
                array[i].append(int(array[i][-1]+(array[i][j+1]-array[i][j])))
                break;
            elif(array[i][j+1]/array[i][j]==array[i][j+2]/array[i][j+1]):
                array[i].append(int(array[i][-1]*(array[i][j+1]/array[i][j])))
                break;
    #return array;

def output(array):
    for i in range(len(array)):
        for j in array[i]:
            print(j,end=' ')
        print('')

main()
