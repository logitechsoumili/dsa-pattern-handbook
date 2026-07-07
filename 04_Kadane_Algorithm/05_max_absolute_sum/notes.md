<h2><a href="https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray">1749. Maximum Absolute Sum of Any Subarray</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Statement

You are given an integer array `nums`. The **absolute sum** of a subarray $[nums_l, nums_{l+1}, \dots, nums_{r-1}, nums_r]$ is $\left| nums_l + nums_{l+1} + \dots + nums_{r-1} + nums_r \right|$.

Return the **maximum absolute sum** of any (possibly empty) subarray of `nums`.

Note: The absolute sum of an empty subarray is $0$.

### Constraints:
*   $1 \le \text{nums.length} \le 10^5$
*   $-10^4 \le \text{nums}[i] \le 10^4$

---

## Intuition

The maximum absolute sum of a subarray can come from either:
1.  A highly positive subarray sum (maximized using standard Kadane's algorithm).
2.  A highly negative subarray sum (minimized using min-Kadane's algorithm), whose absolute value is very large.

Thus, we can track both the **maximum subarray sum** and the **minimum subarray sum** ending at each index in a single pass. The answer will be the maximum of the absolute values of these two sums.

### Alternative Intuition (Prefix Sums)

An elegant alternative way to think about this problem uses prefix sums:
Let $S_i = \sum_{j=0}^{i} \text{nums}[j]$ be the prefix sum up to index $i$, with $S_{-1} = 0$.
The sum of any subarray from index $l$ to $r$ is:
$$\text{Sum}(l, r) = S_r - S_{l-1}$$

To maximize the absolute value $|S_r - S_{l-1}|$, we simply need to find the difference between the absolute maximum prefix sum and the absolute minimum prefix sum (including $S_{-1} = 0$):
$$\max |S_r - S_{l-1}| = \max(S) - \min(S)$$

While both approaches have $O(n)$ time and $O(1)$ space complexity, the Kadane-based approach is implemented here.

---

## Approach (Simultaneous Max and Min Kadane's)

1.  Initialize three variables:
    *   `maxSum = nums[0]`: Tracks the maximum subarray sum ending at the current index.
    *   `minSum = nums[0]`: Tracks the minimum subarray sum ending at the current index.
    *   `ans = abs(nums[0])`: Tracks the maximum absolute sum found so far.
2.  Iterate through the array starting from index `1` to `n - 1`.
3.  For each element `nums[i]`:
    *   Update `maxSum` using the standard Kadane's transition: `maxSum = max(nums[i], maxSum + nums[i])`.
    *   Update `minSum` using the min-Kadane's transition: `minSum = min(nums[i], minSum + nums[i])`.
    *   Update `ans` with the maximum absolute value found so far: `ans = max(ans, max(abs(minSum), abs(maxSum)))`.
4.  Return `ans`.

---

## Dry Run

Let's trace the algorithm with the input array: `nums = [2, -5, 1, -4, 3]`

### Initialization:
*   `maxSum = 2`
*   `minSum = 2`
*   `ans = 2`

### Iteration Table:

| Index | Element | `maxSum` Update: `max(nums[i], maxSum + nums[i])` | Updated `maxSum` | `minSum` Update: `min(nums[i], minSum + nums[i])` | Updated `minSum` | `ans` Update: `max(ans, abs(maxSum), abs(minSum))` | Updated `ans` | Action / Explanation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | - | `2` | - | `2` | - | `2` | Initialize variables. |
| **1** | `-5` | `max(-5, 2 + -5)` | `-3` | `min(-5, 2 + -5)` | `-5` | `max(2, 3, 5)` | `5` | `minSum` drops to `-5`. `ans` becomes `5`. |
| **2** | `1` | `max(1, -3 + 1)` | `1` | `min(1, -5 + 1)` | `-4` | `max(5, 1, 4)` | `5` | Extend both subarrays. |
| **3** | `-4` | `max(-4, 1 + -4)` | `-3` | `min(-4, -4 + -4)` | `-8` | `max(5, 3, 8)` | `8` | `minSum` drops to `-8` (subarray `[-5, 1, -4]`). `ans` becomes `8`. |
| **4** | `3` | `max(3, -3 + 3)` | `3` | `min(3, -8 + 3)` | `-5` | `max(8, 3, 5)` | `8` | Extend subarray. `ans` remains `8`. |

**Final Output**: `8`

---

## C++ Implementation

```cpp
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
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We perform a single traversal of the input array. At each element, we do constant number of additions and comparisons. |
| **Space Complexity** | $O(1)$ | Only a few state variables are used, which uses a constant amount of memory. |

---

## Pattern Recognition

Look for these clues in the problem description to identify if this simultaneous Kadane's optimization is applicable:
*   **Absolute sum of contiguous subarrays**: The absolute value function $|x|$ means we care about both extremely positive and extremely negative values.
*   **Contiguous subsegment optimization**: Need to locate an optimal contiguous range where the values are either highly concentrated in one sign or prefix sums have a large range.

---

## Key Takeaways

*   **Symmetry in Kadane**: Kadane's algorithm is easily symmetric. To track minimums instead of maximums, simply swap `max` with `min`.
*   **Simultaneous Tracking**: Tracking multiple properties (both min and max) in a single pass is highly efficient and keeps the time complexity at $O(n)$ and space complexity at $O(1)$.
*   **Prefix Sum Difference**: The maximum absolute subarray sum is also equivalent to $\max(\text{prefix sum}) - \min(\text{prefix sum})$.
