def power(x,n):
  if n==0:
    return 1 
  else:
    temp=power(x,n//2)
    temp=temp*temp 
    if n%2:
      return temp*a 
    else:
      return temp
a,n=map(float,input().split())
if n<0:
  x=power(a,-n)
  x=1/x
else:
  x=power(a,n)
print(x)
