Given an array arr[] consisting of positive integers, your task is to find the length of the longest subarray that contains at most two distinct integers.
#code here
  class Solution:
    def totalElements(self, arr):
        left = 0
        freq = {}
        max_len = 0

        for right, num in enumerate(arr):
            freq[num] = freq.get(num, 0) + 1

        # Shrink window if more than two distinct values
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

        # Update maximum length
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len   
