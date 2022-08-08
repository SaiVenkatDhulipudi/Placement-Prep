#https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1#
def reverseInGroups(self,l, n, k):
	    for i in range(0,n,k):
	        le=i
	        ri=min(i+k-1,n-1)
	        while le<ri:
	            l[le],l[ri]=l[ri],l[le]
	            le+=1
	            ri-=1
