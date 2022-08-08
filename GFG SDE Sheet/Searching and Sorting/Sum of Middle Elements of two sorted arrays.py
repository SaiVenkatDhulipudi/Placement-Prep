#https://practice.geeksforgeeks.org/problems/sum-of-middle-elements-of-two-sorted-arrays2305/1#
from heapq import merge
class Solution:
	def findMidSum(self, ar1, ar2, n): 
		l=list(merge(ar1,ar2))
		su=l[n]+l[n-1]
		return su
