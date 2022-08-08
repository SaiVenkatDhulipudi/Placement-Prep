def fit(l,cow,n,mindist):
    cntCows = 1
    lastPlacedCow =l[0]
    for i in range(n):
        if(l[i] - lastPlacedCow >= mindist) :
                cntCows+=1
                lastPlacedCow = l[i]; 
    if(cntCows >= cow) :
        return True
    return False
def aggressive(l,low,high,cow,n):
    if low<=high:
        mid=(low+high)//2
        if fit(l,cow,n,mid):
            low=mid+1
        else:
            high=mid-1
        return aggressive(l,low,high,cow,n)
    return high
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    c=int(input('enter cows : '))
    l.sort()
    high=l[-1]-l[0]
    print(aggressive(l,1,high,c,n))