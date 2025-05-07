Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
Note: Return an empty list in case of no occurrences of pattern.

#User function Template for python3

class Solution:
    def search(self, pat, txt):
        n=len(pat)
        ans=[]
        for i in range(0,len(txt)-n+1):
            if txt[i:i+n]==pat:
                ans.append(i)
        
        return ans
                
        # code here
