class Solution:
    def jump(self, l: List[int]) -> int:
        n=len(l)
        if n<=1:
          return 0
        i,j=0,l[0]
        c=1
        while j<n-1:
          c+=1
          nxt=max(ind+l[ind] for ind in range(i,j+1))
          i,j=j,nxt
        return c
     
