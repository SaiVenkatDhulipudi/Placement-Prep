def union_intersection(l1,l2):
    l1=set(l1)
    l2=set(l2)
    print(sorted(l1.union(l2)))
    print(sorted(l1.intersection(l2)))
if __name__=='__main__':
    n=int(input('enter n : '))
    l1=list(map(int,input('enter l1: ').split()))
    l2=list(map(int,input('enter l2: ').split()))
    union_intersection(l1,l2)