class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            sum_h = 0
            for x in piles:
                sum_h += x // mid
                if x % mid > 0:
                    sum_h += 1
            if sum_h > h:
                low = mid + 1
            else:
                high = mid
        return low