Given a string s consisting of lowercase English Letters. Return the first non-repeating character in s.
If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1

#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        n=len(s)
        for i in range(n):
            found=False
            
            for j in range(n):
                if i!=j and s[i]==s[j]:
                    found=True
                    break
            if not found:
                return s[i]
        return '$'
        
      
    
