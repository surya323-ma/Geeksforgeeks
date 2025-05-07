Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward.

class Solution:
    def minChar(self, s):
        i=1
        len_=0
        temp=s+"$"+s[::-1]
        lps=[0]*len(temp)
        while(i<len(temp)):
            if temp[i]==temp[len_]:
                len_+=1
                lps[i]=len_
                i+=1
            else:
                if(len_==0):
                    lps[i]=0
                    i+=1
                else:
                    len_=lps[len_-1]
        return len(s)-lps[-1]


Your code cleverly uses KMP's Longest Prefix Suffix (LPS) array to determine the minimum number of characters required to make a string a palindrome. Let's break down the approach:
Approach:
- Concatenation Trick:
- You create a temporary string temp by appending:
- The original string s
- A special delimiter ($) to avoid overlap
- The reversed version of s
- This helps in determining the longest palindromic prefix.
- Building the LPS Array using KMP Algorithm:
- The LPS array stores the longest proper prefix of temp which is also a suffix.
- This helps in identifying the longest prefix of s that matches the suffix of the reversed s.
- Computing the Result:
- The minimum characters required to make s a palindrome is: [ \text{len(s)} - \text{lps[-1]} ]
- Here, lps[-1] gives the longest matching prefix of s with the reversed s.
Complexity Analysis:
- Building the LPS array takes O(N) time.
- The overall time complexity is O(N), making it highly efficient.
