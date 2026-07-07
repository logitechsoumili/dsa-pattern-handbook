# Kadane's Algorithm Pattern

## Overview

Kadane's Algorithm is a dynamic programming technique used to find the maximum (or minimum) sum of a contiguous subarray in linear time $O(n)$ and constant space $O(1)$. Instead of calculating the sum of every possible subarray from scratch, Kadane's algorithm iterates through the array and determines the optimal subarray ending at each position. By leveraging local decisions, it avoids redundant calculations and solves optimization problems efficiently.

## Recognition Signals

Consider using Kadane's Algorithm or its variations when:
*   You need to find a **contiguous subarray** that maximizes or minimizes a cumulative metric (such as sum or product).
*   The array contains both positive and negative values (if all values are positive, the entire array is always the maximum sum subarray).
*   The optimal decision ending at index $i$ depends directly on the optimal decision ending at index $i - 1$.
*   Constraints require an $O(n)$ time complexity (typically $n \ge 10^5$), preventing brute-force nested loop solutions.

## Core Concepts

*   **Local vs. Global Optimality:** At each index $i$, the algorithm computes the maximum subarray sum ending *exactly* at $i$ (the local optimum, `currentSum`). The overall maximum subarray sum seen across the entire array is updated accordingly (the global optimum, `bestSum`).
*   **"Start New Subarray vs. Extend Subarray":** The core transition at index $i$ represents a choice:
    1.  Extend the active subarray to include the current element: `currentSum + nums[i]`
    2.  Discard the previous subarray and start a new one beginning at the current element: `nums[i]`
*   **Discarding Negative Running Sums (Burdens):** Since our goal is maximization, a negative running sum acts as a burden. If `currentSum` drops below $0$, starting a new subarray from the next element will always be more optimal than carrying forward the negative sum.
*   **Complement / Inversion Logic (Circular Arrays):** For wrapping or circular structures, the maximum circular subarray sum is equal to the total array sum minus the minimum subarray sum: `totalSum - minSub`.
*   **Multi-State Tracking:** In more complex variations (such as product-based optimization or allowed deletions), we track multiple states per index (e.g., tracking both `maxEnding` and `minEnding` to handle sign flips, or tracking `noDel` and `oneDel` to handle element deletion).

---

## Template

### Standard Maximum Subarray Sum

```python
def max_subarray_sum_template(nums):
    # Initialize trackers with the first element
    current_sum = nums[0]
    best_sum = nums[0]
    
    # Iterate starting from the second element
    for i in range(1, len(nums)):
        # Decide: Start new subarray or extend current subarray
        current_sum = max(nums[i], current_sum + nums[i])
        # Update the global maximum
        best_sum = max(best_sum, current_sum)
        
    return best_sum
```

```cpp
int maxSubArrayTemplate(const vector<int>& nums) {
    // Initialize trackers with the first element
    int currentSum = nums[0];
    int bestSum = nums[0];
    
    // Iterate starting from the second element
    for (size_t i = 1; i < nums.size(); ++i) {
        // Decide: Start new subarray or extend current subarray
        currentSum = std::max(nums[i], currentSum + nums[i]);
        // Update the global maximum
        bestSum = std::max(bestSum, currentSum);
    }
    
    return bestSum;
}
```

### Standard Minimum Subarray Sum

```python
def min_subarray_sum_template(nums):
    current_sum = nums[0]
    best_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Decide: Start new subarray or extend current subarray (focused on minimization)
        current_sum = min(nums[i], current_sum + nums[i])
        best_sum = min(best_sum, current_sum)
        
    return best_sum
```

```cpp
int minSubArrayTemplate(const vector<int>& nums) {
    int currentSum = nums[0];
    int bestSum = nums[0];
    
    for (size_t i = 1; i < nums.size(); ++i) {
        currentSum = std::min(nums[i], currentSum + nums[i]);
        bestSum = std::min(bestSum, currentSum);
    }
    
    return bestSum;
}
```

---

## Common Variations

*   **Minimum Subarray Sum:** Solved by replacing the `max()` transition function with `min()`.
*   **Maximum Product Subarray:** Negative numbers flip the sign of products. We must maintain both `maxEnding` (most positive) and `minEnding` (most negative) and swap them whenever the current element is negative.
*   **Subarray with at most One Deletion:** Introduce a secondary state `oneDel` representing the maximum sum with exactly one deletion, which transitions using the previous no-deletion sum (`noDel_prev`) or by extending an already deleted sequence (`oneDel_prev + nums[i]`).
*   **Maximum Absolute Sum of Any Subarray:** Run both max-Kadane and min-Kadane simultaneously, taking the maximum of their absolute values at each index.
*   **Maximum Sum Circular Subarray:** Analyze the non-circular case (`maxSub`) and the circular case (`totalSum - minSub`). Take the maximum of both while checking for the edge case where all elements are negative.

---

## Complexity Characteristics

*   **Time Complexity:** Typically $O(n)$ as we visit each element exactly once and execute $O(1)$ arithmetic operations/comparisons.
*   **Space Complexity:** Typically $O(1)$ since we only store a few primitive tracking variables to preserve state from the previous step.

---

## Problems Solved

| # | Problem | Key Lesson |
| - | ------- | ---------- |
| 1 | [Maximum Subarray](./01_maximum_subarray_sum) ([Notes](./01_maximum_subarray_sum/notes.md)) | Classic Kadane's algorithm. Negative running sums are discarded as they reduce future subarray sums. |
| 2 | [Smallest Sum Contiguous Subarray](./02_minimum_subarray_sum) ([Notes](./02_minimum_subarray_sum/notes.md)) | Minimization adaptation of Kadane's. Positive running sums are discarded. |
| 3 | [Maximum Product Subarray](./03_maximum_product_subarray) ([Notes](./03_maximum_product_subarray/notes.md)) | Tracks both max and min products ending at each index to handle sign flips caused by negative numbers. |
| 4 | [Maximum Subarray Sum with One Deletion](./04_maxSub_one_deletion) ([Notes](./04_maxSub_one_deletion/notes.md)) | Multi-state DP where the decision to delete or keep an element branches into two separate states. |
| 5 | [Maximum Absolute Sum of Any Subarray](./05_max_absolute_sum) ([Notes](./05_max_absolute_sum/notes.md)) | Simultaneously tracks both max and min subarray sums, or can be solved via prefix sum difference: $\max(S) - \min(S)$. |
| 6 | [Maximum Sum Circular Subarray](./06_maximum_sum_circular_subarray) ([Notes](./06_maximum_sum_circular_subarray/notes.md)) | Combining max-Kadane and min-Kadane to resolve wrapping subarrays, while handling the all-negative edge case. |

---

## Common Mistakes

*   ❌ **Incorrect Tracker Initialization:** Initializing `currentSum` or `bestSum` to `0` instead of `nums[0]`. This fails when the array contains only negative numbers (e.g., `nums = [-3, -2, -4]`), where the correct answer is `-2` but the code returns `0`.
*   ❌ **Failing to Track Minimums in Product Subarrays:** Forgetting that two negative numbers multiply to form a positive number.
*   ❌ **All-Negative Circular Edge Case:** In circular subarrays, returning `totalSum - minSub` when all elements are negative. Since `totalSum == minSub`, this yields `0`, which represents an empty subarray. The algorithm must fall back to `maxSub`.
*   ❌ **Out of Order Updates:** When implementing multi-state DP (like the one-deletion variant), updating `noDel` before calculating `oneDel` will corrupt `oneDel`'s transition because it relies on the previous index's `noDel` value.

---

## Interview Takeaways

*   **Contiguous = Kadane:** When a question specifies contiguous elements (subarray) along with optimization (max/min), Kadane's algorithm should be your default pattern.
*   **Optimizing Dynamic Programming Space:** Kadane's is essentially a dynamic programming algorithm where we optimize the space from $O(n)$ (an array storing optimal solutions ending at all indices) to $O(1)$ by only keeping the immediate previous state.
*   **State Machine thinking:** For complex optimization constraints, treat them as states in a state machine (e.g., State 0: No Deletions, State 1: One Deletion) and write transition rules from $i-1$ to $i$ for each state.
