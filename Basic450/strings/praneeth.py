from collections import defaultdict
n=int(input())
mat=[]
d=defaultdict(lambda:0)
for i in range(0,n,1):
  l=list(input().split())
  mat.append(l)
  l=set(l)
  for ele in l:
    d[ele]+=1
out=[[0 for _ in range(len(mat[0]))]for _ in range(n)]
k=n/2
for i in range(n):
  for j in range(len(mat[0])):
    if d[mat[i][j]]==n:
      out[i][j]=0
    elif d[mat[i][j]]>k:
      if i%2==0:
        out[i][j]=1
      else:
        out[i][j]=0
    else:
      out[i][j]=1
m=len(mat[0])
l=[]
for i in range(n):
  if out[i].count(1)-out[i].count(0)==0:
    s=''
    for j in range(m):
      if j%2==0:
        s+='1'
      else:
        s+='0'
    l.append(list(s))
  elif out[i].count(1)==m or out[i].count(0)==m:
    l.append(out[i])
  else:
    if out[i].count(1)>out[i].count(0):
      ones=out[i].count(1)
      s='1'*(int(ones/2)+1)
      s+='0'*out[i].count(0)
      s+='1'*(int(ones/2))
    else:
      ones=out[i].count(0)
      s='0'*(int(ones/2)+1)
      s+='1'*out[i].count(1)
      s+='0'*(int(ones/2))
    l.append(list(s))
for i in l:
  print(*i,sep=',')
