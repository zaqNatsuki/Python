def main():
    cards=input().split(' ')
    style=check(cards)
    out(style)
    return;

def check(cards):
    isStraight=straight(cards)
    isSuit=sameSuit(cards)
    if(isStraight==1 and isSuit==1):
        return 7;
    elif(isStraight==1):
        return 4;
    else:
        style=otherStyle(cards)
        return style;

def straight(cards):
    card=[int(i[:-1]) for i in cards]
    card=sorted(card)
    yesStr=1
    for i in range(len(card)-1):
        if(not(card[i+1]-card[i]==1 or card[i+1]-card[i]==9)):
            yesStr=0
            break;
    return yesStr;

def sameSuit(cards):
    suit=[i[-1] for i in cards]
    if(suit.count(suit[0])==5):
        return 1;
    else:
        return 0;

def otherStyle(cards):
    card=[int(i[:-1]) for i in cards]
    card=sorted(card)
    li=[card.count(i) for i in card]
    if(li.count(4)==4):
        return 6;
    elif(li.count(3)==3 and li.count(2)==2):
        return 5;
    elif(li.count(3)==3):
        return 3;
    elif(li.count(2)==4):
        return 2;
    elif(li.count(2)==2):
        return 1;
    else:
        return 0;

def out(style):
    print(style)
    return;

main()
