def knapsack(n,w,profit,weight):
    dp=[[0 for i in range(w+1)] for j in range(n+1)] #matrix intialisation
    for i in range(1,n+1):
        for j in range(1,w+1):
            if weight[i-1]>j:
                dp[i][j]=dp[i-1][j] 
            else:
                dp[i][j]=max( profit[i-1]+dp[i-1][j-weight[i-1]] , dp[i-1][j]) 
    return dp[n][w]
if __name__=='__main__':
    n=int(input('enter no of bags :'))
    w=int(input('enter weight :'))
    profit=list(map(int,input('enter profit array: ').split()))
    weight=list(map(int,input('enter weight array: ').split()))
    knap = knapsack(n,w,profit,weight)
    print(knap)