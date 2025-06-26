Given a string s consisting of lowercase alphabets and an integer k, your task is to find the minimum possible value of the string after removing exactly k characters.

The value of the string is defined as the sum of the squares of the frequencies of each distinct character present in the string.
#code here
class Solution:
    def minValue(self, s, k):

        d={}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l=list(d.values())
        for j in range(k):
            x=l.index(max(l))
            l[x]=max(l)-1
        a=0
        for i in l:
            a += i**2
        return a
