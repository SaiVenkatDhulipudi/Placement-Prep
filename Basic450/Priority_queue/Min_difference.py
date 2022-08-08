from heapq import heapify,heappop 
def minimum_difference(nums):
    heapify(nums)
    print(nums)
    k=heappop(nums)
    min_dif=1e9
    while(len(nums)>0):
        x=heappop(nums)
        min_dif=min(abs(k-x),min_dif)
        k=x
    return min_dif
if __name__=='__main__':
    n=int(input('enter size: '))
    l=list(map(int,input('enter array : ').split()))
    print(minimum_difference(l))
