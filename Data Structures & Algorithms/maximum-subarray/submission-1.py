class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        curr_max, glo_max = nums[0], nums[0]
        for n in nums[1:]:
            curr_max = max(n, n + curr_max)
            glo_max = max(curr_max, glo_max)
        return glo_max