Given a sorted array arr[] containing distinct positive integers that has been rotated at some unknown pivot, and a value x. Your task is to count the number of elements in the array that are less than or equal to x.
class Solution:
    @staticmethod
    def countLessEqual(arr, x):
        n = len(arr)

        # Find pivot (index of smallest element)
        def findPivot():
            low, high = 0, n - 1
            while low < high:
                mid = (low + high) // 2
                if arr[mid] > arr[high]:
                    low = mid + 1
                else:
                    high = mid
            return low

        # Binary search for upper bound in [low..high]
        def countInRange(low, high):
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= x:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        pivot = findPivot()

        # Search in both halves
        leftCount = countInRange(0, pivot - 1)
        rightCount = countInRange(pivot, n - 1)

        total = 0
        if leftCount != -1:
            total += leftCount + 1
        if rightCount != -1:
            total += rightCount - pivot + 1

        return total
