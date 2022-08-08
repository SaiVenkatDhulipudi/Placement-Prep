def LCSof3(A,B,C,n1,n2,n3):
        dp=[[[0 for _ in range(n3+1)] for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                for k in range(1,n3+1):
                    if A[i-1]==B[j-1] and B[j-1]==C[k-1]:
                        dp[i][j][k]=1+dp[i-1][j-1][k-1]
                    else:
                        
                        dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
                    
        return dp[n1][n2][n3]
if __name__=='__main__':
    s1=input('enter string 1: ')
    s2=input('enter string 2: ' )
    s3=input('enter string 2: ' )
    print(LCSof3(s1,s2,s3,len(s1),len(s2),len(s3)))