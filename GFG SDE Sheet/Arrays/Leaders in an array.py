#https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1#
def leaders(A, N):
  l=[A[-1]]
  for i in range(N-2,-1,-1):
    if l[-1]<=A[i]:
      l.append(A[i])
  return l[::-1]
