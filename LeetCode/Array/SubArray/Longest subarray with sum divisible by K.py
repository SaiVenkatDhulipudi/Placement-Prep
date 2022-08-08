from collections import defaultdict
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
	    d=defaultdict(lambda:-2)
	    su=0
	    d[su]=-1
	    maxle=0
	    for i in range(n):
	        su=((su%k)+(arr[i]%k+k))%k
	        if d[su]!=-2:
	           maxle=max(maxle,i-d[su])
	        else:
                d[su]=i
        return maxle
	            
