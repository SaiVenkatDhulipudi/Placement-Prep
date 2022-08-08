def LCSof3(A,B,n1,n2):
        dp=[[0  for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if A[i-1]==B[j-1] :
                    dp[i][j]=1+dp[i-1][j-1]
                else:
    
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i][j])
                    
        return dp[n1][n2]
if __name__=='__main__':
    n=int(input())
    m=int(input())
    s1=input()
    s2=input()
    x=(LCSof3(s1,s2,n,m))
    print((n-x)+(m-x))
    