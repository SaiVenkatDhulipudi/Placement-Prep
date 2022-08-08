def moveNegToEnd(l,i,j,n):
    if i==(n//2):
        print(l)
    else:
        if l[i]<0 and l[j]>0:
            l[i],l[j]=l[j],l[i]
            j=j-1
            i+=1
        elif l[i]<0:
            j-=1
        else:
            i+=1
            j-=1
        moveNegToEnd(l,i,j,n)
if __name__=='__main__':
    n=int(input('enter n: '))
    l=list((map(int,input('enter list : ').split())))
    moveNegToEnd(l,0,n-1,n)
