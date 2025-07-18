Given a number n, find the maximum possible LCM that can be obtained by selecting three numbers less than or equal to n.
Note : LCM stands for Lowest Common Multiple.
class Solution:
    def lcmTriplets(self, n: int) -> int:
        if n < 3:
            return n
        elif n % 2 != 0:
            return n * (n - 1) * (n - 2)
        elif n % 3 != 0:
            return n * (n - 1) * (n - 3)
        else:
            return (n - 1) * (n - 2) * (n - 3)
