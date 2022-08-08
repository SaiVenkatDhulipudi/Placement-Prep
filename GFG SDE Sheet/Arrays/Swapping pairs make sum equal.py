#https://practice.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal4142/1#
class Solution:
    def findSwapValues(self,a, n, b, m):
        sum_a=sum(a)
        sum_b=sum(b)
        x=abs(sum_a-sum_b)
        s=set(b)
        if sum_a==sum_b:
            for i in a:
                if i in s:
                    return 1
            return -1
        if x&1:
            return -1
        dif=x//2
        if sum_a>sum_b:
            for i in a:
                if i-dif in s:
                    return 1
        else:
            s=set(a)
            for i in b:
                if i-dif in s:
                    return 1
        return -1
