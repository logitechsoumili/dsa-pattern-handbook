<h2><a href="https://www.geeksforgeeks.org/problems/smallest-sum-contiguous-subarray/1">Smallest Sum Contiguous Subarray</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Statement

Given an array `a` of `N` integers, find the contiguous subarray (containing at least one number) which has the minimum sum and return *its sum*.

A **subarray** is a **contiguous** part of an array.

### Constraints:
*   $1 \le a.\text{length} \le 10^5$
*   $-10^4 \le a[i] \le 10^4$

---

## Intuition

To find the minimum sum of a contiguous subarray, we can adapt the concepts from Maximum Subarray (Kadane's Algorithm) but invert the logic to focus on minimization.

### Why Brute Force is $O(n^2)$

A naive brute-force approach would examine every possible contiguous subarray. 
1. We choose a starting index $i$ ($0 \le i < n$).
2. We choose an ending index $j$ ($i \le j < n$).
3. We calculate the sum of the subarray from $i$ to $j$. 

This requires exploring all pairs of $(i, j)$. For an array of size $n$, there are:
$$\frac{n(n + 1)}{2} \approx O(n^2) \text{ subarrays}$$

For $n = 10^5$, an $O(n^2)$ solution requires $\approx 10^{10}$ operations, which will lead to a **Time Limit Exceeded (TLE)** error.

### Key Observation behind Kadane's Algorithm (Minimization)

Just like the maximum subarray problem, instead of looking at all possible subarrays from scratch, we ask ourselves a simple question at each index $i$:
> What is the minimum sum of a subarray that **must end** at index $i$?

If we know the minimum subarray sum ending at index $i - 1$ ($\text{currentSum}_{i-1}$), we can determine the optimal decision at index $i$.

### Why a Positive Running Sum Should be Discarded

Suppose we are at index $i$ and we have the minimum sum of the subarray ending at $i - 1$, let's call it $\text{currentSum}_{i-1}$. 

* If $\text{currentSum}_{i-1} < 0$, it is **negative**. Extending this subarray to include `a[i]` will decrease the overall sum compared to starting a new subarray from `a[i]` alone.
* If $\text{currentSum}_{i-1} > 0$, it is **positive**. Adding a positive value to `a[i]` will only make the sum larger. For example, if we have a running sum of $3$ and the current element is $-4$, extending the previous subarray gives us $3 + (-4) = -1$. However, starting a new subarray from $-4$ gives us $-4$. Because $-4 < -1$, it is always better to discard the positive running sum and start fresh.

> [!IMPORTANT]
> A positive running sum acts as a "burden" when we are trying to find the minimum sum. Discarding it (resetting it to 0 or restarting the subarray) is always more optimal than carrying it forward.

### "Start New Subarray vs Extend Current Subarray"

At each element `a[i]`, we make a local decision:
1. **Extend the current subarray** to include the current element: `currentSum + a[i]`
2. **Start a new subarray** starting exactly at the current element: `a[i]`

We choose the path that yields the smaller (more negative) sum:
$$\text{currentSum}_i = \min(\text{a}[i], \text{currentSum}_{i-1} + \text{a}[i])$$

---

## Approach (Kadane's Algorithm)

The algorithm maintains two variables as it traverses the array:

1. **`currentSum`**: The minimum sum of a subarray ending at the current index. At each step, it represents the decision:
   $$\text{currentSum} = \min(\text{a}[i], \text{currentSum} + \text{a}[i])$$
2. **`bestSum`**: The minimum sum seen so far across all subarrays evaluated. It keeps track of the global minimum:
   $$\text{bestSum} = \min(\text{bestSum}, \text{currentSum})$$

### Variable Details:
* `currentSum` starts at `a[0]`.
* `bestSum` starts at `a[0]`.
* We iterate from index `1` to `n - 1`. At each index, we update `currentSum` and then update `bestSum` if `currentSum` is smaller than the previous `bestSum`.

---

## Dry Run

Let's trace the algorithm with the input array: `a = [3, -4, 2, -3, -1, 7, -5]`

### Initialization:
* `currentSum = a[0] = 3`
* `bestSum = a[0] = 3`

### Iteration Table:

| Index | Element | Decision: `min(a[i], currentSum + a[i])` | Updated `currentSum` | `bestSum` Update: `min(bestSum, currentSum)` | Updated `bestSum` | Action / Explanation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | - | `3` | - | `3` | Initialize both variables with the first element `a[0]`. |
| **1** | `-4` | `min(-4, 3 + -4) = min(-4, -1)` | `-4` | `min(3, -4)` | `-4` | Discard previous positive sum `3`. Start new subarray at `-4`. Update `bestSum`. |
| **2** | `2` | `min(2, -4 + 2) = min(2, -2)` | `-2` | `min(-4, -2)` | `-4` | Extend current subarray. `bestSum` remains `-4`. |
| **3** | `-3` | `min(-3, -2 + -3) = min(-3, -5)` | `-5` | `min(-4, -5)` | `-5` | Extend current subarray. Update `bestSum` to `-5`. |
| **4** | `-1` | `min(-1, -5 + -1) = min(-1, -6)` | `-6` | `min(-5, -6)` | `-6` | Extend current subarray. Update `bestSum` to `-6` (minimum subarray is `[-4, 2, -3, -1]`). |
| **5** | `7` | `min(7, -6 + 7) = min(7, 1)` | `1` | `min(-6, 1)` | `-6` | Extend current subarray. `bestSum` remains `-6`. |
| **6** | `-5` | `min(-5, 1 + -5) = min(-5, -4)` | `-5` | `min(-6, -5)` | `-6` | Extend current subarray. `bestSum` remains `-6`. |

**Final Output**: `-6`

---

## C++ Implementation

```cpp
class Solution {
  public:
    int smallestSumSubarray(vector<int>& a) {
        // Initialize currentSum and bestSum with the first element
        int currentSum = a[0];
        int bestSum = a[0];
        
        // Iterate through the array starting from the second element
        for (size_t i = 1; i < a.size(); ++i) {
            // Decide whether to start a new subarray or extend the existing one
            currentSum = std::min(a[i], currentSum + a[i]);
            // Update the global minimum sum found so far
            bestSum = std::min(bestSum, currentSum);
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

*   **Minimum sum contiguous subarray**: The problem specifically asks for a contiguous segment or subarray with the minimum sum.
*   **Best subarray ending at current index**: The solution structure depends on finding the best local choice ending at the current element to build the global choice.
*   **Contiguous segment optimization**: The elements can be positive or negative, and we need to locate an optimal contiguous boundary.
*   **Need $O(n)$ instead of $O(n^2)$**: The array size constraints are typically large (e.g., $n \ge 10^5$), preventing brute-force nested loops.

---

## Key Takeaways

*   **Minimization Adaptation**: Adapting Kadane's Algorithm from maximum subarray to minimum subarray only requires switching the optimization functions from `max` to `min`.
*   **Discarding Positives**: A cumulative sum that rises above zero will only increase the potential sum of any future subarray. Hence, we reset/discard the running sum when it becomes positive.
*   **Local vs. Global**: By solving the local optimization problem (what is the best sum ending here?) at every index, we can determine the global minimum sum in a single linear pass.
