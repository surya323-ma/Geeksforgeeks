Given a positive integer n, you need to count the numbers less than or equal to n having exactly 9 divisors.

import math

class Solution:
    def countNumbers(self, n):
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0:2] = [False, False]
            for i in range(2, int(limit ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
            return [x for x, val in enumerate(is_prime) if val]

        limit = int(math.isqrt(n))
        primes = sieve(limit)
        prime_squares = [p * p for p in primes if p * p <= n]
        count = 0

        for p in primes:
            if p ** 8 > n:
                break
            count += 1
        for i in range(len(prime_squares)):
            p_sq = prime_squares[i]
            if p_sq * p_sq > n:
                break
            for j in range(i + 1, len(prime_squares)):
                val = p_sq * prime_squares[j]
                if val > n:
                    break
                count += 1
        return count
