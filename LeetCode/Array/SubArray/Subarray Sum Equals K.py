from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d=defaultdict(lambda:0)
        su=0
        c=0
        for i in nums:
          su+=i
          if su==k:
            c+=1
          if d[su-k]:
            c+=d[su-k]
          d[su]+=1
        return c
