class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left = 0;
        int sum = accumulate(nums.begin(), nums.end(), 0);

        for (int i = 0; i < nums.size(); i++){
            int right = sum - nums[i] - left;

            if (left == right) return i;

            left += nums[i];
        }
        return -1;
    }
};