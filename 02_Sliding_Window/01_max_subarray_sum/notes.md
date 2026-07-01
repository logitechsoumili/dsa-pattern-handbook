<h2><a href="https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1">Max Sum Subarray of Size K</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## Problem Summary

Given an array of integers `arr` and a number `k`, return the maximum sum of any contiguous subarray of size `k`.

## Brute Force Approach

Iterate through the array and generate all possible subarrays of size `k`. For each subarray, calculate the sum of its elements using a nested loop, and track the maximum sum.

```python
def maxSubarraySum_bruteforce(arr, k):
    max_sum = 0
    for i in range(len(arr) - k + 1):
        curr_sum = 0
        for j in range(i, i + k):
            curr_sum += arr[j]
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

```cpp
int maxSubarraySum_bruteforce(vector<int>& arr, int k) {
    int maxSum = 0;
    for (int i = 0; i <= (int)arr.size() - k; i++) {
        int currSum = 0;
        for (int j = i; j < i + k; j++) {
            currSum += arr[j];
        }
        maxSum = max(maxSum, currSum);
    }
    return maxSum;
}
```

- Time Complexity: O(n * k) because we compute the sum of `k` elements for each of the `n - k + 1` window positions.
- Space Complexity: O(1)

## Optimized Approach

Use a fixed-size sliding window of size `k`. First, calculate the sum of the first `k` elements. Then, slide the window from index `k` to the end of the array. In each step, compute the new window sum in O(1) time by adding the incoming element (`arr[i]`) and subtracting the outgoing element (`arr[i - k]`). Track the maximum sum encountered.

```python
class Solution:
    def maxSubarraySum(self, arr, k):
        if len(arr) < k:
            return 0

        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum
```

```cpp
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
```

- Key idea: Reuse the sum of the overlapping elements between adjacent windows.
- Why it works: Moving the window one position to the right changes the window elements by exactly one incoming and one outgoing element, meaning we can update the sum incrementally without recomputing it.

## Pattern Recognition

This problem is the classic entry-level example of the Fixed-Size Sliding Window pattern. The subarray length is fixed at `k`, and we are searching for an optimal contiguous subarray sum.

## Key Observation

The difference between the sums of two adjacent windows is solely determined by the incoming element at the right edge and the outgoing element at the left edge.
`New Sum = Old Sum + Incoming - Outgoing`

## Complexity Analysis

### Time Complexity

O(n) because we slide the window across the array, performing constant-time O(1) additions and subtractions at each step.

### Space Complexity

O(1) auxiliary space since we only store variables for the sums and pointers.

## Common Mistakes

- Recalculating the sum of each window from scratch, resulting in an O(n * k) solution.
- Forgetting to subtract the outgoing element `arr[i - k]`.
- Forgetting to initialize the maximum sum with the sum of the first window.
- Using nested loops that degrade performance to quadratic-like behavior.

## Interview Notes

This problem evaluates a candidate's transition from a naive O(n * k) solution to an optimal O(n) sliding window approach. It is a fundamental benchmark for sliding window questions.
