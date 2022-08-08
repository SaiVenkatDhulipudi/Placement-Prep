
#https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i=0
        j=len(arr)-1
        res=0
        while(i<j):
            res=max(res,(j-i)*min(arr[i],arr[j]))
            if arr[i]>arr[j]:
              j-=1
            else:
              i+=1
        return res
