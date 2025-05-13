Given a string S which consists of only lowercase English alphabets, you have to perform the below operations:
If the string S contains any repeating character, remove the first repeating character and reverse the string and again perform the above operation on the modified string, otherwise, you stop.
You have to find the final string.

from collections import Counter

class Solution:
    def removeReverse(self, S):
        m = Counter(S)
        n = len(S)
        ans1 = []
        ans2 = []
        i, e = 0, n - 1
        f = 1
        cnt = 0

        while i <= e:
            if f == 1:
                if m[S[i]] > 1:
                    m[S[i]] -= 1
                    f = 0
                    i += 1
                    cnt += 1
                else:
                    ans1.append(S[i])
                    i += 1
            else:
                if m[S[e]] > 1:
                    m[S[e]] -= 1
                    f = 1
                    e -= 1
                    cnt += 1
                else:
                    ans2.append(S[e])
                    e -= 1

        ans2.reverse()
        ans = "".join(ans1) + "".join(ans2)

        if cnt % 2 != 0:
            ans = ans[::-1]

        return ans
