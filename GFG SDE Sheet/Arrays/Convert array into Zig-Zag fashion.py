#https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1
def zigZag(self,l, n):
		for i in range(1,n,2):
		    if (l[i]<l[i-1]):
		        l[i],l[i-1]=l[i-1],l[i]
		    if i<n-1 and l[i]<l[i+1]:
		        l[i],l[i+1]=l[i+1],l[i]
