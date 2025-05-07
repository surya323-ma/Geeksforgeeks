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
        
      
Your approach uses a brute-force method to find the first non-repeating character in the string. Let's break it down:
Approach:
- Iterate through each character in the string.
- For each character, iterate again through the string to check if it appears more than once.
- If the character is unique, return it.
- If no unique character is found, return '$'.
Complexity Analysis:
- The outer loop runs O(N) times, where N is the length of the string.
- The inner loop also runs O(N) times.
- Hence, the overall time complexity is O(N²), making it inefficient for large inputs.

