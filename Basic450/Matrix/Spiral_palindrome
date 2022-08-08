def spiralPrint(m, n, a):
  k = 0
  l = 0
  out=[]
  while (k < m and l < n):
    for i in range(l, n):
      out.append(a[k][i])
    k += 1
    for i in range(k, m):
      out.append(a[i][n - 1])
    n -= 1
    if (k < m):
      for i in range(n - 1, (l - 1), -1):
        out.append(a[m - 1][i])
      m -= 1
    if (l < n):
      for i in range(m - 1, k - 1, -1):
        out.append(a[i][l])
      l += 1
  return out
R=int(input())
arr=[]
for i in range(R):
  arr.append(list(input().split(',')))
C=len(arr[0]) 
ou1=[]
out=spiralPrint(R, C, arr)
s=''
for i in out:
  s+=i
  if len(s)>1:
    if s[::-1]==s:
      ou1.append(s)
      s=''
ou1.append(s)
print(*ou1,sep=',')
