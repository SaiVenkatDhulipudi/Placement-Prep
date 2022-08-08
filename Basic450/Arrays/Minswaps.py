def minSwaps(self, nums):
		n=len(nums)
		l=sorted(nums)
		c=0
		d={}
		init =0
		for i in range(n):
		    d[nums[i]]=i
		for i in range(n):
		    if l[i]!=nums[i]:
		        init=nums[i]
		        c+=1
		        j=d[l[i]]
		        nums[i],nums[j]=nums[j],nums[i]
    		    d[init]=d[l[i]]
    		    d[l[i]]=i
		return c