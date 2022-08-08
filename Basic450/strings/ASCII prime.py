from itertools import product
def fun(l):
  out=[]
  for sub in l:
    s=''
    for j in sub:
      s+=str(j)
    if seive[int(s)]:
      m=''
      for i in range(0,6,2):
        m+=chr(int(s[i:i+2]))
      out.append(m)
  return out
def s1(seive):
  for i in range(3,1000000,2):
    seive[i]=1 
  for i in range(3,1000000,2):
    for j in range(i*i,1000000,i):
      seive[j]=0
  seive[2]=1
s=input()
asci=[ord(i) for i in s]
l=[p for p in product(asci, repeat=3)]
seive=[0 for i in range(1000000)]
s1(seive)
out=sorted(fun(l))
if len(out):
  print(*out,sep=',')
  exit()
print(-1)
  
