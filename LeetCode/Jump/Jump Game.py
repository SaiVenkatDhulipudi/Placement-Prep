class Solution:
    def canJump(self, l: List[int]) -> bool:
        m=0
        for i in range(len(l)):
          if i>m:
            return False
          m=max(m,i+l[i])
        return True
 
