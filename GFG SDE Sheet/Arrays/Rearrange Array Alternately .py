#https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1
def rearrange(self,arr, n): 
        l1=arr[n//2:]
        l2=arr[:n//2]
        i=0
        j=-1
        for k in range(n):
            if k&1:
                arr[k]=l2[i]
                i+=1
            else:
                arr[k]=l1[j]
                j-=1
