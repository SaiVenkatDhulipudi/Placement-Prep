def ThreeN1(n,dp):
  if n&1:
    n=3*n+1 
  else:
    n=n//2
  if dp[n]!=0:
    return dp[n]
  else:
    dp[n]=1+ThreeN1(n,dp)
  return dp[n]
if __name__=='__main__':
  l=list(map(int,input('enter l  ').split()))
  dp=[0 for i in range(100000)]
  i=1
  while 2**i<100000:
    dp[2**i]=i
    i+=1
  for i in l:
    dp[i]=ThreeN1(i,dp)+1 
    print(dp[i]+1)
  print(*dp[:100])