Given n dice each with m faces. Find the number of ways to get sum x which is the summation of values on each face when all the dice are thrown.
#code here
  class Solution:
   def noOfWays(self, m,n,x):
       dp=[0]*(x+1)
       dp[0]=1
       for i in range(1,n+1):
            for j in range(x,-1,-1):
                dp[j]=sum(dp[j-k] for k in range(1,m+1) if j-k>=0)
       return dp[x]
