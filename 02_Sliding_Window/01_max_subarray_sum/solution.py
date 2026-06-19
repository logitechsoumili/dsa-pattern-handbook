# GeeksforGeeks: Max Sum Subarray of Size K
# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

class Solution:
    def maxSubarraySum(self, arr, k):
        if len(arr) < k:
            return 0

        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum