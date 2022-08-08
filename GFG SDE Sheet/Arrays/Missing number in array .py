#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
def MissingNumber(self,array,n):
        su=sum(array)
        n=n*(n+1)//2
        return n-su
