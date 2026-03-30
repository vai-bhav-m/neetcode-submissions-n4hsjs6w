import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)
        for x in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, x)
            elif x > self.heap[0]:  
                heapq.heapreplace(self.heap, x)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val) 
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
