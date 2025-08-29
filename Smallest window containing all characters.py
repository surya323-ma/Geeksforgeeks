Given two strings s and p. Find the smallest substring in s consisting of all the characters (including duplicates) of the string p. Return empty string in case no such substring is present.
If there are multiple such substring of the same length found, return the one with the least starting index.
from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        need, window = Counter(p), Counter()
        have, left = 0, 0
        res, min_len = "", float("inf")

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == len(need):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return res
