You are given a lowercase string s, determine the total number of distinct strings that can be formed using the following rules:

Identify all unique vowels (a, e, i, o, u) present in the string.
For each distinct vowel, choose exactly one of its occurrences from s. If a vowel appears multiple times, each occurrence represents a unique selection choice.
Generate all possible permutations of the selected vowels. Each unique arrangement counts as a distinct string.
Return the total number of such distinct strings.

from collections import Counter

class Solution:
    def vowelCount(self, s: str) -> int:
        mpp = Counter(s)
        mul = 1
        prod = 0
        
        for vowel in 'aeiou':
            if mpp[vowel]:
                prod += 1
                mul *= mpp[vowel]

        temp = prod
        for i in range(2, temp):
            prod *= i

        return prod * mul
