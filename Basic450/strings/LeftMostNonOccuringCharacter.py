from collections import defaultdict
def defD():
    return -1
def LeftMostNonOccuringCharacter(s):
    d=defaultdict(defD)
    for i in range(len(s)):
        fi=d[s[i]]
        if fi==-1:
            d[s[i]]=i 
        else:
            d[s[i]]=-2
    ch=''
    res=len(s)
    for k in d:
        if d[k]==0:
            res=min(res,d[k])
            ch=k
    return (ch+' ',res if res!=len(s) else -1)
if __name__=='__main__':
    print(LeftMostNonOccuringCharacter(input('enter string:')))