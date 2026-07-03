class Solution {
  public:
    int smallestSumSubarray(vector<int>& a) {
        int currentSum = a[0];
        int bestSum = a[0];
        
        for (int i = 1; i < a.size(); i++){
            currentSum = min(a[i], currentSum + a[i]);
            bestSum = min(bestSum, currentSum);
        }
        
        return bestSum;
    }
};
