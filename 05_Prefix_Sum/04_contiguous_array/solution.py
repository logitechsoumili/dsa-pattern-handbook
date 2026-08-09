class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance, res = 0, 0
        count = {0 : -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                balance -= 1
            else:
                balance += 1

            if balance in count:
                length = i - count[balance]
                res = max(res, length)
            else:
                count[balance] = i

        return res