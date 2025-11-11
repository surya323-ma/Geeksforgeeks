Given two strings s1 and s2, find the length of the smallest string which has both s1 and s2 as its sub-sequences.
Note: s1 and s2 can have both uppercase and lowercase English letters.
class Solution:
    @staticmethod
    def minSuperSeq(X: str, Y: str) -> int:
        n, m = len(X), len(Y)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = dp[i][j] + 1 if X[i] == Y[j] else max(dp[i][j+1], dp[i+1][j])
        return n + m - dp[n][m]
