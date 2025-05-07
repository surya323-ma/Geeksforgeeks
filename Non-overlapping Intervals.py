Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        cnt = 0
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt += 1
                end = min(intervals[i][1], end)
            else:
                end = intervals[i][1]
        return cnt
 
Approach:
This function aims to find the minimum number of intervals that need to be removed so that the remaining intervals do not overlap. Here’s how it works:
- Sort the intervals: It sorts the intervals based on their start time to process them in order.
- Iterate through intervals: It traverses the sorted list and keeps track of the end of the current interval.
- Compare with previous interval:
- If the start of the current interval is less than the previous interval’s end, there is an overlap.
- The function increments cnt to count the removal and updates end to the minimum of the overlapping intervals' end values (keeping the smaller range).
- If there’s no overlap, it simply updates end to the new interval’s end.
Complexity Analysis:
- Sorting the intervals: (O(N \log N)) due to sorting.
- Iteration: (O(N)), where (N) is the number of intervals.
