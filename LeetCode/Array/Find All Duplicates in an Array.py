#https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      dp=[0]*(len(nums)+1)
      out=[]
      for i in nums:
        if dp[i]:
          out.append(i)
        dp[i]+=1
      return out
#O(1) space solution

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      res = []
      for x in nums:
          if nums[abs(x)-1] < 0:
              res.append(abs(x))
          else:
              nums[abs(x)-1] *= -1
      return res
