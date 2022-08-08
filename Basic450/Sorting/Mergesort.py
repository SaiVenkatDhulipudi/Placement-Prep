from threading import Thread
def merge(l,low,mid,high):
    n1=mid-low+1
    n2=high-mid
    left=[0]*n1
    right=[0]*n2
    for i in range(n1):
        left[i]=l[low+i]
    for j in range(n2):
        right[j]=l[mid+j+1]
    i=0
    j=0
    k=low
    while (i<n1 and j<n2):
        if left[i]<=right[j]:
            l[k]=left[i]
            i+=1
        else:
            l[k]=right[j]
            j+=1
        k+=1
    while i<n1:
        l[k]=left[i]
        i+=1
        k+=1
    while j<n2:
        l[k]=right[j]
        j+=1
        k+=1
#mergesort
def mergesort(l,low,high):
    if low<high :
        mid=(low+high)//2
        mergesort(l,low,mid)
        mergesort(l,mid+1,high)
        merge(l,low,mid,high)
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    mergesort(l,0,n-1)
    print(*l)