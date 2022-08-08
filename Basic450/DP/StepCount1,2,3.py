def countsteps(n):
    dp=[0]*n
    dp[1]=dp[0]=1
    dp[2]=2
    for i in range(3,n):
        dp[i]=sum(dp[i-3:i])
    return dp[n-1]
if __name__=='__main__':
    n=int(input("enter n: "))
    print(countsteps(n))
