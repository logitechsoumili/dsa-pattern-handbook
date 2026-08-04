class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        freq = {0:1}
        count = 0

        for i in range(len(nums)):
            currentSum += nums[i]
            count += freq.get(currentSum - k, 0)
            freq[currentSum] = freq.get(currentSum, 0) + 1
            
        return count