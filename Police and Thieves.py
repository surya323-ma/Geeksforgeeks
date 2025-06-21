Given an array arr[], where each element contains either a 'P' for policeman or a 'T' for thief. Find the maximum number of thieves that can be caught by the police. 
Keep in mind the following conditions :

Each policeman can catch only one thief.
A policeman cannot catch a thief who is more than k units away from him.
#code
class Solution:
    def catchThieves(self, arr, k):
        police = []
        thief = []
        caught = 0

        # Collect indices
        for idx, ch in enumerate(arr):
            if ch == 'P':
                police.append(idx)
            elif ch == 'T':
                thief.append(idx)

        i = j = 0
        # Use two-pointer strategy
        while i < len(police) and j < len(thief):
            if abs(police[i] - thief[j]) <= k:
                caught += 1
                i += 1
                j += 1
            elif police[i] < thief[j]:
                i += 1
            else:
                j += 1

        return caught
