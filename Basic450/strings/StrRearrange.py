s=str(input())
x=2**len(s)
res=[]
for i in range(x):
    b=bin(i).replace("0b","")
    if len(b)<len(s):
        b+='0'*(len(s)-len(b))
    re=""
    k=0
    for j in b:
        if j=='0':
            re+=s[k].lower()
        else:
            re+=s[k].upper()
        k+=1
    res.append(re)
print(*res,sep=',')