Given a circular integer array arr[], the task is to determine the next greater element (NGE) for each element in the array.

The next greater element of an element arr[i] is the first element that is greater than arr[i] when traversing circularly. If no such element exists, return -1 for that position.

Note: Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once.
class Solution:
    def nextGreater(self, arr):
        # code here
        n = len(arr)
        result = [-1] * n
        stack = []

    # Traverse the array twice to simulate circular behavior
        for i in range(2 * n - 1, -1, -1):
            current = arr[i % n]
        # Maintain a decreasing stack
            while stack and arr[stack[-1]] <= current:
                stack.pop()
            if i < n:
                if stack:
                    result[i] = arr[stack[-1]]
            stack.append(i % n)

        return result
