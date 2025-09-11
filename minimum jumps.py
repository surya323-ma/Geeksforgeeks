You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
For example:
If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.

class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0  
        if arr[0] == 0:
            return -1 
        jumps = 0
        curr_end = 0
        farthest = 0
        for i in range(n - 1): 
            farthest = max(farthest, i + arr[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                if curr_end >= n - 1:
                    return jumps
        return -1
