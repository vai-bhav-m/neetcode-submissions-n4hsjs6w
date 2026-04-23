class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum, post_sum = [1]*len(nums), [1]*len(nums)
        i = 1
        while i < len(nums):
            pre_sum[i] = nums[i-1] * pre_sum[i-1]
            post_sum[len(nums)-1-i] = nums[len(nums)-i] * post_sum[len(nums)-i]
            i += 1
        return [pre_sum[i]*post_sum[i] for i in range(len(nums))]
