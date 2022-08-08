def LIS(l,n):
    lis=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if l[j]<l[i]:
                lis[i]=max(lis[i],lis[j]+1)
    return max(lis)

if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    print(LIS(l,n))