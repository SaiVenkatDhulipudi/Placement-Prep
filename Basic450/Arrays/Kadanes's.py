def Kadane(l,n):
    max_sum=l[0]
    cur_sum=l[0]
    for i in range(1,n):
        cur_sum=max(l[i],cur_sum+l[i])
        max_sum=max(max_sum,cur_sum)
        
    print(max_sum)
if __name__=='__main__':
    n=int(input('enter n : '))
    l=list(map(int,input('enter l1: ').split()))
    Kadane(l,n)
    