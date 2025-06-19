Given a string s consisting of only uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa
#code here
class Solution:
    def caseSort(self, s):
        uppers = iter(sorted(c for c in s if c.isupper()))
        lowers = iter(sorted(c for c in s if c.islower()))
        
        result = [next(lowers) if c.islower() else next(uppers) for c in s]
        return ''.join(result)
