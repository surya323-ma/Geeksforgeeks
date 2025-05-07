Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

class Solution:
    def mergeOverlap(self, arr):
        #Code here
        arr.sort()      
        i = 0
        j = 1
        while j < len(arr):
            if arr[j][0] <= arr[i][1] <= arr[j][1]:
                arr[i][1] = arr[j][1]
                del arr[j]
            elif arr[i][0] <= arr[j][1] <= arr[i][1]:
                arr[j][1] = arr[i][1]
                arr[j][0] = arr[i][0]
                del arr[i]
            else:
                i += 1
                j += 1           
        return arr

Approach
- Sorting: The array of intervals is sorted based on the starting value.
- Merging: You traverse the sorted list using two pointers (i and j), attempting to merge overlapping intervals by adjusting their boundaries and deleting elements from the list.
Complexity Analysis
- Sorting: Sorting the list takes O(N log N).
- Merging: Since you're using del arr[j] or del arr[i] (which involves shifting elements), worst-case complexity can be O(N²) due to repeated deletions and shifts.
