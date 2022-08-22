def pali(s,i,n):
    if i==n//2:
        return True
    else:
        if s[i]==s[n-i-1]:
            return pali(s,i+1,n)
        else:
            return False
if __name__=='__main__':
    s=input('enter string : ')
    print(pali(s,0,len(s)))