#https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1#
from heapq import nsmallest
class Solution:
    def kthSmallest(self,arr, l, r, k):
        return nsmallest(k,arr)[-1]
