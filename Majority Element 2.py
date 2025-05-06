You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.
class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        result=[]
        train=set(arr)
        for i in train:
            if arr.count(i)>len(arr)/3:
                result.append(i)
        result=sorted(result)
        return result
        #Your Code goes here.
Approach:
This solution finds majority elements in an array that appear more than n/3 times using the following steps:
- Convert the array into a set (to remove duplicates).
- Iterate through unique elements and check if their count exceeds n/3.
- Store and sort the qualifying elements before returning.
This method is straightforward but inefficient due to multiple count operations.
Complexity Analysis:
- Time Complexity: O(n²) – Since arr.count(i) is O(n) and we iterate over O(n) unique elements, worst-case complexity is O(n²).
- Space Complexity: O(n) – A set is used to store unique elements and a list for results.
