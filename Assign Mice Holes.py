You are given two arrays mices[] and holes[] of the same size. The array mices[] represents the positions of the mice on a straight line, while the array holes[] represents the positions of the holes on the same line. Each hole can accommodate exactly one mouse. A mouse can either stay in its current position, move one step to the right, or move one step to the left, and each move takes one minute. The task is to assign each mouse to a distinct hole in such a way that the time taken by the last mouse to reach its hole is minimized.
class Solution:
    def assignHole(self, mices, holes):
        mices.sort()
        holes.sort()
        max_time=0
        for i in range(len(mices)):
            max_time=max(max_time,abs(mices[i]-holes[i]))
        return max_time
