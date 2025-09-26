You are given a deque dq (double-ended queue) containing non-negative integers, along with two positive integer type and k. The task is to rotate the deque circularly by k positions.
There are two types of rotation operations:
Right Rotation (Clockwise): If type = 1, rotate the deque to the right. This means moving the last element to the front, and repeating the process k times.
Left Rotation (Anti-Clockwise): If type = 2, rotate the deque to the left. This means moving the first element to the back, and repeating the process k times.
from collections import deque

def rotate_deque(dq, type, k):
    # Normalize k to avoid unnecessary full rotations
    k = k % len(dq) if dq else 0

    if type == 1:
        # Right rotation
        dq.rotate(k)
    elif type == 2:
        # Left rotation
        dq.rotate(-k)
    else:
        raise ValueError("Invalid rotation type. Use 1 for right or 2 for left.")

    return dq
