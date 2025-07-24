We have a wooden plank of length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second, with some moving left and others right.
When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time. When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

Given an integer n and two integer arrays left[] and right[], the positions of the ants moving to the left and the right, return the time when the last ant(s) fall out of the plank.

#User function Template for python3
class Solution:
    def getLastMoment(self, n, left, right):
        ans=0
        
        for i in left:
            ans =max(ans,i)
        for j in right:
            ans=max(ans,n-j)
        return ans
        #code here
