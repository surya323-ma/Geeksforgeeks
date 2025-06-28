You are given two unsorted arrays a[] and b[]. Both arrays may contain duplicate elements. For each element in a[], your task is to count how many elements in b[] are less than or equal to that element. 
#code here
class Solution:
    def countLessEq(self, a, b):
        if not b:
            return [0] * len(a)
    
        maxB = max(max(b), max(a))  # Handle items in 'a' greater than max(b)
        count = [0] * (maxB + 2)     # Extra space to avoid index issues

        for num in b:
            count[num] += 1
        for i in range(1, maxB + 1):
            count[i] += count[i - 1]

        return [count[val] for val in a]
        
