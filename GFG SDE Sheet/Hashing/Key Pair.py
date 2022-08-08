#https://practice.geeksforgeeks.org/problems/key-pair5616/1/
from collections import defaultdict
class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
	    has=defaultdict(lambda:0)
	    for i in arr:
	        if has[(x-i)]!=0:
	            return 1
	        has[i]+=1
	    return 0
