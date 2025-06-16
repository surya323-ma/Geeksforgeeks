You are given an array heights[] representing the heights of towers and another array cost[] where each element represents the cost of modifying the height of respective tower.

The goal is to make all towers of same height by either adding or removing blocks from each tower.
Modifying the height of tower (add or remove) 'i' by 1 unit costs cost[i].
Return the minimum cost to equalize the heights of all towers.
two type search method
#Binarysearch
class Solution:
    def minCost(self, heights, cost):
        def calc(target):
            return sum(abs(h - target) * c for h, c in zip(heights, cost))
        
        low, high = min(heights), max(heights)
        while low < high:
            mid = (low + high) // 2
            cost_mid = calc(mid)
            cost_next = calc(mid + 1)
            if cost_mid <= cost_next:
                high = mid
            else:
                low = mid + 1
        return calc(low)
#codeherew
#Ternarysearch
class Solution:
    def minCost(self, heights, cost):
        def calc(m):
            return sum(abs(h - m) * c for h, c in zip(heights, cost))
        low, high = min(heights), max(heights)
        while high - low > 2:
            t = (high - low) // 3
            mid1 = low + t
            mid2 = high - t
            c1 = calc(mid1)
            c2 = calc(mid2)
            if c1 < c2:
                high = mid2
            else:
                low = mid1
        return min(calc(h) for h in range(low, high + 1))
