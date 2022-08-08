#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1#
from collections import defaultdict
class Solution:
    def subArraySum(self,arr, n, s): 
        d=defaultdict(lambda:0)
        d[0]=0
        su=0
        for i in range(n):
            su+=arr[i]
            if su-s in d:
                return [d[su-s]+1,i+1]
            d[su]=i+1
        return [-1] 
