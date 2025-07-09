Given an array arr[] of positive integers, find the total sum of the minimum elements of every possible subarrays.

Note: It is guaranteed that the total sum will fit within a 32-bit unsigned integer.
class Solution:
    def sumSubMins(self, arr):
        # Code here
        n = len(arr)
        stack = []
        prev_smaller = [0] * n
        next_smaller = [0] * n

    # Previous less element
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev_smaller[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

    # Clear stack for next pass
        stack.clear()

    # Next less element
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] - i if stack else n - i
            stack.append(i)

    # Final result
        total = 0
        for i in range(n):
            total += arr[i] * prev_smaller[i] * next_smaller[i]
        
        return total   
