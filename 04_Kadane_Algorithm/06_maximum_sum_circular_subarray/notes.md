<h2><a href="https://leetcode.com/problems/maximum-sum-circular-subarray">918. Maximum Sum Circular Subarray</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Statement

Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`.

A **circular array** means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A subarray may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i+1], ..., nums[j]`, there does not exist `i <= k1, k2 <= j` with `k1 % n == k2 % n`.

### Constraints:
*   $n == \text{nums.length}$
*   $1 \le n \le 3 \times 10^4$
*   $-3 \times 10^4 \le \text{nums}[i] \le 3 \times 10^4$

---

## Intuition

A subarray in a circular array can be categorized into two cases:

### Case 1: The subarray does not wrap around (Non-Circular Subarray)
The maximum sum subarray lies entirely within the array boundaries without wrapping around. This is the standard maximum subarray sum problem, which can be solved directly using Kadane's algorithm.
Let's call this sum **`maxSub`**.

```
[  _ _ _ _ [max subarray] _ _ _ _  ]
```

### Case 2: The subarray wraps around (Circular Subarray)
The maximum sum subarray starts in the suffix of the array and wraps around to the prefix.
```
[ max suffix ] _ _ _ _ _ _ [ max prefix ]
```

Notice that the remaining part of the array that is **not** included in the circular subarray is a contiguous, non-empty middle subarray:
```
[ max suffix ] [ excluded middle ] [ max prefix ]
```

To maximize the sum of the circular subarray, we must **minimize** the sum of this excluded middle subarray.
$$\text{Max Circular Sum} = \text{Total Sum} - \text{Min Subarray Sum}$$
Let's call the minimum contiguous subarray sum **`minSub`**.

```
Max Circular Sum = totalSum - minSub
```

### The Edge Case (All Negative Elements)
If all elements in the array are negative:
*   `totalSum` will be equal to `minSub` (since the minimum subarray will include the entire array).
*   `totalSum - minSub` will evaluate to `0`.
*   However, since the subarray must be **non-empty**, a sum of `0` corresponds to an empty subarray (which is invalid).
*   In this scenario, the maximum subarray sum must be the single largest (least negative) element, which is already stored in `maxSub`.

Therefore:
*   If `minSub == totalSum`, return `maxSub`.
*   Otherwise, return $\max(\text{maxSub}, \text{totalSum} - \text{minSub})$.

---

## Approach

1.  Initialize variables with the first element:
    *   `totalSum = nums[0]`
    *   `maxEnding = nums[0]`, `maxSub = nums[0]` (for max Kadane's)
    *   `minEnding = nums[0]`, `minSub = nums[0]` (for min Kadane's)
2.  Iterate from index `1` to `n - 1`:
    *   Add `nums[i]` to `totalSum`.
    *   Update `maxEnding = max(nums[i], maxEnding + nums[i])` and `maxSub = max(maxSub, maxEnding)`.
    *   Update `minEnding = min(nums[i], minEnding + nums[i])` and `minSub = min(minSub, minEnding)`.
3.  After the loop, check if `minSub == totalSum`.
    *   If true, return `maxSub`.
    *   Otherwise, return `max(maxSub, totalSum - minSub)`.

---

## Dry Run

### Example 1: `nums = [5, -3, 5]`

#### Initialization:
*   `totalSum = 5`
*   `maxEnding = 5`, `maxSub = 5`
*   `minEnding = 5`, `minSub = 5`

#### Iteration Table:

| Index | Element | `totalSum` | `maxEnding` | `maxSub` Update | `minEnding` | `minSub` Update | Explanation / Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | `5` | `5` | `5` | `5` | `5` | Initialize variables. |
| **1** | `-3` | `2` | `max(-3, 5 + -3) = 2` | `max(5, 2) = 5` | `min(-3, 5 + -3) = -3` | `min(5, -3) = -3` | Extend both max and min subarrays. |
| **2** | `5` | `7` | `max(5, 2 + 5) = 7` | `max(5, 7) = 7` | `min(5, -3 + 5) = 2` | `min(-3, 2) = -3` | Max sum updated to 7. Min sum remains -3. |

*   `minSub` ($-3$) is not equal to `totalSum` ($7$).
*   Return `max(maxSub, totalSum - minSub) = max(7, 7 - (-3)) = max(7, 10) = 10`.
*   **Result**: `10` (from circular subarray `[5] + [5]`).

---

### Example 2: `nums = [-3, -2, -3]` (All Negatives)

#### Initialization:
*   `totalSum = -3`
*   `maxEnding = -3`, `maxSub = -3`
*   `minEnding = -3`, `minSub = -3`

#### Iteration Table:

| Index | Element | `totalSum` | `maxEnding` | `maxSub` Update | `minEnding` | `minSub` Update | Explanation / Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | `-3` | `-3` | `-3` | `-3` | `-3` | Initialize variables. |
| **1** | `-2` | `-5` | `max(-2, -3 + -2) = -2` | `max(-3, -2) = -2` | `min(-2, -3 + -2) = -5` | `min(-3, -5) = -5` | `maxSub` becomes `-2`. `minSub` becomes `-5`. |
| **2** | `-3` | `-8` | `max(-3, -2 + -3) = -3` | `max(-2, -3) = -2` | `min(-3, -5 + -3) = -8` | `min(-5, -8) = -8` | `minSub` equals the `totalSum` ($-8$). |

*   `minSub` ($-8$) is equal to `totalSum` ($-8$).
*   Return `maxSub = -2`.
*   **Result**: `-2` (subarray `[-2]`).

---

## C++ Implementation

```cpp
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int totalSum = nums[0];

        int maxEnding = nums[0];
        int maxSub = nums[0];

        int minEnding = nums[0];
        int minSub = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            totalSum += nums[i];

            // Maximum subarray Kadane
            maxEnding = max(nums[i], maxEnding + nums[i]);
            maxSub = max(maxSub, maxEnding);

            // Minimum subarray Kadane
            minEnding = min(nums[i], minEnding + nums[i]);
            minSub = min(minSub, minEnding);
        }

        // All elements negative
        if (minSub == totalSum)
            return maxSub;

        return max(maxSub, totalSum - minSub);
    }
};
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We perform a single traversal of the input array of size $n$, computing running maximums and minimums in $O(1)$ time per element. |
| **Space Complexity** | $O(1)$ | We only use a constant amount of extra space to store the running variables. |

---

## Pattern Recognition

Look for these clues to identify if this circular variation is applicable:
*   **Circular array structures**: The problem description mentions the array is circular or elements wrap around from the end to the start.
*   **Inversion strategy (Complementary thinking)**: Maximizing a wrapped array is mathematically equivalent to minimizing the non-wrapped middle subarray. This transition from maximizing to minimizing using the complement (Total Sum) is a common pattern in array and range query problems.

---

## Key Takeaways

*   **Complement Optimization**: A wrapping subarray can always be represented as the total array sum minus a non-wrapping middle subarray.
*   **Edge Case Detection**: Always check if the minimum subarray covers the entire array (i.e. `minSub == totalSum`), which happens when all elements are negative. This prevents returning an empty subarray (sum $0$).
*   **Single-Pass Efficiency**: Running both max-Kadane and min-Kadane together in a single loop allows us to keep the algorithm linear in time and constant in space.
