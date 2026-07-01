class Solution {
  public:
    int maxSubarraySum(vector<int>& arr, int k) {
        int left = 0, sum = 0;
        int maxSum = INT_MIN;
        
        for (int right = 0; right < arr.size(); right++){
            sum += arr[right];
            
            if ((right - left + 1) == k){
                maxSum = max(maxSum, sum);
                sum -= arr[left];
                left++;
            }
        }
        return maxSum;
    }
};