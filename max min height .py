Given a garden with n flowers planted in a row, that is represented by an array arr[], where arr[i] denotes the height of the ith flower.You will water them for k days. In one day you can water w continuous flowers. Whenever you water a flower its height increases by 1 unit. You have to maximize the minimum height of all flowers after  k days of watering.
                                                                                                                                                            class Solution:
    def maxMinHeight(self, arr, k, w):
        def is_possible(target):
            n = len(arr)
            added = [0] * n
            curr_add = 0
            ops = 0
            
            for i in range(n):
                if i >= w:
                    curr_add -= added[i - w]
                if arr[i] + curr_add < target:
                    need = target - (arr[i] + curr_add)
                    if ops + need > k:
                        return False
                    added[i] = need
                    curr_add += need
                    ops += need
            return True

        low, high = min(arr), min(arr) + k
        result = low
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result
