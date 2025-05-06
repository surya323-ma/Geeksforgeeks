Given an array arr[] of distinct positive integers, your task is to find all its subsets. The subsets should be returned in lexicographical order.

#User function Template for python3

class Solution:
    def subsets(self, arr):
        res=[]
        arr.sort()
        def subset(curr,index):
            if index >=len(arr):
                res.append(curr.copy())
                return
            else:
                curr.append(arr[index])
                subset(curr,index+1)
                curr.pop()
                subset(curr,index+1)
        subset([],0)
        res.sort()
        return res
        # code here
yes my approach is recursive method to find all possible subsets of an array. Explain like I'm five.

Approach:

- Sorting the Array: You first sort the array so that subsets are generated in a lexicographical order.
- Recursive Function (subset):
- If the index > end of the array the subset in question is saved in the result list.
- Otherwise, the function explores two possibilities:
- Include the current element in the subset.
- Exclude the current element and move to the next index.
- This ensures all possible subsets are explored.
- Sorting the result: When you 've created all subsets you sort them so they are in a constant order.
