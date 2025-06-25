Given a string s consisting only lowercase alphabetic characters, check whether it is possible to remove at most one character such that the  frequency of each distinct character in the string becomes same. Return true if it is possible; otherwise, return false.

from collections import Counter
class Solution:
    def sameFreq(self, s: str) -> bool:
        char_freq = Counter(s)
        freq_count = Counter(char_freq.values())
        if len(freq_count) == 1:
            return True
        if len(freq_count) > 2:
            return False
        freq1, freq2 = freq_count.keys()
        count1, count2 = freq_count[freq1], freq_count[freq2]
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
            return True
        if (abs(freq1 - freq2) == 1) and ((freq1 > freq2 and count1 == 1) or (freq2 > freq1 and count2 == 1)):
            return True

        return False

        #code here
