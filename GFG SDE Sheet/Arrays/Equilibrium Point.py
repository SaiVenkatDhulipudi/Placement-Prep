#https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1
def equilibriumPoint(self,A, N):
        su=sum(A)
        cs=0
        for i in range(N):
            cs+=A[i]
            if su-cs==0:
                return i+1
            su-=A[i]
        return -1
