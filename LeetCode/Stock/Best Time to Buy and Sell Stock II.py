#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, l: List[int]) -> int:
        n=len(l)
        mini=l[0]
        maxi=l[0]
        ans=0
        for i in range(1,n):
          if mini>l[i]:
            mini=l[i]
            maxi=l[i]
          if maxi<l[i]:
            maxi=l[i]
            ans+=(maxi-mini)
            mini=l[i]
        return ans
