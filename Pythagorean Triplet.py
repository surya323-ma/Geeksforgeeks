Given an array arr[], return true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.
#code here
class Solution:
    def pythagoreanTriplet(self, arr):
        num_set = set(arr)
        n = len(arr)
        
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                
                # Calculate c² = a² + b²
                c_squared = a * a + b * b
                
                # Check if c is a perfect square
                c = int(c_squared ** 0.5)
                if c * c == c_squared and c in num_set:
                    return True
        
        return False
