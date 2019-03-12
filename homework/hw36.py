def main():     #A-B-C-D=黑桃-紅心-磚塊-梅花
    play()

def play():                 #玩遊戲
    error=0
    hand=[input().split() for i in range(4)]      #手牌
    convert(hand)
    error,trump,who=getTrump()
    if(error!=-1):
        start(who,hand,trump)
    else:
        print("ERROR")
    return;

def getTrump():             #取得王牌
    now=past='0'
    p=error=0
    who=0
    while True:
        now=input()
        who+=1
        if(now=='pass'):
            p+=1
            if(p==3):
                if(past=='0'):
                    return -1,0,0;
                return error,trump,who%4;
            continue;
        else:
            p=0
        if(past!='0'):
            error,trump=discuss(past,now)
            if(error==-1):
                return error,trump,-1;
        past=now

def convert(card):          #將1轉成14
    for i in card:
        for j,xj in enumerate(i):
            if(xj[:-1]=='1'):
                i[j]=xj.replace('1','14')
    
def discuss(past,now):      #判斷喊牌階段是否符合規則
    if(now[0]>past[0]):
        return 1,now;
    elif(now[0]==past[0] and now[1]<past[1]):
        return 1,now;
    else:
        return -1,'';

def start(who,hand,trump):  #開始玩牌
    winTime=int(trump[:-1])
    trump=trump[-1]
    turn=error=0
    show=[input().split() for i in range(3)]  #丟出的牌
    convert(show)
    win=[0 for i in range(4)]                   #獲勝次數
    turn=who+1              #丟牌順序
    for i in range(3):
        error=check(turn,show[i],hand)
        if(error==-1):
            print("ERROR")
            return;
        turn=winner(turn,show[i],trump,win)
    out(who,win,winTime)
    return;

def check(turn,show,hand):  #檢查出牌
    n=turn
    for i in show:          #檢查手牌是否有牌
        if(i in hand[n%4]):
            hand[n%4].remove(i)
            n+=1
        else:
            return -1;
    suit=[[j[-1] for j in i] for i in hand]
    for i in range(1,4):    #檢查花色
        if(show[0][-1]!=show[i][-1] and show[0][-1] in suit[(turn+i)%4]):
            return -1;
    return 1;

def winner(turn,show,trump,win):                #判斷回合誰贏
    big=show[0]
    for i in range(4):
        big=biggest(big,show[i],trump)
        whoWin=(turn+show.index(big))%4
    win[whoWin]+=1
    return whoWin;

def biggest(big,other,trump):
    if(other[-1]==trump and big[-1]!=trump):
        return other;
    elif(other[-1]==big[-1] and int(other[:-1])>int(big[:-1])):
        return other;
    else:
        return big;
    
def out(who,win,winTime):
    p13=win[0]+win[2]
    p24=win[1]+win[3]
    for i in win:
        print(i)
    if(who%2==0):
        if(p13!=winTime):
            print("P2 P4")
        else:
            print("P1 P3")
    else:
        if(p24!=winTime):
            print("P1 P3")
        else:
            print("P2 P4")
    return;

main()
