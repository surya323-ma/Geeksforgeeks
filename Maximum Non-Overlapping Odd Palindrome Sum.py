Given a string s consisting of lowercase English letters, find the maximum possible sum of the lengths of any two non-empty and non-overlapping palindromic substrings of odd length.

Formally, choose any two substrings s[i...j] and s[k...l] such that 1 ≤ i ≤ j < k ≤ l ≤ s.size(), both substrings are palindromes of odd length, and they do not overlap. Return the maximum sum of their lengths.

Note: A palindrome is a string that reads the same forward and backward. A substring is a contiguous sequence of characters within the string.
import heapq

class Solution:
    def maxSum(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        d = self.manacherOdd(s)

        maxEnd = [0] * n   # best palindrome length ending exactly at i
        maxStart = [0] * n # best palindrome length starting exactly at i

        # Sweep left->right to compute maxEnd
        pq = []  # using max heap by storing negative values
        centerIdx = 0
        for e in range(n):
            while centerIdx < n and centerIdx <= e:
                c = centerIdx
                B = 1 - 2 * c           # contribution constant
                R = c + d[c] - 1        # rightmost end
                # Using max heap by pushing negative values
                heapq.heappush(pq, (-B, R))
                centerIdx += 1
            while pq and pq[0][1] < e:
                heapq.heappop(pq)
            if pq:
                neg_B, _ = pq[0]
                maxEnd[e] = 2 * e + (-neg_B)  # 2*e + B
            else:
                maxEnd[e] = 1

        # prefix maxima
        maxPref = [0] * n
        cur = 0
        for i in range(n):
            if maxEnd[i] > cur:
                cur = maxEnd[i]
            maxPref[i] = cur

        # Sweep right->left to compute maxStart
        pq2 = []  # max heap using negative values
        centerIdx2 = n - 1
        for sIdx in range(n-1, -1, -1):
            while centerIdx2 >= 0 and centerIdx2 >= sIdx:
                c = centerIdx2
                C = 2 * c + 1
                L = c - d[c] + 1
                heapq.heappush(pq2, (-C, L))
                centerIdx2 -= 1
            while pq2 and pq2[0][1] > sIdx:
                heapq.heappop(pq2)
            if pq2:
                neg_C, _ = pq2[0]
                maxStart[sIdx] = -2 * sIdx + (-neg_C)
            else:
                maxStart[sIdx] = 1

        # suffix maxima
        maxSuff = [0] * n
        cur = 0
        for i in range(n-1, -1, -1):
            if maxStart[i] > cur:
                cur = maxStart[i]
            maxSuff[i] = cur

        # combine non-overlapping
        ans = 0
        for i in range(n - 1):
            ans = max(ans, maxPref[i] + maxSuff[i + 1])
        return ans

    def manacherOdd(self, s: str) -> list:
        n = len(s)
        d = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1
            if i <= r:
                k = min(d[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
        return d
