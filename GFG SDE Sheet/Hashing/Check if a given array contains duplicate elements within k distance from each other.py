#https://www.geeksforgeeks.org/check-given-array-contains-duplicate-elements-within-k-distance/
from collections import OrderedDict,Counter,defaultdict
n=int(input())
l=list(map(int,input().split(',')))
k=int(input())
has=defaultdict(lambda:-1)
for i in range(n):
  if has[l[i]]==-1:
    has[l[i]]=i
  else:
    if i-has[l[i]]<=k:
      print("Yes")
      exit()
print("No")

  

  
