class Solution:
    def maxScore(self, l: List[int], k: int) -> int:
        n=len(l)
        i,j=0,n-k
        total=sum(l[j:])
        res=total
        while j<n:
          total+=(l[i]-l[j])
          res=max(total,res)
          i+=1
          j+=1
        return res
