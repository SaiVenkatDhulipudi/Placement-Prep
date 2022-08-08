class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        while i<n:
          j=0
          while j<m and nums1[j]<nums2[i]:
            j+=1
          nums1.insert(j,nums2[i])
          nums1.pop()
          m+=1
          i+=1
