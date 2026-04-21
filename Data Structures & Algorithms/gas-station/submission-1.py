class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(delta) < 0:
            return -1
        trailing_ptr, total = 0, 0
        for i, x in enumerate(delta):
            if total + x < 0:
                trailing_ptr = i+1
                total = 0
            else:
                total += x
        return trailing_ptr

        
