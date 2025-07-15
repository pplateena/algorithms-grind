from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        l = len(piles)
        answer = right
        if l == h:
            return max(piles)

        while left <= right:
            mid = (left + right) // 2  # How much to eat
            i, hrs_spent = 0, 0

            while i < l and hrs_spent <= h:
                hrs_spent += ceil(piles[i] / mid)
                i += 1

            if hrs_spent <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer