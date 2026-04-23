class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def get_hours(piles, k):
            res = 0
            for x in piles:
                res += x // k
                if x % k: res += 1
            return res
        
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2
            n_h = get_hours(piles, mid)
            print(mid, n_h)
            if n_h > h:
                low = mid + 1
            else:
                high = mid
        return high