class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentSum = nums[0];
        int bestSum = nums[0];

        for (int i = 1; i < nums.size(); i++){
            currentSum = max(nums[i], currentSum + nums[i]);
            bestSum = max(bestSum, currentSum);
        }
        return bestSum;
    }
};