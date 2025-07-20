You are given an integer n representing the number of digits in a number, and an array arr[] containing digits from 0 to 9. Your have to count how many n-digit positive integers can be formed such that at least one digit from the array arr[] appears in the number.

class Solution:
    def countValid(self, n, arr):
        forbidden = set(arr)
        allowed = set(range(10)) - forbidden

        if not allowed:
            return 0  # No allowed digits means no valid number

        if n == 1:
            # Only digits 1–9 are valid for single-digit numbers
            total_valid = sum(1 for d in allowed if d != 0)
        else:
            # First digit must be non-zero
            first_digit_opts = [d for d in allowed if d != 0]
            total_valid = len(first_digit_opts) * pow(len(allowed), n - 1)

        total_all = 9 * pow(10, n - 1) if n > 1 else 9
        return total_all - total_valid
