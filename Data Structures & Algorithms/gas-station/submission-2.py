class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(delta) < 0:
            return -1
        trailing_ptr, total = 0, 0
        for i, x in enumerate(delta):
            total += x
            if total < 0:
                trailing_ptr = i+1
                total = 0
        return trailing_ptr

        
