# LeetCode 283: Move Zeroes
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        curr = 0  # position where next non-zero should be placed

        for nxt in range(len(nums)):
            if nums[nxt] != 0:
                nums[curr], nums[nxt] = nums[nxt], nums[curr]
                curr += 1