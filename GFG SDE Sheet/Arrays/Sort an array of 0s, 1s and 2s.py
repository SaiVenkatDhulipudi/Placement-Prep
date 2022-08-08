#https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
def sort012(self,l,n):
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if l[mid]==0:
                l[low],l[mid]=l[mid],l[low]
                low+=1
                mid+=1
            elif l[mid]==2:
                l[mid],l[high]=l[high],l[mid]
                high-=1
            else:
                mid+=1
