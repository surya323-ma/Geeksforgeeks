You are given a binary string s consisting only of characters '0' and '1'. Your task is to split this string into the minimum number of non-empty substrings such that:

Each substring represents a power of 5 in decimal (e.g., 1, 5, 25, 125, ...).
No substring should have leading zeros.
Return the minimum number of such pieces the string can be divided into.
Note: If it is not possible to split the string in this way, return -1.
class Solution:
    def is_power_of_5(self, bin_str):
        if bin_str[0] == '0':
            return False
        num = int(bin_str, 2)
        while num > 1:
            if num % 5 != 0:
                return False
            num //= 5
        return num == 1

    def cuts(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if self.is_power_of_5(sub):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1
