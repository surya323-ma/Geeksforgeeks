You are given a string s consisting only of the characters '(' and ')'. Your task is to determine the minimum number of parentheses (either '(' or ')') that must be inserted at any positions to make the string s a valid parentheses string.

A parentheses string is considered valid if:

Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
Every closing parenthesis ')' has a corresponding opening parenthesis '('.
Parentheses are properly nested.
class Solution:
    def minParentheses(self, s):
        open_count = 0   
        insertions = 0  

        for char in s:
            if char == '(':
                open_count += 1
            else:  # char == ')'
                if open_count > 0:
                    open_count -= 1  
                else:
                    insertions += 1  
        insertions += open_count
        return insertions
