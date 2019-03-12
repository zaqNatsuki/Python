def payProject(callin,callout,calltel,mailin,mailout):
    project183=callin*0.08+callout*0.139+calltel*0.135+mailin*1.128+mailout*1.483
    project383=callin*0.07+callout*0.130+calltel*0.121+mailin*1.128+mailout*1.483
    project983=callin*0.06+callout*0.108+calltel*0.101+mailin*1.128+mailout*1.483
    if(project183<183):
        project183=183
    if(project383<383):
        project383=383
    if(project983<983):
        project983=983
    if(project183<project383 and project183<project983):
        return project183, 183;
    elif(project383<project183 and project383<project983):
        return project383, 383;
    elif(project983<project183 and project983<project383):
        return project983, 983;
def main():
    callin=int(input())
    callout=int(input())
    calltel=int(input())
    mailin=int(input())
    mailout=int(input())
    fee,project=payProject(callin,callout,calltel,mailin,mailout)
    print("%d"%fee)
    print("%d"%project)

main()
