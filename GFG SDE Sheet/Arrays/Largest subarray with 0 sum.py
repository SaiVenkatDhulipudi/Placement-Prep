#https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
from collections import defaultdict
class Solution:
    def maxLen(self, n, arr):
        d=defaultdict(lambda :-1)
        cursum=0
        maxlen=0
        for i in range(n):
            cursum+=arr[i]
            if cursum==0:
                maxlen=i+1
            elif d[cursum]!=-1:
                maxlen=max(maxlen,i-d[cursum])
            else:
                d[cursum]=i
        return maxlen
