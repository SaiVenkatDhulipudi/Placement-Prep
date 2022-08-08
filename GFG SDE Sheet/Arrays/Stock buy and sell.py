#https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1
class Solution:
	def stockBuySell(self, A, n):
		l=[]
		for i in range(1,n):
	        if A[i]>A[i-1]:
	            l.append([i-1,i])
	    return l
