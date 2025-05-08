Given a sorted array arr[] that represents an Arithmetic Progression (AP) with exactly one missing element, find the missing number.

Note: An element will always exist that, upon inserting into a sequence forms Arithmetic progression. If the given sequence already forms a valid complete AP, return the (n+1)-th element that would come next in the sequence.

        # code here        
class Solution:
     def findMissing(self, arr):
        # compute the difference of the AP
        d = min(arr[1] - arr[0], arr[-1] -arr[-2])
        # Compare the difference to find the missing term
        return next((arr[i] + d for i in range(len(arr)-1) if d != arr[i+1] - arr[i]), arr[-1]+d)



Your approach efficiently finds the missing element in the arithmetic progression using a generator expression within next(). Here's a breakdown:
Approach:
- Determine the Common Difference:
- Compute the minimum difference (d) between consecutive elements, assuming only one missing element.
- Find the Missing Term:
- Iterate through the array, checking if the difference between consecutive elements deviates from d.
- If a mismatch is found, return the expected missing element.
- If no mismatch is found, return the next term in sequence.
Time Complexity:
- O(n): The approach involves a single pass through the array (O(n)).
- The next() function efficiently finds the missing element without extra space.
Space Complexity:
- O(1): No additional data structures are used, making it memory efficient
