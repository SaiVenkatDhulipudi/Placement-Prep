class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        mini=1e9
        i=0
        j=M-1
        while j<N:
            mini=min(mini,A[j]-A[i])
            i+=1
            j+=1
        return mini
