from collections import defaultdict
arr=list(map(int,input().split(',')))
dp=defaultdict(lambda:0)
visited=defaultdict(bool)
for i in arr:
  dp[i]+=1
k=0
for i in arr:
  if not visited[i]:
    j=i
    k1=0
    while dp[j]:
      visited[j]=1
      j+=1
      k1+=1
    k=max(k,k1)
if k==1:
  print(-1)
  exit()
  
print(k)