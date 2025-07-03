You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1
class Solution:
    def longestKSubstr(self, s, k):
        #sam
        from collections import defaultdict
        mp = defaultdict(int)
        n = len(s)
        left = 0
        count = 0
        for r in range(n):
            mp[s[r]] += 1
            while len(mp)>k and left<n:
                if mp[s[left]]==1:
                    del mp[s[left]]
                else:
                    mp[s[left]] -=1
                left += 1
            if len(mp)==k:
                count = max(count,r-left+1)
            # print(mp)
        return -1 if count == 0 else count
