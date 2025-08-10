Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2.

Note: A substring is palindromic if it reads the same forwards and backwards.
#User function Template for python3

class Solution:
    
    def countPS(self, s):
        cnt = 0
        n = len(s)
        
        for i in range(n):
            l,r=i,i
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>=2:
                    cnt+=1
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                if r-l+1>=2:
                    cnt+=1
                l-=1
                r+=1
        return cnt

