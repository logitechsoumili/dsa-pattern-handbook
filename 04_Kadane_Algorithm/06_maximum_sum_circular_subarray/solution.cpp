class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int totalSum = nums[0];

        int maxEnding = nums[0];
        int maxSub = nums[0];

        int minEnding = nums[0];
        int minSub = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            totalSum += nums[i];

            // Maximum subarray Kadane
            maxEnding = max(nums[i], maxEnding + nums[i]);
            maxSub = max(maxSub, maxEnding);

            // Minimum subarray Kadane
            minEnding = min(nums[i], minEnding + nums[i]);
            minSub = min(minSub, minEnding);
        }

        // All elements negative
        if (minSub == totalSum)
            return maxSub;

        return max(maxSub, totalSum - minSub);
    }
};