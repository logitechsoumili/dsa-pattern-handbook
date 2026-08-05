class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currentSum = 0
        freq = {0:1}
        count, rem = 0, 0

        for i in range(len(nums)):
            currentSum += nums[i]
            rem = currentSum % k
            count += freq.get(rem, 0)
            freq[rem] = freq.get(rem, 0) + 1

        return count