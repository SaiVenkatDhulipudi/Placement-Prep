def partition(l,low,high):
    pivot=l[high]
    i=low-1
    for j in range(low,high):
        if l[j]<=pivot:
            i+=1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[high]=l[high],l[i+1]
    return i+1
def quicksort(l,low,high):
    if(low<high):
        j=partition(l,low,high)
        quicksort(l,low,j-1)
        quicksort(l,j+1,high)


if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    quicksort(l,0,n-1)
    print(*l)