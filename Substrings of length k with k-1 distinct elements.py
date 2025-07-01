Given a string s consisting only lowercase alphabets and an integer k. Find the count of all substrings of length k which have exactly k-1 distinct characters.
# code herer
from collections import defaultdict

class Solution:
    def substrCount(self, s, k):
        if k > len(s):
            return 0

        count = 0
        freq_map = defaultdict(int)
        left = 0

        for right in range(len(s)):
            freq_map[s[right]] += 1

            if right - left + 1 > k:
                freq_map[s[left]] -= 1
                if freq_map[s[left]] == 0:
                    del freq_map[s[left]]
                left += 1

            if right - left + 1 == k:
                if len(freq_map) == k - 1:
                    count += 1

        return count
