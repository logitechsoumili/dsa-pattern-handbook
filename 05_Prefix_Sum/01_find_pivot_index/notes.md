<h2><a href="https://leetcode.com/problems/find-pivot-index">724. Find Pivot Index</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />

---

## Problem Statement

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly to the left** of the index is equal to the sum of all the numbers **strictly to the right** of the index.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the *leftmost pivot index*. If no such index exists, return `-1`.

### Constraints:
*   `1 <= nums.length <= 10^4`
*   `-1000 <= nums[i] <= 1000`

---

## Intuition

To find the pivot index, we need to compare the sum of elements before any index `i` (left sum) with the sum of elements after index `i` (right sum).

### Why Brute Force is $O(n^2)$

A naive brute-force approach would:
1. Iterate through each index `i` from `0` to `n - 1`.
2. For each index `i`, run a loop to calculate the sum of elements from index `0` to `i - 1` (`leftSum`).
3. Run another loop to calculate the sum of elements from index `i + 1` to `n - 1` (`rightSum`).
4. Compare `leftSum` and `rightSum`.

For an array of size $n$, this requires calculating sums repeatedly:
*   **Time Complexity**: $O(n^2)$
*   For $n = 10^4$, $O(n^2)$ is $10^8$ operations, which can be slow and inefficient.

### Key Observation behind Prefix Sum / Running Sum

We can optimize this to $O(n)$ time using a running sum.
Instead of recalculating the sums at each index:
1. The **total sum** of the array, `sum`, is constant.
2. If we keep a running sum of elements we have already visited, let's call it `left`, then at any index `i`:
   * The sum of elements strictly to the left of `i` is exactly `left`.
   * The sum of elements strictly to the right of `i` can be computed in $O(1)$ as:
     `right = sum - left - nums[i]`

> [!IMPORTANT]
> Since the total sum of the array is fixed, the right sum is simply the remaining portion of the total sum after subtracting the current element and the left sum. This allows us to avoid calculating prefix/suffix arrays or using nested loops.

---

## Approach (Running Prefix Sum)

1. Calculate the total sum of all elements in the array using `accumulate` (or a single pass).
2. Initialize `left` to `0`, which represents the sum of elements to the left of the current index.
3. Traverse the array from left to right:
   * Calculate the `right` sum: `sum - left - nums[i]`.
   * If `left == right`, return the current index `i`.
   * Update the running `left` sum by adding the current element: `left += nums[i]`.
4. If the loop completes without finding a pivot index, return `-1`.

### Variable Details:
*   `left`: Running sum of elements strictly to the left of index `i`. Starts at `0`.
*   `sum`: Total sum of all elements in the array.

---

## Dry Run

Let's trace the algorithm with the input array: `nums = [1, 7, 3, 6, 5, 6]`

### Initialization:
*   `left = 0`
*   `sum = 28`

### Iteration Table:

| Index | Element | Running `left` | Formula: `right = sum - nums[i] - left` | Comparison: `left == right` | Action / Explanation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0** | `1` | `0` | `28 - 1 - 0 = 27` | `0 != 27` | Continue. Update `left` to `0 + 1 = 1`. |
| **1** | `7` | `1` | `28 - 7 - 1 = 20` | `1 != 20` | Continue. Update `left` to `1 + 7 = 8`. |
| **2** | `3` | `8` | `28 - 3 - 8 = 17` | `8 != 17` | Continue. Update `left` to `8 + 3 = 11`. |
| **3** | `6` | `11` | `28 - 6 - 11 = 11` | `11 == 11` | **Pivot found!** Return index `3`. |

**Final Output**: `3`

---

## C++ Implementation

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left = 0;
        int sum = accumulate(nums.begin(), nums.end(), 0);

        for (int i = 0; i < nums.size(); i++){
            int right = sum - nums[i] - left;

            if (left == right) return i;

            left += nums[i];
        }
        return -1;
    }
};
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We perform one pass to calculate the total sum using `accumulate`, and a second pass to find the pivot index. Each pass takes linear time $O(n)$, resulting in overall $O(n)$ time complexity. |
| **Space Complexity** | $O(1)$ | We only use a constant amount of extra space for the running variables `left`, `sum`, and `right`. |

---

## Pattern Recognition

Look for these clues in the problem description to identify if a Running Prefix Sum approach is applicable:

*   **Subarray/Partition Comparison**: The problem asks to partition the array into two parts (left and right) and compare their properties (like sum or product).
*   **Linear Time Constraints**: The constraint on array size requires an $O(n)$ time complexity solution.
*   **Complementary Sum Relationship**: The sum of the right half is dependent on the total sum and the left sum, making it possible to derive one from another in $O(1)$ time.

---

## Key Takeaways

*   **Space Optimization**: Although we could use prefix and suffix sum arrays to solve this problem, a running sum variable reduces the space complexity from $O(n)$ to $O(1)$.
*   **Edge Case Handling**: At index `0`, `left` is correctly initialized to `0` (as there are no elements to its left). Similarly, if the pivot is at the last index, `right` will correctly evaluate to `0`.
*   **Strict Left/Right**: Remember that "strictly to the left" and "strictly to the right" excludes the current element `nums[i]`. Thus, the formula subtracts `nums[i]` from the total sum.
