#https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0
from collections import defaultdict
class solution:
    def SortByFrequency(self,arr,n):
        cou=defaultdict(lambda:0)
        for i in arr:
            cou[i]+=1
        arr.sort(key=lambda x:(cou[x],-x),reverse=True)
