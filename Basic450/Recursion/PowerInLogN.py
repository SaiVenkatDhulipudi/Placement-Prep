def POWER(a,n):
    if(n==0):
        return 1
    else:
        temp=POWER(a,n//2)
        temp*=temp
        if n&1:
            return temp*a
        else:
            return temp
if __name__=='__main__':
    a=int(input('enter a '))
    n=int(input('enter n '))
    print(POWER(a,n))
