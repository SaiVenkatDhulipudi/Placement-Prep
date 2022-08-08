from collections import defaultdict
def factorcount(n):
    d=defaultdict(lambda :0)
    #for 2 multiples
    while n%2==0:
        n=n//2
        d[2]+=1
    #for 3 multiples
    while n%3==0:
        n=n//3
        d[3]+=1
    k=int(n**(0.5))
    for i in range(5,k+1,6):
        while n%i==0:
            d[i]+=1
        while n%(i+2)==0:
            d[i+2]+=1
    #if n is prime 
    if n>3:
        d[n]+=1
    return d
if __name__=='__main__':
    n=int(input('enter number : '))
    cou=1
    
    for value in factorcount(n).values():
        cou*=(value+1)
    print(cou)