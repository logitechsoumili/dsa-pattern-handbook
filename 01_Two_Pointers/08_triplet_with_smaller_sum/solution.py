# Triplets with Smaller Sum
# Find count of triplets (i, j, k) with i < j < k such that arr[i] + arr[j] + arr[k] < sum

class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        ans = 0

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total >= sum:
                    right -= 1
                else:
                    ans = ans + (right - left)
                    left += 1

        return ans