Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.

Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

#User function Template for python3

class Solution:
    def insertInterval(self, intervals, newInterval):
        intervals.append(newInterval)
        return self.merge(intervals)
        
    def merge(self,intervals):

        intervals.sort()
        res=[]
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            last=res[-1]
            curr=intervals[i]
            if(last[1]>=curr[0]):
                last[1]=max(last[1],curr[1])
            else:
                res.append(intervals[i])
        return res        
