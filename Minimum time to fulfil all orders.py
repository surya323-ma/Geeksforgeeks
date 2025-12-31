Geek is organizing a party at his house. For the party, he needs exactly n donuts for the guests. Geek decides to order the donuts from a nearby restaurant, which has m chefs and each chef has a rank r.
A chef with rank r can make 1 donut in the first r minutes, 1 more donut in the next 2r minutes, 1 more donut in the next 3r minutes, and so on.
For example, a chef with rank 2, can make one donut in 2 minutes, one more donut in the next 4 minutes, and one more in the next 6 minutes. So, it take 2 + 4 + 6 = 12 minutes to make 3 donuts. A chef can move on to making the next donut only after completing the previous one. All the chefs can work simultaneously.
Since, it's time for the party, Geek wants to know the minimum time required in completing n donuts. Return an integer denoting the minimum time.
class Solution:
    def minTime(self, ranks, n):
        # code here
        left, right = 0, max(ranks) * n * (n + 1) // 2
        ans = right
        while left <= right:
            mid = (left + right) // 2
            donuts = 0
            for r in ranks:
            # k such that r*k*(k+1)/2 <= mid
                k = int((math.isqrt(1 + (8 * mid) // r) - 1) // 2)
                donuts += k
                if donuts >= n:  # early break
                    break
            if donuts >= n:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
