def NearestMultiple():
  z=((num//m)-1)*m
  x=((num//m))*m
  y=((num//m)+1)*m
  return min(x,y,z,key=lambda k:abs(num-k))
num=int(input())
m=int(input())
print(NearestMultiple(num,m))
