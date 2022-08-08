#https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i=1
        j=0
        tot=1
        while i<n:
            if arr[i]>dep[j]:
                j+=1
            else:
                tot+=1
            i+=1
        return tot
