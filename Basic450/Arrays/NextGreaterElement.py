def NextGreater(n,l):
    stack=list()
    stack.append(l[0])
    for i in range(1,n):
        if not len(stack):
            stack.append(l[i])
            continue
        while len(stack) and stack[0]<l[i]:
            print(stack[0],' --> ',l[i])
            stack.pop(0)
        try:
            stack.insert(0,l[i])
        except:
            stack.append(l[i])
    while(len(stack)):
        print(stack[0],' --> ',-1)
        stack.pop(0)
        
if __name__=='__main__':
    n=int(input('enter n: '))
    l=list(map(int,input('enter list : ').split()))
    NextGreater(n,l)