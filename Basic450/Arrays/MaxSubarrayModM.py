def subarraymodM(n,l,m):
    s=set()
    prefix=maxim=0
    s.add(0)
    for i in range(n):
        prefix=(prefix+l[i])%m
        maxim=max(maxim,prefix)
        it =0
        for i in s:
            if i>=prefix+1:
                it=i
        if it!=0:
            maxim=max(maxim,prefix-it+m)
        s.add(prefix)
    return maxim

if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    m=int(input('enter m : '))
    print(subarraymodM(n,l,m))