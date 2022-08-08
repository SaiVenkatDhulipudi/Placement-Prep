from collections import defaultdict
def fun():
    return 0
def find3Numbers(l, n, X):
        d=defaultdict(fun)
        for i in l:
            d[i]=1
        for i in range(n):
            for j in range(i+1,n):
                x=X-(l[i]+l[j])
                if x!=l[i] and x!=l[j] and d[x]:
                    return 1
        return 0
if __name__=='__main__':
    n=int(input('enter n : '))
    l1=list(map(int,input('enter l1: ').split()))
    x=int(input('enter x : '))
    print(l1,n,x)