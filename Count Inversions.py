Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum

class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        return self.mergeSort(arr, 0, len(arr)-1)     
    def mergeSort(self, arr, start, end):
        if(start >= end):
            return 0
        cnt = 0
        mid = (start + end)//2
        cnt += self.mergeSort(arr, start, mid)
        cnt += self.mergeSort(arr, mid+1, end)
        cnt += self.merge(arr, start, mid, end)
        return cnt
        
    def merge(self, arr, start, mid, end):
        left = start
        right = mid+1
        temp = []
        cnt = 0     
        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                cnt += (mid - left + 1)
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= end:
            temp.append(arr[right])
            right += 1
        for i in range(len(temp)):
            arr[start+i] = temp[i]
        return cnt

Your approach to counting inversions in an array is based on Merge Sort, which efficiently finds and counts pairs (i, j) such that i < j and arr[i] > arr[j]. Here's a detailed breakdown:
Approach:
- Recursive Merge Sort:
- The array is recursively divided into left and right halves until each subarray has one element.
- As the subarrays are merged back together, we count the number of inversions.
- An inversion occurs when an element from the left subarray is greater than an element from the right subarray.
- Counting Inversions During Merge Step:
- While merging two sorted halves, every time an element from the right half is placed before an element from the left half, it contributes to mid - left + 1 inversions.
- The count of such inversions is accumulated across recursive calls.
Complexity Analysis:
- Time Complexity:
- Each merge step takes O(n) time, and since the merge sort divides the array log(n) times, the total complexity is O(n log n).
- Space Complexity:
- The algorithm uses O(n) additional space for the temporary array used during merging.
- If implemented using an in-place approach, space complexity can be reduced to O(1).

