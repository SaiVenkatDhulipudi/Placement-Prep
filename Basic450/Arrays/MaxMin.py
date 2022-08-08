def maxmin(l):
    ma=mi=l[0]
    for  i in l[1:]:
        if i>ma:
            ma=i
        if i<mi:
            mi=i
    return ma,mi
    
if __name__=='__main__':
    n=int(input('enter n :'))
    l=list(map(int,input('enter list: ').split()))
    ma,mi=maxmin(l)
    print("Max element is: %s"%ma)
    print("Min element is: %s"%mi)