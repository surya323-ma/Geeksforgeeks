Given an array arr[] and an integer k, divide the array into k contiguous subarrays such that the maximum sum among these subarrays is minimized. Find this minimum possible maximum sum.
#code 
class Solution:
    def splitArray(self, nums, k):
        def is_valid(mid):
            count, total = 1, 0
            for num in nums:
                if total + num <= mid:
                    total += num
                else:
                    count += 1
                    total = num
            return count <= k

        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if is_valid(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
