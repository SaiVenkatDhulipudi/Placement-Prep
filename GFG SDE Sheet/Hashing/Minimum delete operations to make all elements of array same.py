#https://www.geeksforgeeks.org/minimum-delete-operations-make-elements-array/
from collections import OrderedDict,Counter,defaultdict
n=int(input())
l=list(map(int,input().split()))
has=defaultdict(lambda:0)
for i in l:
  has[i]+=1
mx=max(has.values())
print(n-mx)
  

  
