def findfirst(arr,low,high,x):
    if low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            if arr[mid-1]!=x:
                return mid
            else:
                high=mid-1
        if arr[mid]>x:
            high=mid+1
        else:
            low=mid-1
        return findfirst(arr,low,high,x)
    return -1
def findlast(arr,low,high,x):
    if low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            if arr[mid+1]!=x:
                return mid
            else:
                high=mid+1
        if arr[mid]>x:
            high=mid+1
        else:
            low=mid-1
        return findfirst(arr,low,high,x)
    return -1
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    x=int(input('enter x : '))
    first=findfirst(l,0,n-1,x)
    last=findlast(l,0,n-1,x)
    print(first,' ',last)
    print(*enumerate(l),sep='\n')
