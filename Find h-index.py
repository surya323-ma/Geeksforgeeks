Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper. The task is to find the H-index.

H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times.

#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]<i+1:
                return i
        return len(citations)
        #code here
Your approach to finding the h-index is straightforward and efficient. 
Approach:
- You sort the citation list in descending order.
- You iterate through the sorted list to find the largest i such that citations[i] >= i + 1.
- As soon as the condition fails (citations[i] < i + 1), return i since it represents the maximum number of papers with at least i citations.
- If all values satisfy the condition, return the length of citations, meaning all papers qualify.
Complexity Analysis:
- Sorting takes O(n log n).
- Iterating through the list takes O(n).
- So the overall time complexity is O(n log n).
- Space complexity is O(1) (in-place sorting is used).
Optimized Approach (Bucket Sort)
- Instead of sorting, you can use counting-based bucket sort to store citation frequencies, reducing time complexity to O(n).
- This is useful when dealing with large datasets.

