from bisect import bisect_left,bisect
def lis(l):
        res=[]
        if len(l)>0:
            res.append(l[0])
        for i in range(1,len(l)):
            if l[i]>res[-1]:
                res.append(l[i])
            else:
                ind=bisect_left(res,l[i],0,len(res))
                res[ind]=l[i]
        return len(res)
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    print(lis(l))