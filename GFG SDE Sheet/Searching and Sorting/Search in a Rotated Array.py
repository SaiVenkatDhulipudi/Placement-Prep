#https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1#
class Solution:
    def search(self, arr: list, l : int, h : int, key : int):
        if l>h:
            return -1
        mid=l+(h-l)//2
        if arr[mid]==key:
            return mid
        if arr[l]<=arr[mid]:
            if key>=arr[l] and key<=arr[mid]:
                h=mid-1
            else:
                l=mid+1
        else:
            if key>=arr[mid] and key<=arr[h]:
                l=mid+1
            else:
                h=mid-1
        return self.search(arr,l,h,key)
