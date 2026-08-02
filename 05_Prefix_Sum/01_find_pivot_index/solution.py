class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        cal = sum(nums)
        for i in range(0, len(nums)):
            right = cal - left - nums[i]

            if left == right:
                return i

            left += nums[i]
            
        return -1