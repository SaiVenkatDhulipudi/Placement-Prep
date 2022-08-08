from collections import defaultdict
def isSubset( a1, a2, n, m):
    if(m>n):
        return 'No'
    else:
        d=defaultdict(lambda:0)
        for i in a1:
            d[i]=1
        for i in a2:
            if not d[i]:
                return 'No'
        return 'Yes'
if __name__=='__main__':
    n=int(input('enter n : '))
    m=int(input('enter m : '))
    l1=list(map(int,input('enter l1: ').split()))
    l2=list(map(int,input('enter l2: ').split()))
    print(isSubset(l1,l2,n,m))