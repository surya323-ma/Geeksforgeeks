Given an array arr[] containing 2*n + 2 positive numbers, out of which 2*n numbers exist in pairs whereas only two number occur exactly once and are distinct. Find the other two numbers. Return the answer in increasing order.

#User function Template for python3

class Solution:
    def singleNum(self, arr):
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        r=[]
        for i in d:
            if d[i]==1:
                r.append(i)
        r.sort()
        return r
           
        # Code here
APPROACH
Your solution uses a dictionary (hash map) to count occurrences of each number in the array. Then, it iterates over the dictionary to find elements that appear only once and sorts the result before returning.
- Time Complexity:
- - Constructing the dictionary takes O(N) time, where N is the length of arr.
-  the worst-case complexity is O(N + K log K).
- Space Complexity:
- The dictionary (d) stores counts for up to N elements, resulting in O(N) space.
- The list (r) stores at most N elements in the worst case, contributing another O(N).

