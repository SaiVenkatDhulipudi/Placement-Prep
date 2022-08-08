from heapq import heapify,heappop 
def Median(med,k):
    if(k==0):
        return heappop(med)
    else:
        heappop(med)
        return Median(med,k-1)
if __name__=='__main__':
    n1=int(input('enter size 1: '))
    l1=list(map(int,input('enter array1 : ').split()))
    n2=int(input('enter size 2: '))
    l2=list(map(int,input('enter array2 : ').split()))
    l1.extend(l2)
    heapify(l1)
    print(Median(l1,(n1+n2)//2))

