#https://practice.geeksforgeeks.org/problems/binary-search/1
class Solution:	
	def binarysearch(self, arr, n, k):
		lo=0
		hi=n-1
		while lo<=hi:
		    mid=(lo+hi)//2
		    if arr[mid]==k:
		        return mid
		    elif arr[mid]>k:
		        hi=mid-1
		    else:
		        lo=mid+1
		return -1
