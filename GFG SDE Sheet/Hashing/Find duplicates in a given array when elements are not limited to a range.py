#https://www.geeksforgeeks.org/find-duplicates-given-array-elements-not-limited-range/
from collections import OrderedDict,Counter,defaultdict
n=int(input())
l=list(map(int,input().split(',')))
has=defaultdict(lambda:0)
for i in range(n):
  has[l[i]]+=1 
for i in has:
  if has[i]>1:
    print(i,end=' ')

  

  
