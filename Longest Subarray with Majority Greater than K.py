Given an array arr[] and an integer k, the task is to find the length of longest subarray in which the count of elements greater than k is more than the count of elements less than or equal to 


#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        max_length = 0

        # Convert the array into a +1, -1 form
        modified_arr = [1 if num > k else -1 for num in arr]

        # Use prefix sum with hashmap to track longest valid subarray
        prefix_sum = 0
        prefix_map = {0: -1}  # Base case for when subarray starts from index 0

        for i in range(n):
            prefix_sum += modified_arr[i]

            # If the prefix sum becomes positive, update the max_length
            if prefix_sum > 0:
                max_length = i + 1
            elif prefix_sum - 1 in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum - 1])

            # Store the first occurrence of prefix_sum
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_length
        

#{
 # Driver Code Starts


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends
