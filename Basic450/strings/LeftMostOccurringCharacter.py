from collections import defaultdict
def defD():
    return -1
def LeftMostOccuringCharacter(s):
    d=defaultdict(defD)
    res=len(s)
    for i in range(len(s)):
        fi=d[s[i]]
        if fi==-1:
            d[s[i]]=i 
        else:
            res=min(res,fi)
    return (res if res!=len(s)else -1)

if __name__=='__main__':
    print(LeftMostOccuringCharacter(input('enter string:')))