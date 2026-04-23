class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]: return nums[0]
        l, h = 0, len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        return nums[-1]