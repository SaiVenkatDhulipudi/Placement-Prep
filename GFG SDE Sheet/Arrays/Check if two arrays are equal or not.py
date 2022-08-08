#https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
from collections import defaultdict
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        d=defaultdict(lambda:0)
        for i in A:
            d[i]+=1
        for i in B:
            d[i]-=1
            if d[i]<0:
                return False
        if sum(d.values())>0:
            return False
        return True
