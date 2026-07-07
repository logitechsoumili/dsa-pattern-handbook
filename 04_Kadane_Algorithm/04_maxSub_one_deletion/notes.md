<h2><a href="https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion">1186. Maximum Subarray Sum with One Deletion</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Statement

Given an array of integers `arr`, return the maximum sum for a non-empty subarray (containing at least one element) with at most one element deleted. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum is maximum.

Note that the subarray must be non-empty after deleting one element.

### Constraints:
*   $1 \le \text{arr.length} \le 10^5$
*   $-10^4 \le \text{arr}[i] \le 10^4$

---

## Intuition

This problem is an extension of the classic **Maximum Subarray Sum (Kadane's Algorithm)**. In Kadane's algorithm, we only track the maximum subarray sum ending at each index without any deletions. Here, we are allowed to delete **at most one** element.

### Dynamic Programming State Representation

To solve this, we can maintain two states at each index $i$:

1.  **`noDel`**: The maximum subarray sum ending at index $i$ with **zero** deletions.
2.  **`oneDel`**: The maximum subarray sum ending at index $i$ with **exactly one** deletion.

### State Transitions

At each element `arr[i]`, we need to update our states based on the decisions made at the previous index $i - 1$:

#### 1. Updating `noDel` (Zero Deletions)
This is exactly the standard Kadane's transition. At index $i$, we can either:
*   Start a new subarray starting at the current element: `arr[i]`
*   Extend the previous subarray ending at $i - 1$ with no deletions: `noDel_prev + arr[i]`

$$\text{noDel}_i = \max(\text{arr}[i], \text{noDel}_{i-1} + \text{arr}[i])$$

#### 2. Updating `oneDel` (One Deletion)
For the subarray ending at index $i$ to have exactly one deletion, we have two options:
*   **Delete the current element `arr[i]`**: This means we take the maximum subarray sum ending at $i - 1$ with zero deletions. The current element is ignored: `noDel_prev`.
*   **Extend a subarray that already has one deletion**: This means we take the maximum subarray sum ending at $i - 1$ with one deletion and extend it to include `arr[i]`: `oneDel_prev + arr[i]`.

$$\text{oneDel}_i = \max(\text{noDel}_{i-1}, \text{oneDel}_{i-1} + \text{arr}[i])$$

> [!IMPORTANT]
> Since we need a non-empty subarray, if the array has only negative numbers, deleting the only element is not allowed. Our transition handles this by initializing `noDel = arr[0]`, `oneDel = 0`, and starting the loop from index `1`. This guarantees at least one element remains in the subarray.

---

## Approach

1.  Initialize three variables:
    *   `noDel = arr[0]`
    *   `oneDel = 0` (represents deletion state, initialized to 0 since at index 0 we cannot have a deleted subarray of size at least 1)
    *   `ans = arr[0]` (stores the global maximum sum found)
2.  Iterate through the array from index `1` to `n - 1`.
3.  For each element, update the states:
    *   Store the transition for `oneDel` using the previous `noDel` value.
    *   Update `noDel` using the standard Kadane's transition.
    *   Update `ans` to be the maximum of `ans`, `noDel`, and `oneDel`.
4.  Return `ans`.

---

## Dry Run

Let's trace the algorithm with the input array: `arr = [1, -2, 0, 3]`

### Initialization:
*   `noDel = 1`
*   `oneDel = 0`
*   `ans = 1`

### Iteration Table:

| Index | Element | `oneDel` Update: `max(noDel_prev, oneDel_prev + arr[i])` | Updated `oneDel` | `noDel` Update: `max(arr[i], noDel_prev + arr[i])` | Updated `noDel` | `ans` Update: `max(ans, noDel, oneDel)` | Updated `ans` | Action / Explanation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | - | `0` | - | `1` | - | `1` | Initialize variables. |
| **1** | `-2` | `max(1, 0 + -2)` | `1` | `max(-2, 1 + -2)` | `-1` | `max(1, -1, 1)` | `1` | `oneDel = 1` (keeping `[1]`, deleting `-2`). `noDel = -1` (keeping `[1, -2]`). |
| **2** | `0` | `max(-1, 1 + 0)` | `1` | `max(0, -1 + 0)` | `0` | `max(1, 0, 1)` | `1` | `oneDel = 1` (keeping `[1, 0]`, deleting `-2`). `noDel = 0` (starting new subarray `[0]`). |
| **3** | `3` | `max(0, 1 + 3)` | `4` | `max(3, 0 + 3)` | `3` | `max(1, 3, 4)` | `4` | `oneDel = 4` (keeping `[1, 0, 3]`, deleting `-2`). `noDel = 3` (subarray `[0, 3]`). |

**Final Output**: `4`

---

## C++ Implementation

```cpp
class Solution {
public:
    int maximumSum(vector<int>& arr) {
        int noDel = arr[0];
        int oneDel = 0;
        int ans = arr[0];

        for (int i = 1; i < arr.size(); i++) {
            oneDel = max(noDel, oneDel + arr[i]);
            noDel = max(arr[i], noDel + arr[i]);

            ans = max(ans, max(noDel, oneDel));
        }

        return ans;
    }
};
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We perform a single pass over the array of size $n$, updating states in $O(1)$ time at each step. |
| **Space Complexity** | $O(1)$ | We only use a few integer variables (`noDel`, `oneDel`, `ans`) to track the state, requiring constant space. |

---

## Pattern Recognition

Look for these clues to identify if this DP/Kadane variation is applicable:
*   **Contiguous subarray optimization**: You need to find an optimal subarray.
*   **Allowed exceptions/operations**: The problem permits a single exception or deletion, which introduces extra states (e.g., state with 0 operations done vs. state with 1 operation done).
*   **Dependencies on previous states**: The optimal subarray sum ending at index $i$ depends on the optimal subarray sum ending at index $i-1$.

---

## Key Takeaways

*   **State Split**: Multi-state DP is powerful when a simple decision (like deleting an element) splits the path into multiple scenarios.
*   **Order of Updates**: We must update `oneDel` using the previous `noDel` value *before* updating `noDel` for the current index, ensuring that we don't use the same element twice for the same state transition.
*   **Constant Space**: By only keeping track of state values from the previous step, the space complexity is optimized to $O(1)$.
