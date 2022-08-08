c=0
def Issorted(l,low,high):
    if(high-low>1):
        mid=(low+high)//2
        if l[mid-1]<=l[mid]<=l[mid+1]:
            if Issorted(l,low,mid) and Issorted(l,mid+1,high):
                return True
    else:
        return True
    return False
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    print(Issorted(l,0,n-1))
    print(c)