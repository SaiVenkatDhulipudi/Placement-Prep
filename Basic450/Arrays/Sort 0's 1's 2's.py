def sorts(l,n,low,mid,high):
    if mid<=high:
        if l[mid]==0:
            l[low],l[mid]=l[mid],l[low]
            low+=1
            mid+=1
        elif l[mid]==2:
            l[mid],l[high]=l[high],l[mid]
            high-=1
        else:
            mid+=1
        sorts(l,n,low,mid,high)
    else:
        print(*l)
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    sorts(l,n,0,0,n-1)
