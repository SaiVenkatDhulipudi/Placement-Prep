#https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1#
class Solution:
    def findOnce(self,arr : list, n : int):
        x=0
        for i in arr:
            x^=i
        return x
