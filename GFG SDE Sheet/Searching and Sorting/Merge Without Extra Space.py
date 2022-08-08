#https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1#
class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        i=0
        j=0
        le=n-1
        while i<n and j<m:
            if arr1[i]>arr2[j]:
                arr1[le],arr2[j]=arr2[j],arr1[le]
                j+=1
                le-=1
            else:
                i+=1
        arr1.sort()
        arr2.sort()
