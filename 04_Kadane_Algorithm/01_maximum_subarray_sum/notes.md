<h2><a href="https://leetcode.com/problems/maximum-subarray">53. Maximum Subarray</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Statement

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

A **subarray** is a **contiguous** part of an array.

### Constraints:
*   $1 \le \text{nums.length} \le 10^5$
*   $-10^4 \le \text{nums}[i] \le 10^4$

---

## Intuition

To find the maximum sum of a contiguous subarray, we need to explore how subarray sums are formed and how we can optimize this search.

### Why Brute Force is $O(n^2)$

A naive brute-force approach would examine every possible contiguous subarray. 
1. We choose a starting index $i$ ($0 \le i < n$).
2. We choose an ending index $j$ ($i \le j < n$).
3. We calculate the sum of the subarray from $i$ to $j$. 

Even if we optimize the sum calculation using a running sum (to avoid the inner $O(n)$ loop for summation), we still have to explore all pairs of $(i, j)$. For an array of size $n$, there are:
$$\frac{n(n + 1)}{2} \approx O(n^2) \text{ subarrays}$$

For $n = 10^5$, an $O(n^2)$ solution requires $\approx 10^{10}$ operations, which will lead to a **Time Limit Exceeded (TLE)** error.

### Key Observation behind Kadane's Algorithm

Kadane's Algorithm leverages dynamic programming to reduce the time complexity from $O(n^2)$ to $O(n)$ by keeping track of the local optimal choice.

Instead of looking at all possible subarrays from scratch, we ask ourselves a simple question at each index $i$:
> What is the maximum sum of a subarray that **must end** at index $i$?

If we know the maximum subarray sum ending at index $i - 1$, we can easily find the maximum subarray sum ending at index $i$.

### Why a Negative Running Sum Should be Discarded

Suppose we are at index $i$ and we have the maximum sum of the subarray ending at $i - 1$, let's call it $\text{currentSum}_{i-1}$. 

* If $\text{currentSum}_{i-1} > 0$, it is **positive**. Extending this subarray to include `nums[i]` will increase the overall sum compared to starting a new subarray from `nums[i]` alone.
* If $\text{currentSum}_{i-1} < 0$, it is **negative**. Adding a negative value to `nums[i]` will only make the sum smaller. For example, if we have a running sum of $-2$ and the current element is $4$, extending the previous subarray gives us $-2 + 4 = 2$. However, starting a new subarray from $4$ gives us $4$. Because $4 > 2$, it is always better to discard the negative running sum and start fresh.

> [!IMPORTANT]
> A negative running sum acts as a "burden." Discarding it (resetting it to 0 or restarting the subarray) is always more optimal than carrying it forward.

### "Start New Subarray vs Extend Current Subarray"

At each element `nums[i]`, we make a local decision:
1. **Extend the current subarray** to include the current element: `currentSum + nums[i]`
2. **Start a new subarray** starting exactly at the current element: `nums[i]`

We choose the path that yields the larger sum:
$$\text{currentSum}_i = \max(\text{nums}[i], \text{currentSum}_{i-1} + \text{nums}[i])$$

---

## Approach (Kadane's Algorithm)

The algorithm maintains two variables as it traverses the array:

1. **`currentSum`**: The maximum sum of a subarray ending at the current index. At each step, it represents the decision:
   $$\text{currentSum} = \max(\text{nums}[i], \text{currentSum} + \text{nums}[i])$$
2. **`bestSum`**: The maximum sum seen so far across all subarrays evaluated. It keeps track of the global maximum:
   $$\text{bestSum} = \max(\text{bestSum}, \text{currentSum})$$

### Variable Details:
* `currentSum` starts at `nums[0]`.
* `bestSum` starts at `nums[0]`.
* We iterate from index `1` to `n - 1`. At each index, we update `currentSum` and then update `bestSum` if `currentSum` exceeds the previous `bestSum`.

---

## Dry Run

Let's trace the algorithm with the input array: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

### Initialization:
* `currentSum = nums[0] = -2`
* `bestSum = nums[0] = -2`

### Iteration Table:

| Index | Element | Decision: `max(nums[i], currentSum + nums[i])` | Updated `currentSum` | `bestSum` Update: `max(bestSum, currentSum)` | Updated `bestSum` | Action / Explanation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | - | `-2` | - | `-2` | Initialize both variables with the first element `nums[0]`. |
| **1** | `1` | `max(1, -2 + 1) = max(1, -1)` | `1` | `max(-2, 1)` | `1` | Discard previous negative sum `-2`. Start new subarray at `1`. Update `bestSum`. |
| **2** | `-3` | `max(-3, 1 + -3) = max(-3, -2)` | `-2` | `max(1, -2)` | `1` | Extend current subarray. `bestSum` remains `1`. |
| **3** | `4` | `max(4, -2 + 4) = max(4, 2)` | `4` | `max(1, 4)` | `4` | Discard negative running sum `-2`. Start new subarray at `4`. Update `bestSum`. |
| **4** | `-1` | `max(-1, 4 + -1) = max(-1, 3)` | `3` | `max(4, 3)` | `4` | Extend subarray. `bestSum` remains `4`. |
| **5** | `2` | `max(2, 3 + 2) = max(2, 5)` | `5` | `max(4, 5)` | `5` | Extend subarray. Update `bestSum` to `5`. |
| **6** | `1` | `max(1, 5 + 1) = max(1, 6)` | `6` | `max(5, 6)` | `6` | Extend subarray. Update `bestSum` to `6` (the maximum subarray is `[4, -1, 2, 1]`). |
| **7** | `-5` | `max(-5, 6 + -5) = max(-5, 1)` | `1` | `max(6, 1)` | `6` | Extend subarray. `bestSum` remains `6`. |
| **8** | `4` | `max(4, 1 + 4) = max(4, 5)` | `5` | `max(6, 5)` | `6` | Extend subarray. `bestSum` remains `6`. |

**Final Output**: `6`

---

## C++ Implementation

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Initialize currentSum and bestSum with the first element
        int currentSum = nums[0];
        int bestSum = nums[0];

        // Iterate through the array starting from the second element
        for (size_t i = 1; i < nums.size(); ++i) {
            // Decide whether to start a new subarray or extend the existing one
            currentSum = std::max(nums[i], currentSum + nums[i]);
            // Update the global maximum sum found so far
            bestSum = std::max(bestSum, currentSum);
        }

        return bestSum;
    }
};
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We perform a single traversal of the input array of size $n$. At each step, we perform constant-time $O(1)$ operations (addition, comparison, assignment). |
| **Space Complexity** | $O(1)$ | We only use a constant amount of extra space to store the two state variables (`currentSum` and `bestSum`). |

---

## Pattern Recognition

Look for these clues in the problem description to identify if Kadane's Algorithm is applicable:

*   **Maximum sum contiguous subarray**: The problem specifically asks for a contiguous segment or subarray with the maximum sum.
*   **Best subarray ending at current index**: The solution structure depends on finding the best local choice ending at the current element to build the global choice.
*   **Contiguous segment optimization**: The elements can be positive or negative, and we need to locate an optimal contiguous boundary.
*   **Need $O(n)$ instead of $O(n^2)$**: The array size constraints are typically large (e.g., $n \ge 10^5$), preventing brute-force nested loops.

---

## Key Takeaways

*   **Dynamic Programming in Place**: Kadane's Algorithm is a dynamic programming approach that only requires remembering the result of the immediate previous subproblem (`currentSum`), allowing us to optimize space to $O(1)$.
*   **No Burden Carrying**: A cumulative sum that falls below zero will only reduce the potential sum of any future subarray. Hence, we reset/discard the running sum when it becomes negative.
*   **Local vs. Global**: By solving the local optimization problem (what is the best sum ending here?) at every index, we can determine the global maximum sum in a single linear pass.
