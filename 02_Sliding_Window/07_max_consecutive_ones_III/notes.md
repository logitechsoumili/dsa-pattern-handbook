<h2><a href="https://leetcode.com/problems/max-consecutive-ones-iii/">Max Consecutive Ones III</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Statement

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

## Example

**Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2`  
**Output:** `6`  
**Explanation:** By flipping the two `0`s at indices 4 and 5, the input array becomes `[1,1,1,0,1,1,1,1,1,1,0]`. The longest contiguous subarray of `1`s is `[1,1,1,1,1,1]` from index 4 to index 9, which has length 6.

**Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3`  
**Output:** `10`  
**Explanation:** By flipping the `0`s at indices 5, 9, and 12, the input array becomes `[0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1]`. The longest contiguous subarray of `1`s is `[1,1,1,1,1,1,1,1,1,1]` from index 5 to index 14, which has length 10.

## Brute Force Approach

### Intuition

A brute force solution checks all possible subarrays. For each subarray, we count the number of `0`s. If the count of `0`s is less than or equal to `k`, it means we can flip all the `0`s in this subarray to `1`s, forming a contiguous sequence of all `1`s. 

We check every single subarray, and if it is valid, we update the maximum length.

### Algorithm

1. Iterate over all possible starting indices `i` from `0` to `len(nums) - 1`.
2. For each `i`, iterate over all possible ending indices `j` from `i` to `len(nums) - 1`.
3. For each subarray `nums[i:j+1]`:
   - Count the number of zeros (`zero_count`) inside the subarray.
   - If `zero_count <= k`, it is valid. Update `max_len = max(max_len, j - i + 1)`.
   - If `zero_count > k`, we can break the inner loop early because expanding the subarray further will only add more elements, potentially increasing the zero count but never decreasing it.
4. Return `max_len`.

```python
def longestOnes_bruteforce(nums: List[int], k: int) -> int:
    max_len = 0
    for i in range(len(nums)):
        zero_count = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zero_count += 1
            
            if zero_count <= k:
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len
```

```cpp
int longestOnes_bruteforce(vector<int>& nums, int k) {
    int maxLen = 0;
    for (int i = 0; i < nums.size(); i++) {
        int zeroCount = 0;
        for (int j = i; j < nums.size(); j++) {
            if (nums[j] == 0) {
                zeroCount++;
            }
            if (zeroCount <= k) {
                maxLen = max(maxLen, j - i + 1);
            } else {
                break;
            }
        }
    }
    return maxLen;
}
```

- **Time Complexity:** O(n^2) due to nested loops iterating over subarrays.
- **Space Complexity:** O(1) auxiliary space as we only use a few integer variables.

## Optimized Approach (Sliding Window)

### Pattern Used

This problem is solved using the **Variable-Size Sliding Window** pattern. We expand the window using a `right` pointer to include new numbers and contract it from the `left` when the window condition is violated.

### Key Observation

The problem of "finding the maximum number of consecutive ones after flipping at most $k$ zeros" is equivalent to "finding the longest contiguous subarray (window) that contains at most $k$ zeros." 

If a window contains at most $k$ zeros, we can flip all of those zeros to ones. This will produce a valid contiguous subarray containing only ones.

### Why this problem is related to Longest Repeating Character Replacement

In **Longest Repeating Character Replacement**, we find the longest substring where we can replace at most `k` characters to match the most frequent character.
* The window validity condition is: `windowLen - maxFreq <= k`
* Here, `windowLen - maxFreq` represents the count of all characters that are *not* the most frequent character in the current window (i.e. the "bad" characters that we must change).

In **Max Consecutive Ones III**, we want to make all elements `1`.
* The target element is always `1`, and the element we want to replace (flip) is always `0`.
* The count of elements that do not match our target is simply the count of `0`s (represented by `zeroCount`).
* Thus, `zeroCount` plays the exact same role as `windowLen - maxFreq`.
* This problem is a binary-array variant of character replacement: our alphabet is binary (`{0, 1}`) and our target character is fixed as `1`.

### Why a frequency map is unnecessary here

In the general character replacement problem, we don't know in advance which character will be the most frequent one (the target) or what characters we will replace, so we use a frequency map to keep track of counts and dynamically compute the most frequent character.

Here, because the array is binary and our goal is fixed (make all elements `1` by replacing `0`s):
1. The target is always `1`.
2. The replaced elements are always `0`.
3. The count of replaced elements is exactly the count of `0`s.

Therefore, we only need to track the count of `0`s using a single integer variable `zeroCount` rather than maintaining a full hash map.

### Window Validity Condition

The window `nums[left:right+1]` is valid if and only if the number of zeros it contains does not exceed `k`:
```python
zeroCount <= k
```
If `zeroCount > k`, the window becomes invalid, and we must shrink it from the left until `zeroCount <= k` again.

### Step-by-Step Sliding Window Logic

1. Initialize `left = 0`, `zeroCount = 0`, and `maxLen = 0`.
2. Loop `right` from `0` to `len(nums) - 1` to expand the window:
   - If `nums[right] == 0`, increment `zeroCount`.
3. If `zeroCount > k`, the window is invalid. Run a `while` loop to shrink the window from the left:
   - If the element leaving the window `nums[left] == 0`, decrement `zeroCount`.
   - Increment `left` to move the left boundary.
4. Once `zeroCount <= k`, update the maximum valid length: `maxLen = max(maxLen, right - left + 1)`.
5. Return `maxLen`.

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeroCount = maxLen = 0

        for right in range(len(nums)):
            # Expand the window: Include nums[right]
            if nums[right] == 0:
                zeroCount += 1

            # Shrink the window if we have exceeded k zeros
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            # Update the maximum valid window length found so far
            maxLen = max(maxLen, right - left + 1)

        return maxLen
```

```cpp
class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int zeroCount = 0, left = 0, maxLen = 0;

        for (int right = 0; right < nums.size(); right++){
            if (nums[right] == 0) zeroCount++;

            while (zeroCount > k){
                if (nums[left] == 0) zeroCount--;
                left++;
            }

            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};
```

### Dry Run Example

Let's trace the algorithm with `nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]` and `k = 2`.

| Step | `right` | `nums[right]` | `zeroCount` | Window (`nums[left:right+1]`) | Validity / Action | `maxLen` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 1 | 0 | `[1]` | Valid (`0 <= 2`). Update `maxLen`. | 1 |
| 2 | 1 | 1 | 0 | `[1, 1]` | Valid (`0 <= 2`). Update `maxLen`. | 2 |
| 3 | 2 | 1 | 0 | `[1, 1, 1]` | Valid (`0 <= 2`). Update `maxLen`. | 3 |
| 4 | 3 | 0 | 1 | `[1, 1, 1, 0]` | Valid (`1 <= 2`). Update `maxLen`. | 4 |
| 5 | 4 | 0 | 2 | `[1, 1, 1, 0, 0]` | Valid (`2 <= 2`). Update `maxLen`. | 5 |
| 6 | 5 | 0 | 3 | `[1, 1, 1, 0, 0, 0]` | **Invalid** (`3 > 2`). Shrink from left. <br> - `left = 0` (val 1): `left` becomes 1. <br> - `left = 1` (val 1): `left` becomes 2. <br> - `left = 2` (val 1): `left` becomes 3. <br> - `left = 3` (val 0): `zeroCount` becomes 2, `left` becomes 4. <br> **Validated** (`2 <= 2`). Window is now `[0, 0]`. | 5 |
| 7 | 6 | 1 | 2 | `[0, 0, 1]` (indices 4 to 6) | Valid (`2 <= 2`). Update `maxLen`. | 5 |
| 8 | 7 | 1 | 2 | `[0, 0, 1, 1]` (indices 4 to 7) | Valid (`2 <= 2`). Update `maxLen`. | 5 |
| 9 | 8 | 1 | 2 | `[0, 0, 1, 1, 1]` (indices 4 to 8) | Valid (`2 <= 2`). Update `maxLen`. | 5 |
| 10 | 9 | 1 | 2 | `[0, 0, 1, 1, 1, 1]` (indices 4 to 9) | Valid (`2 <= 2`). Update `maxLen`. | 6 |
| 11 | 10 | 0 | 3 | `[0, 1, 1, 1, 1, 0]` (indices 5 to 10) | **Invalid** (`3 > 2`). Shrink from left. <br> - `left = 4` (val 0): `zeroCount` becomes 2, `left` becomes 5. <br> **Validated** (`2 <= 2`). Window is now `[0, 1, 1, 1, 1, 0]`. | 6 |

**Final Output:** `maxLen = 6`

### Complexity Analysis

#### Time Complexity

- **O(n)** because the `right` pointer iterates through the array of length `n` exactly once, and the `left` pointer only moves forward, visiting each index at most once. Inside the loops, we only perform constant-time updates and comparisons.

#### Space Complexity

- **O(1)** auxiliary space since we only use a few integer variables (`left`, `zeroCount`, `maxLen`) and do not allocate any additional collections or hash maps.

## Common Mistakes

- **Incorrect check when shrinking:** Decrementing `zeroCount` on every step of the `while` loop instead of checking if the leaving element `nums[left]` is actually a `0`.
- **Using a full frequency map:** Maintaining a map or set for a binary input. Although it does not affect the time complexity class, it adds unnecessary space and runtime overhead.
- **Off-by-one errors:** Calculating window size using `right - left` instead of `right - left + 1`.
- **Shrinking too early:** Using an incorrect validity check (e.g. `zeroCount < k` instead of `zeroCount <= k`). A window with exactly `k` zeros is still valid.

## Key Takeaways

- **Track the Counter-Condition directly:** In binary arrays or scenarios with only two categories, we can count the frequency of the "bad" element directly using a single integer variable instead of an expensive map.
- **Subarray Window Equivalence:** Translating "flip at most $k$ zeros to get consecutive ones" into "find the longest subarray with at most $k$ zeros" is the key mapping that enables the Sliding Window technique.
- **Comparison to character replacement:** Recognizing that this is the same problem as *Longest Repeating Character Replacement* but on a binary alphabet with a fixed target character.
