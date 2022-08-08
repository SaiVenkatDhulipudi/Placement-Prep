from collections import defaultdict
def fun():
    return 0
def findLongestConseqSubseq(arr, N):
    dp=defaultdict(fun)
    visited=defaultdict(bool)
    for i in arr:
        dp[i]+=1
    k=0
    for i in arr:
        if not visited[i]:
            j=i
            k1=0
            while dp[j]:
                visited[j]=1
                j+=1
                k1+=1
            k=max(k,k1)
    return k
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    print(findLongestConseqSubseq(l,n))