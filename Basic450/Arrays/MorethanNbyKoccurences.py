def morethannbyk(l,n,k):
    d={}
    x=n//k
    for i in l:
        try:
            d[i]+=1
        except:
            d[i]=1
    def fun(i):
        if d[i]>x:
            return i
        else:
            pass
    l=list(map(fun,d.keys()))
    print(l)
    
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    k=int(input('enter k : '))
    morethannbyk(l,n,k)
