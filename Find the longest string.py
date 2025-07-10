Given an array of strings words[]. Find the longest string in words[] such that every prefix of it is also present in the array words[]. 

Note: If multiple strings have the same maximum length, return the lexicographically smallest one.

  class Solution():
    def longestString(self, words):
        words_set = set(words)
        result = ""

        for word in sorted(words):
            is_valid = True
            for i in range(1, len(word)):
                if word[:i] not in words_set:
                    is_valid = False
                    break
            if is_valid:
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        return result    # code here
        
        
