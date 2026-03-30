import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stones = [-x for x in stones]
        heapq.heapify(max_stones)
        while len(max_stones) > 1:
            s1 = heapq.heappop(max_stones)
            s2 = heapq.heappop(max_stones)
            if abs(s1 - s2) > 0:
                heapq.heappush(max_stones,-abs(s1 - s2))
        if len(max_stones) == 1:
            return -max_stones[0]
        return 0