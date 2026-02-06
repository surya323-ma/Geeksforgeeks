You are given three arrays a[], b[], c[] of the same size . Find a triplet such that (maximum-minimum) in that triplet is the minimum of all the triplets. A triplet should be selected so that it should have one number from each of the three given arrays. This triplet is the happiest among all the possible triplets. Print the triplet in decreasing order.

Note: If there are 2 or more smallest difference triplets, then the one with the smallest sum of its elements should be displayed.
class Solution:
    def smallestDiff(self, a, b, c):
        a.sort()
        b.sort()
        c.sort()
        
        i = j = k = 0
        best_triplet = None
        best_diff = float('inf')
        best_sum = float('inf')
        
        while i < len(a) and j < len(b) and k < len(c):
            x, y, z = a[i], b[j], c[k]
            max_val = max(x, y, z)
            min_val = min(x, y, z)
            diff = max_val - min_val
            s = x + y + z
            
            if diff < best_diff or (diff == best_diff and s < best_sum):
                best_diff = diff
                best_sum = s
                best_triplet = (x, y, z)
            
            # Move the pointer of the minimum element
            if min_val == x:
                i += 1
            elif min_val == y:
                j += 1
            else:
                k += 1
        
        return sorted(best_triplet, reverse=True)
