class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        # if nums[-1] < nums[-2]:
        #     return nums[-1]
        low, high = 0, len(nums)-1

        while True:
            mid = (low + high) // 2
            n1 = mid - 1 if mid > 0 else len(nums) - 1
            n2 = mid + 1 if mid <= len(nums)-1 else 0
            if 2*nums[mid] > nums[n1] + nums[n2]:
                return nums[n2]
            elif nums[mid] > nums[low]:
                low = mid + 1 
            else:
                high = mid
