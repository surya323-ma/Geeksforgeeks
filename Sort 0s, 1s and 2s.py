Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        zero=0
        one=0
        two=0
        for i in arr:
            if i==1:
                one+=1
            elif i==2:
                two+=1
            else:
                zero+=1
        arr.clear()
        arr.extend([0]*zero)
        arr.extend([1]*one)
        arr.extend([2]*two)
        # code here

Your approach effectively counts the occurrences of 0, 1, and 2 and then reconstructs the array based on these counts. This is a counting sort-based approach and works well when sorting elements within a limited range.
Here are a couple of alternative approaches you might find interesting:
- Dutch National Flag Algorithm (Two-Pointer Approach):
- Uses three pointers (low, mid, and high) to partition the array.
- Iterates through the array and swaps elements to place 0s, 1s, and 2s in the correct order with constant space complexity.
- More efficient with O(n) time complexity and O(1) space complexity.
- In-place Sorting (Quicksort or Merge Sort):
- If allowed, you could use a sorting algorithm like Quicksort or Merge Sort, though they may take O(n log n) time.
- Since the problem only deals with three unique values (0, 1, 2), specialized sorting methods like Counting Sort or the Dutch National Flag Algorithm are preferable.
