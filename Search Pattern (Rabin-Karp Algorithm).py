Given two strings:

A text string in which you want to search.
A pattern string that you are looking for within the text.
Return all positions (1-based indexing) where the pattern occurs as a substring in the text. If the pattern does not occur, return an empty list.
All characters in both strings are lowercase English letters (a to z).

class Solution:
    def search(self, pat, txt):
        st=0
        res=[]
        while((pos:=txt.find(pat,st))!=-1):
            res.append(pos+1)
            st=pos+1
        return res
        # code here
