class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1, p2 = 0, len(numbers)-1
        while True:
            if numbers[p1]+numbers[p2] < target: p1 += 1
            elif numbers[p1]+numbers[p2] > target: p2 -= 1
            else: return [p1+1, p2+1]