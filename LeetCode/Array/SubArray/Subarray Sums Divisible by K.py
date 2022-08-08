#https://leetcode.com/problems/subarray-sums-divisible-by-k/
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dp=[0]*k
        dp[0]=1
        su=0
        cou=0
        for i in nums:
          su+=i 
          cou+=(dp[su%k])
          dp[su%k]+=1
        return cou
