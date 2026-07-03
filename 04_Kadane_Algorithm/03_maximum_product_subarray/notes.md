<h2><a href="https://leetcode.com/problems/maximum-product-subarray">152. Maximum Product Subarray</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Statement

Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return *the product*.

The test cases are generated so that the answer will fit in a **32-bit** integer.

A **subarray** is a contiguous subsequence of the array.

### Constraints:
*   $1 \le \text{nums.length} \le 2 \times 10^4$
*   $-10 \le \text{nums}[i] \le 10$
*   The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

---

## Why Normal Kadane Fails

Standard Kadane's Algorithm is designed for the **Maximum Subarray Sum** problem. It fails when applied directly to products due to the mathematical nature of multiplication compared to addition.

### 1. Multiplication Behaves Differently from Addition

In addition:
* Adding a positive number *increases* the sum.
* Adding a negative number *decreases* the sum.
* Sums change monotonically with sign.

In multiplication:
* Multiplying by a positive number changes the magnitude but keeps the sign.
* Multiplying by a negative number **flips the sign** of the product.
  * A very large positive product multiplied by a negative number becomes a very small negative product.
  * A very small negative product (large negative magnitude) multiplied by a negative number becomes a **very large positive product**.

### 2. Why Tracking Only the Maximum Product is Insufficient

If we only track the maximum product (`maxEnding`), we would discard negative products as they look like "sub-optimal" states. However, a negative product is a potential goldmine if we encounter another negative number later. 

#### Example: `[-2, 3, -4]`

If we trace this using standard Kadane's logic (only keeping the maximum product ending at each index):

1. `nums[0] = -2`: `maxEnding = -2`
2. `nums[1] = 3`: `maxEnding = max(3, -2 * 3) = 3` (We discard the product `-6` because it's smaller than `3`).
3. `nums[2] = -4`: `maxEnding = max(-4, 3 * -4) = -4`

Standard Kadane returns `3`. However, the contiguous subarray `[-2, 3, -4]` has a product of:
$$-2 \times 3 \times -4 = 24$$

The negative product from the first two elements ($-6$) multiplied by the next negative number ($-4$) yielded the global maximum of $24$. 

> [!IMPORTANT]
> The minimum (most negative) product ending at index $i - 1$ is just as important as the maximum product. When multiplied by a negative number, the minimum product flips to become the maximum product.

---

## Intuition

To solve this problem in $O(n)$ time, we must maintain two running values at each index $i$:
1. **`maxEnding`**: The maximum product of a subarray ending at index $i$.
2. **`minEnding`**: The minimum product of a subarray ending at index $i$.

### Role of Negative Numbers (The Sign-Flip Concept)

When the current element `nums[i]` is negative, it will flip the sign of whatever it multiplies:
* $\text{Positive} \times \text{Negative} = \text{Negative}$ (Shrinks value, becomes candidate for `minEnding`)
* $\text{Negative} \times \text{Negative} = \text{Positive}$ (Grows value, becomes candidate for `maxEnding`)

Therefore, when `nums[i] < 0`:
* The new candidate for `maxEnding` is obtained by multiplying `nums[i]` with the previous `minEnding`.
* The new candidate for `minEnding` is obtained by multiplying `nums[i]` with the previous `maxEnding`.

To handle this role reversal cleanly, we can **swap** `maxEnding` and `minEnding` whenever `nums[i] < 0` before calculating the new values.

### Start New Subarray vs Extend Existing Subarray

Just like standard Kadane's, at each step we must decide whether to:
1. **Extend** the existing product chain: `maxEnding * nums[i]` (or `minEnding * nums[i]`)
2. **Start a new subarray** starting exactly at the current element: `nums[i]` (e.g., if the previous product was $0$ or extremely close to it).

Thus, after resolving any potential swaps, the state transitions are:
$$\text{maxEnding}_i = \max(\text{nums}[i], \text{maxEnding}_{i-1} \times \text{nums}[i])$$
$$\text{minEnding}_i = \min(\text{nums}[i], \text{minEnding}_{i-1} \times \text{nums}[i])$$

---

## Approach

The optimized $O(n)$ solution works as follows:

1. **Initialize** three variables: `maxEnding`, `minEnding`, and `res` (the global maximum product), all set to `nums[0]`.
2. **Loop** from index `1` to `n - 1`. For each element `nums[i]`:
   * If `nums[i]` is negative, swap `maxEnding` and `minEnding`.
   * Update `maxEnding` to be the maximum of `nums[i]` and `maxEnding * nums[i]`.
   * Update `minEnding` to be the minimum of `nums[i]` and `minEnding * nums[i]`.
   * Update `res` with the maximum of `res` and `maxEnding`.
3. Return `res`.

### Code Formula Breakdown:
```cpp
if (nums[i] < 0) {
    swap(maxEnding, minEnding);
}
```
* **Why**: When `nums[i]` is negative, multiplying by it swaps the relative ordering of our products: the maximum product becomes the minimum, and the minimum product becomes the maximum. Swapping them upfront ensures we multiply the correct candidate to get the new maximum and minimum.

```cpp
maxEnding = max(nums[i], maxEnding * nums[i]);
minEnding = min(nums[i], minEnding * nums[i]);
```
* **Why**: At index $i$, the maximum product ending here is either the current element itself (starting a new subarray) or the extended product chain. The same logic applies to the minimum product.

---

## Dry Run 1

Array: `nums = [2, 3, -2, 4]`

### Initialization:
* `maxEnding = 2`
* `minEnding = 2`
* `res = 2`

### Iteration Table:

| Index | Element | Sign | Swap Action | `maxEnding` Update | `minEnding` Update | `res` Update | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | - | - | `2` | `2` | `2` | Initialize variables to `nums[0]`. |
| **1** | `3` | `+` | None | `max(3, 2 * 3) = 6` | `min(3, 2 * 3) = 3` | `max(2, 6) = 6` | Extend current positive chain. |
| **2** | `-2` | `-` | Swap `maxEnding` and `minEnding`<br>(`maxEnding = 3`, `minEnding = 6`) | `max(-2, 3 * -2) = -2` | `min(-2, 6 * -2) = -12` | `max(6, -2) = 6` | Swapped due to negative sign. A new minimum of `-12` is recorded. |
| **3** | `4` | `+` | None | `max(4, -2 * 4) = 4` | `min(4, -12 * 4) = -48` | `max(6, 4) = 6` | `res` remains `6` (the maximum subarray product is `[2, 3]`). |

**Final Output**: `6`

---

## Dry Run 2

Array: `nums = [-2, 3, -4]`

### Initialization:
* `maxEnding = -2`
* `minEnding = -2`
* `res = -2`

### Iteration Table:

| Index | Element | Sign | Swap Action | `maxEnding` Update | `minEnding` Update | `res` Update | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | - | - | - | `-2` | `-2` | `-2` | Initialize variables to `nums[0]`. |
| **1** | `3` | `+` | None | `max(3, -2 * 3) = 3` | `min(3, -2 * 3) = -6` | `max(-2, 3) = 3` | Discard negative chain for max, but store `-6` as min. |
| **2** | `-4` | `-` | Swap `maxEnding` and `minEnding`<br>(`maxEnding = -6`, `minEnding = 3`) | `max(-4, -6 * -4) = 24` | `min(-4, 3 * -4) = -12` | `max(3, 24) = 24` | Swap makes previous min `-6` the max base. Multiplying by `-4` yields `24`. |

**Final Output**: `24`

---

## C++ Implementation

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Initialize state trackers with the first element
        int maxEnding = nums[0];
        int minEnding = nums[0];
        int res = nums[0];

        // Iterate through the array starting from the second element
        for (size_t i = 1; i < nums.size(); ++i) {
            // If the current element is negative, maximum and minimum swap roles
            if (nums[i] < 0) {
                std::swap(maxEnding, minEnding);
            }

            // Decide whether to start a new subarray or extend the existing one
            maxEnding = std::max(nums[i], maxEnding * nums[i]);
            minEnding = std::min(nums[i], minEnding * nums[i]);

            // Track the global maximum product found so far
            res = std::max(res, maxEnding);
        }

        return res;
    }
};
```

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We perform a single traversal of the input array of size $n$. All operations inside the loop (swapping, multiplications, and comparisons) take $O(1)$ time. |
| **Space Complexity** | $O(1)$ | We only maintain three integer tracking variables (`maxEnding`, `minEnding`, `res`), requiring no extra storage. |

---

## Pattern Recognition

Look for these clues in the problem description to identify if this variant of Kadane's Algorithm is applicable:

*   **Contiguous subarray optimization**: The problem asks for contiguous elements to achieve a target.
*   **Product instead of sum**: The optimization metric is multiplicative (`*`) rather than additive (`+`).
*   **Presence of negative numbers**: The array contains both negative and positive integers (if all numbers were positive, a simple greedy traversal or prefix product would suffice).
*   **Need to track both extremes**: The problem involves operations where an extreme minimum value can transition directly into an extreme maximum value (due to sign-flipping).
*   **Kadane-like optimization**: The need to decide at each step whether to extend the current sequence or reset to the current element.

---

## Common Mistakes

*   ❌ **Tracking Only the Maximum Product**: Forgetting to maintain `minEnding`. As shown in Dry Run 2, a negative minimum product can multiply with a negative element to yield a larger positive product.
*   ❌ **Incorrect Swap Timing**: Swapping `maxEnding` and `minEnding` after updating one of them. The swap must happen **before** calculating the new values, using the previous step's states.
*   ❌ **Mishandling Zeroes**: Assuming zeroes are discarded. A zero resets both `maxEnding` and `minEnding` to `0`, effectively forcing a restart of the subarray at the next non-zero element. The `std::max(nums[i], ...)` handles this automatically.
*   ❌ **Not Considering Single-Element Subarrays**: Initializing `maxEnding` or `minEnding` to `1` or `0` instead of `nums[0]`. This fails for negative single-element arrays (e.g. `nums = [-2]`).

---

## Key Takeaways

*   **Kadane for Multiplication**: We extend Kadane's algorithm to product space by tracking both maximum and minimum products ending at the current index.
*   **Track Both Extremes**: `maxEnding` stores the maximum positive product, and `minEnding` stores the minimum negative product.
*   **Negative Numbers Flip Roles**: A negative multiplier swaps the maximum and minimum values.
*   **`swap()` Simplifies Implementation**: Swapping variables on negative elements avoids complex conditional checks and keeps the transition code uniform.
*   **$O(n)$ Time, $O(1)$ Space**: The algorithm remains highly efficient and runs in linear time with constant memory.
