Given a single string s, the task is to check if it is a palindrome sentence or not.
A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols that reads the same backward as forward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters (including spaces and punctuation).
class Solution:
	def isPalinSent(self, s):
		# code here
        str_ = s.lower()
        rev_str = str_[::-1]

        i, j, n = 0, 0, len(s)
        while i < n and j < n:
            res1 = self.isAlphaNumeric(str_[i])
            res2 = self.isAlphaNumeric(rev_str[j])

            if not res1:
                i += 1
            elif not res2:
                j += 1
            elif str_[i] == rev_str[j]:
                i += 1
                j += 1
            else:
                return False

        return True

    def isAlphaNumeric(self, ch: str) -> bool:
        return ch.isalnum()
