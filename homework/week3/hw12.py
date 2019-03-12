def main():
    a1=int(input())
    a2=int(input())
    b1=int(input())
    b2=int(input())
    c1=int(input())
    c2=int(input())
    domain=getLocation(a1,a2,b1,b2,c1,c2)
    output(domain)

def getLocation(a1,a2,b1,b2,c1,c2):
    amax=max(a1,a2)
    amin=min(a1,a2)
    bmax=max(b1,b2)
    bmin=min(b1,b2)
    cmax=max(c1,c2)
    cmin=min(c1,c2)
    domain=abs(a1-a2)+abs(b1-b2)+abs(c1-c2)
    _max=max(amax,bmax,cmax)
    _min=min(amin,bmin,cmin)
    if((amax<bmax and amax>bmin and amin<bmin) or
       (amax>bmax and bmax>amin and amin>bmin)):
        domain=abs(bmax-amin)+abs(cmax-cmin)
    if((amax<cmax and amax>cmin and amin<cmin) or
       (amax>cmax and cmax>amin and amin>cmin)):
        domain=abs(amax-cmin)+abs(bmax-bmin)
    if((cmax<bmax and cmax>bmin and cmin<bmin) or
       (cmax>bmax and bmax>cmin and cmin>bmin)):
        domain=abs(bmin-cmax)+abs(amax-amin)
    if(_max-_min)<domain:
        domain=_max-_min
    return domain;

def output(domain):
    print(domain)

main()
