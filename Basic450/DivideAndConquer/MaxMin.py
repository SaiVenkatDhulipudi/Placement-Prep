def maxmin(l,low,high,ma,mi):
    if low==high:
        ma=mi=l[low]
    elif low==high-1:
        ma=max(l[high],l[low])
        mi=min(l[high],l[low])
    else:
        mid=(low+high)//2
        ma,mi=maxmin(l,low,mid,ma,mi)
        mi1=999999
        ma1=-99999
        ma1,mi1=maxmin(l,mid+1,high,ma1,mi1)
        ma=max(ma,ma1)
        mi=min(mi,mi1)
    return ma,mi
if __name__=='__main__':
    mi=999999
    ma=-99999
    n=int(input('enter n :'))
    l=list(map(int,input('enter list: ').split()))
    ma,mi=maxmin(l,0,n-1,ma,mi)
    print("Max element is: %s"%ma)
    print("Min element is: %s"%mi)