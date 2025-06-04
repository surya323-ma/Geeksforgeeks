Given three strings s1, s2, and s3 containing uppercase letters, lowercase letters, and digits, find the length of longest common sub-sequence in all three given strings.
#code here
  class Solution:
    def lcsOf3(self,s1, s2, s3):
        m, n, o = len(s1), len(s2), len(s3)
        dp = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, o + 1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

        return dp[m][n][o]
