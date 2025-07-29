Given a string s consisting of lowercase English letters, for every character whose first and last occurrences are at different positions, calculate the sum of ASCII values of characters strictly between its first and last occurrence.
Return all such non-zero sums (order does not matter).


from collections import defaultdict
class Solution:
    def asciirange(self, s):
        dic=defaultdict(list)
        for i in range(len(s)):
            dic[s[i]].append(i)
        prefix=[0]
        for i in s:
            prefix.append(prefix[-1]+ord(i))
        prefix.pop(0)
        ans=[]
        for i,j in dic.items():
            if len(j)>1:
                a=prefix[j[-1]-1]-prefix[j[0]]
                if a!=0:
                    ans.append(a)
        return sorted(ans)
