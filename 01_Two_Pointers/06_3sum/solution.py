# LeetCode 15: 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res