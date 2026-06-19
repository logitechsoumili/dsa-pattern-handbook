# LeetCode 16: 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        res_sum = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                d = abs(total - target)

                # Update answer if a closer sum is found
                if d < min_diff:
                    min_diff = d
                    res_sum = total

                # Exact match found
                if total == target:
                    return res_sum
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return res_sum