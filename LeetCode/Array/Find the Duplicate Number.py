class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        for i in nums:
            if dp[i]:
                return i
            dp[i]+=1
        
  
