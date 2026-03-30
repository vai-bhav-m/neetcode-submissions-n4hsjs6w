class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol_dict = dict()
        for i, n in enumerate(nums):
            if target - n in sol_dict:
                return [sol_dict[target-n], i]
            sol_dict[n] = i
            
            