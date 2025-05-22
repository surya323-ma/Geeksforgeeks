Given a string s, write a program to delete the minimum number of characters from the string so that the resultant string is a palindrome, while maintaining the order of characters.
#code here
class Solution:
    def minDeletions(self, s):
        r, n = s[::-1], len(s)
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                curr[j] = 1 + prev[j - 1] if s[i - 1] == r[j - 1] else max(prev[j], curr[j - 1])
            prev = curr
        return n - prev[n]
