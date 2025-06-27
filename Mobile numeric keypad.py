There is a standard numeric keypad on a mobile phone. You can press the current button or any button that is directly above, below, to the left, or to the right of it. For example, if you press 5, then pressing 2, 4, 6, or 8 is allowed. However, diagonal movements and pressing the bottom row corner buttons (* and #) are not allowed.
#code here
                                                                                                                                                                                                                                                                                                                     from functools import lru_cache

class Solution:
    def getCount(self, n):
        # Keypad layout
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [None, 0, None]
        ]
        
        # Valid moves: stay, up, down, left, right
        moves = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

        @lru_cache(maxsize=None)
        def helper(i, j, cnt):
            if i < 0 or j < 0 or i >= 4 or j >= 3 or board[i][j] is None:
                return 0
            if cnt == 1:
                return 1
            return sum(helper(i + dx, j + dy, cnt - 1) for dx, dy in moves)

        total = 0
        for i in range(4):
            for j in range(3):
                if board[i][j] is not None:
                    total += helper(i, j, n)
        return total
