Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231.


class Solution:
    def myAtoi(self, s: str) -> int:
       
        s = s.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]  
        elif s[0] == '+':
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break  
            result = result * 10 + int(char)
        
        result *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result



Your solution for myAtoi() employs a systematic and logical technique to parse a string into an integer with edge case handling for whitespace, signs, and overflow. Here's a brief overview of your solution:
Approach Summary:
- Trim Whitespace: You eliminate leading and trailing spaces with .strip().
- Handle Empty String: If the string is reduced to empty after trimming, return 0.
- Check for Sign: If the initial character is '-', set sign = -1. If it is '+', proceed with processing without changing the sign.
- Extract Digits: Loop through the characters, adding numeric values to result until a non-digit character is found.
- Apply Sign: Multiply the last number by sign to compensate for negative inputs.
- Handle Overflow: Clamp the result within the 32-bit integer range using pre-defined limits (INT_MAX and INT_MIN).
- Return Processed Integer: Return the processed value keeping the constraints in mind.
