#https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
def maxSubArraySum(self,l,n):
        max_sum=l[0]
        cur_sum=l[0]
        for i in range(1,n):
            cur_sum=max(l[i],cur_sum+l[i])
            max_sum=max(max_sum,cur_sum)
            
        return max_sum
