class Solution:
    def sortedSquares(self, l: List[int]) -> List[int]:
        n=len(l)
        l1=[0]*(n)
        i=0
        j=n-1
        pos=n-1
        while i<=j:
          if abs(l[i])>abs(l[j]):
            l1[pos]=l[i]*l[i]
            pos-=1
            i+=1
          else:
            l1[pos]=l[j]*l[j]
            pos-=1
            j-=1
        return l1
