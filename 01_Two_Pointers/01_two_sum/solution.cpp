class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;

        while (left < right){
            int res = numbers[left] + numbers[right];
            if (res == target){
                return {left+1, right+1};
            }
            else if (res < target){
                left++;
            }
            else{
                right--;
            }
        }
        return {0,0};
    }
};