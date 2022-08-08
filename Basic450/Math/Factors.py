from collections import defaultdict
def factor_comp(factor):
  for i in range(2,100):
    for j in range(i,100,i):
      factor[j].append(i)
if __name__=='__main__':
  factor=defaultdict(lambda:[1])
  factor_comp(factor)
  s=input()
  n=len(s)
  d=defaultdict(lambda:0)
  for i in range(n):
    d[int(s[i])]=1 
    if i<n-1:
      num=int(s[i]+s[i+1])
      d[num]=1 
  out=dict()
  for i in range(n-1):
    num=int(s[i]+s[i+1])
    c=0
    for j in factor[num]:
      if d[j]:
        c+=1 
    out[num]=c
  print(out)
  num=max(out.keys(),key=lambda x:(out[x],x))
  print(num)
  print(factor[56])