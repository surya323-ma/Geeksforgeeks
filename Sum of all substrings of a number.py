Given an integer s represented as a string, the task is to get the sum of all possible sub-strings of this string.

Note: The number may have leading zeros.
It is guaranteed that the total sum will fit within a 32-bit signed integer.
  #code here
class Solution:
    def sumSubstrings(self,s):
        su=0
        
        for i in range(1,len(s)+1):
            k=0
            j=k+i
            while j<len(s)+1:
                su+=int(s[k:j])
                k+=1
                j+=1
        return su
 
