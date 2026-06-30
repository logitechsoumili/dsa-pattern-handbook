class Solution {
  public:
    int countTriplets(int sum, vector<int>& arr) {
        sort(arr.begin(), arr.end());
        
        int count = 0;
        
        for (int i = 0; i < arr.size() - 2; i++){
            int left = i + 1;
            int right = arr.size() - 1;
            
            while (left < right){
                int currentSum = arr[i] + arr[left] + arr[right];
                
                if (currentSum < sum){
                    count += (right - left);
                    left++;
                }
                else right--;
            }
        }
        return count;
    }
};