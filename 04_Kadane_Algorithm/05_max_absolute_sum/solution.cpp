class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int maxSum = nums[0];
        int minSum = nums[0];
        int ans = abs(nums[0]);

        for (int i = 1; i < nums.size(); i++){
            maxSum = max(nums[i], maxSum + nums[i]);
            minSum = min(nums[i], minSum + nums[i]);
            ans = max(ans, max(abs(minSum), abs(maxSum)));
        }

        return ans;
    }
};