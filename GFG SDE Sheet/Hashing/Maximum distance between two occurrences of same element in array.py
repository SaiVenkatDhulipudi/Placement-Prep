#https://www.geeksforgeeks.org/maximum-distance-two-occurrences-element-array/
from collections import OrderedDict,Counter,defaultdict
n=int(input())
l=list(map(int,input().split(',')))
has=defaultdict(lambda:-1)
mx=0
for i in range(n):
  if has[l[i]]==-1:
    has[l[i]]=i 
  else:
    mx=max(mx,i-has[l[i]])

print(mx)
  

  
