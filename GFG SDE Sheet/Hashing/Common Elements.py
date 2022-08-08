#https://practice.geeksforgeeks.org/problems/common-elements5420/1#
from collections import defaultdict
class Solution:
    def common_element(self,v1,v2):
        d=defaultdict(lambda:0)
        out=[]
        for i in v1:
            d[i]+=1
        for i in v2:
            if d[i]>0:
                out.append(i)
            d[i]-=1
        return sorted(out)
