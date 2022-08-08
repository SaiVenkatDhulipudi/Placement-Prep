def issubsequence(s1,s2,i,j,n1,n2):
    if j==n2:
        return True
    if i==n1:
        return False
    else:
        if s1[i]==s2[j]:
            return issubsequence(s1,s2,i+1,j+1,n1,n2)
        else:
            return issubsequence(s1,s2,i+1,j,n1,n2)
    
    
if __name__=='__main__':
    s1=input('enter string 1: ')
    s2=input('enter string 2: ' )
    print(issubsequence(s1,s2,0,0,len(s1),len(s2)))