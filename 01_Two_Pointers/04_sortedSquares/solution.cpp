class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size());
        int pos = nums.size() - 1;
        int left = 0, right = nums.size() - 1;

        while (left <= right){
            int a = nums[left] * nums[left];
            int b = nums[right] * nums[right];

            if (a > b){
                res[pos--] = a;
                left++;
            }
            else{
                res[pos--] = b;
                right--;
            }
        }

        return res;
    }
};