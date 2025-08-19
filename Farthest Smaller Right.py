You are given an array arr[]. For each element at index i (0-based indexing), find the farthest index j to the right (i.e., j > i) such that arr[j] < arr[i]. If no such index exists for a given position, return -1 for that index. Return the resulting array of answers.
class Solution:
    def farMin(self, arr):
        maxi=-1
        ans=[-1]*(len(arr))
        for val,ind in sorted((arr[i],i) for i in range(len(arr))):
            if ind<maxi:
                ans[ind]=maxi
            maxi=max(ind,maxi)
        return ans
 
