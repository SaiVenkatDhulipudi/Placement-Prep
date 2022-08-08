from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(lambda:-1)
        for i in range(len(nums)):
            if d[target-nums[i]]!=-1:
                return [d[target-nums[i]],i]
            d[nums[i]]=i
        
