def RotateByOne(l,i):
    if(i==0):
        print(*l)
    else:
        l.append(l[0])
        RotateByOne(l[1:],i-1)
if __name__=='__main__':
    n=int(input('enter n'))
    l=list(map(int,input('enter list :').split()))
    k=int(input("enter k:"))
    RotateByOne(l,k%n)
