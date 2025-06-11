You are given two arrays, color and radius, representing a sequence of balls:
color[i] is the color of the i-th ball.
radius[i] is the radius of the i-th ball.
If two consecutive balls have the same color and radius, remove them both. Repeat this process until no more such pairs exist.
Return the number of balls remaining after all possible removals.
  #cde here
  class Solution:
    def findLength(self, color, radius):
        stack = []
        for i in range(len(color)):
            if stack:
                key = stack[-1]
                if color[key] == color[i] and radius[key] == radius[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)
