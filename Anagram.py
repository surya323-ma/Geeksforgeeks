Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

Note: You can assume both the strings s1 & s2 are non-emp

#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    
    def areAnagrams(self, s1, s2):
        if(sorted(s1)==sorted(s2)):
            return True
        else:
            return False
        #code here
