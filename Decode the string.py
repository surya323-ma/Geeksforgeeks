Given an encoded string s, decode it by expanding the pattern k[substring], where the substring inside brackets is written k times. k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets. Return the final decoded string.

Note: The test cases are generated so that the length of the output string will never exceed 105 .
class Solution:
    def decodedString(self, s):
        stack = []
        current_str = ""
        current_num = 0
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char

        return current_str
