#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, l: List[int]) -> None:
        n=len(l)
        j=0
        for i in range(n):
            if l[i]!=0:
                l[j],l[i]=l[i],l[j]
                j+=1
