You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.

Note: The characters in the strings are in lowercase.

#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        if len(s1)!=len(s2) or not s1 or not s2:
            return False
        return s2 in (s1+s1) and s1 in (s2+s2)
        #code here

Your approach is simple and effective for checking if two strings are rotations of each other. Let's break it down:
Approach:
- Check the Lengths:
- If the lengths of s1 and s2 are not equal, they cannot be rotations.
- Also, if either of the strings is empty, return False.
- Concatenate s1 with Itself:
- If s2 is a rotation of s1, then s2 will always be a substring of s1+s1.
- Similarly, s1 will be a substring of s2+s2 if s1 is a rotation of s2.
- Return the Result:
- We check if s2 exists within s1+s1 and vice versa.
- If either condition holds true, the strings are rotations, otherwise they are not.
Time Complexity:
 - String concatenation and substring search both take O(N) time.
- Hence, the overall complexity is O(N), making it highly efficient

                                
