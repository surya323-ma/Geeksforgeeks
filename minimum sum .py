Given an array arr[ ] consisting of digits, your task is to form two numbers using all the digits such that their sum is minimized. Return the minimum possible sum as a string with no leading zeroes.
#code
  class Solution:
    def minSum(self, arr):
        arr.sort()
        num1, num2 = '', ''
        
        # Form two numbers by distributing digits alternately
        for i, digit in enumerate(arr):
            if i % 2 == 0:
                num1 += str(digit)
            else:
                num2 += str(digit)
        
        # Helper to perform addition on two string numbers
        def add_strings(a, b):
            i, j = len(a) - 1, len(b) - 1
            carry = 0
            result = []

            while i >= 0 or j >= 0 or carry:
                d1 = int(a[i]) if i >= 0 else 0
                d2 = int(b[j]) if j >= 0 else 0
                total = d1 + d2 + carry
                result.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return ''.join(result[::-1]).lstrip('0') or '0'

        return add_strings(num1, num2)
