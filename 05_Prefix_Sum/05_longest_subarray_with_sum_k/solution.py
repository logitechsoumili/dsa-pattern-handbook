class Solution:
    def longestSubarray(self, arr, k):
        freq = {0:-1}
        currentSum, res = 0, 0
        
        for i in range(len(arr)):
            currentSum += arr[i]
            find = currentSum - k
            
            if find in freq:
                length = i - freq[find]
                res = max(res, length)
            
            if currentSum not in freq:
                freq[currentSum] = i
                
        return res