from collections import defaultdict
#https://practice.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1
class Solution:
    def firstElementKTime(self,  a, n, k):
        d=defaultdict(lambda:0)
        for i in a:
            d[i]+=1
            if d[i]==k:
                return i
        return -1
    
