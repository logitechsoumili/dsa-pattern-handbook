# Prefix Sum Pattern

## Overview

The Prefix Sum pattern is a fundamental algorithmic technique used to perform fast range sum queries on an array or sequence. By precomputing cumulative totals where each position $i$ stores the sum of all elements from index $0$ to $i$, range sum queries over any contiguous interval $[L, R]$ can be computed in constant $O(1)$ time rather than scanning all elements in $O(R - L + 1)$ time. 

When combined with HashMaps / Hash Tables, Prefix Sum allows us to solve complex subarray search, counting, and optimization problems (including arrays containing negative numbers) in linear $O(n)$ time.

---

## Recognition Signals

Consider using the Prefix Sum pattern when:
*   You need to compute **range sums** or cumulative statistics over contiguous subarrays repeatedly.
*   The problem asks to find a **contiguous subarray** that matches a target sum, target remainder, or target balance constraint.
*   The array contains **negative numbers**, which prevents standard Two-Pointer or Sliding Window techniques from working because cumulative sums are non-monotonic.
*   You need to convert relative element counts (e.g. equal counts of two character types) into numeric target sums.
*   Constraints require an $O(n)$ or $O(n \log n)$ time complexity solution (where $n \ge 10^4$).

---

## Core Concepts

*   **Cumulative Sum Array:** A prefix array `prefix` of size $n + 1$ defined as:
    $$\text{prefix}[0] = 0$$
    $$\text{prefix}[i + 1] = \text{prefix}[i] + \text{nums}[i]$$
*   **Constant Time Range Sum:** The sum of elements in contiguous subarray $\text{nums}[L \dots R]$ is computed instantly via difference:
    $$\text{sum}(L \dots R) = \text{prefix}[R + 1] - \text{prefix}[L]$$
*   **Running Prefix Sum (Space Optimization):** When full range lookup is not required, we can maintain a single scalar variable `current_sum` during traversal, reducing auxiliary space from $O(n)$ to $O(1)$.
*   **Prefix Sum + HashMap Equation Transformation:**
    For target condition $\text{prefix}[R + 1] - \text{prefix}[L] = k$, fix current prefix at $R$ ($\text{current\_sum}$) and look up required previous prefix state:
    $$\text{previous\_prefix} = \text{current\_sum} - k$$
*   **Frequency Map vs. First-Occurrence Map:**
    *   **Counting Subarrays:** Store **frequencies** of seen prefix states (e.g., `prefix_sum -> count`).
    *   **Maximizing Subarray Length:** Store the **earliest index** of each prefix state (e.g., `prefix_balance -> earliest_index`).

---

## Templates

### 1. Basic Static Range Sum Precomputation

```text
Algorithm: Prefix Sum Precomputation
------------------------------------
n = size of nums
prefix = array of size (n + 1) initialized to 0

for i from 0 to n - 1:
    prefix[i + 1] = prefix[i] + nums[i]

// To query sum of subarray nums[L...R]:
function query_range_sum(L, R):
    return prefix[R + 1] - prefix[L]
```

### 2. Prefix Sum + HashMap (Counting Subarrays matching target condition)

```text
Algorithm: Prefix Sum HashMap (Count Subarrays)
-----------------------------------------------
current_sum = 0
count = 0
freq = hashmap / dictionary equivalent
freq[0] = 1  // Base case: empty prefix sum 0 has frequency 1

for num in nums:
    current_sum += num
    target_state = compute_target_state(current_sum)
    
    if target_state exists in freq:
        count += freq[target_state]
        
    freq[current_state] = freq.get(current_state, 0) + 1

return count
```

### 3. Prefix Sum + HashMap (Longest Subarray with Target Sum)

```text
Algorithm: Prefix Sum HashMap (Max Length Subarray)
---------------------------------------------------
current_sum = 0
max_len = 0
first_seen = hashmap / dictionary equivalent
first_seen[0] = -1  // Base case: prefix sum 0 occurs at index -1

for i from 0 to size(nums) - 1:
    current_sum += nums[i]
    target_state = compute_target_state(current_sum)
    
    if target_state exists in first_seen:
        length = i - first_seen[target_state]
        max_len = max(max_len, length)
        
    if current_state NOT in first_seen:
        first_seen[current_state] = i  // Record ONLY earliest occurrence

return max_len
```

---

## Common Variations

1.  **Running Balance Transformation ($0 \to -1, 1 \to +1$):** Used for equal count problems by converting binary choices into $+1$ and $-1$ to search for zero-sum subarrays.
2.  **Modulo Remainder Prefix Sum:** Used for divisibility constraints by storing normalized remainders $\text{rem} = ((\text{sum} \pmod k) + k) \pmod k$ in the lookup structure.
3.  **2D Prefix Sum (Matrix Range Queries):** Precomputing 2D cumulative region sums to answer subgrid sum queries in $O(1)$ time.
4.  **Difference Array (Range Updates):** The dual of Prefix Sum, where range increments are recorded at boundaries $[L, R+1]$ and prefix summed at the end.

---

## Complexity Characteristics

*   **Time Complexity:** 
    *   Precomputation: $O(n)$
    *   Range Query: $O(1)$
    *   Prefix Sum + HashMap single pass: $O(n)$ average time.
*   **Space Complexity:** 
    *   Prefix Array: $O(n)$
    *   Running Scalar Prefix Sum: $O(1)$
    *   HashMap lookup table: $O(n)$ or $O(k)$ distinct keys.

---

## Problems Solved

| # | Problem | Key Lesson |
| - | ------- | ---------- |
| 1 | [Find Pivot Index](./01_find_pivot_index) ([Notes](./01_find_pivot_index/notes.md)) | Running prefix sum comparison ($\text{right} = \text{total} - \text{left} - \text{curr}$) achieves $O(1)$ space. |
| 2 | [Subarray Sum Equals K](./02_subarray_sum_equals_k) ([Notes](./02_subarray_sum_equals_k/notes.md)) | Fix current prefix $R$, algebraically derive required previous prefix $\text{current} - k$, and lookup count via frequency HashMap. |
| 3 | [Subarray Sums Divisible by K](./03_subarray_sums_divisible_by_k) ([Notes](./03_subarray_sums_divisible_by_k/notes.md)) | Equivalence of modulo remainders $\text{prefix}[R+1] \pmod k = \text{prefix}[L] \pmod k$. Normalize remainders to handle negative numbers. |
| 4 | [Contiguous Array](./04_contiguous_array) ([Notes](./04_contiguous_array/notes.md)) | Map $0 \to -1$ and $1 \to +1$ to transform equal count search to zero-sum subarray search. Store earliest index in HashMap to maximize length. |

---

## Common Mistakes

*   ❌ **Forgetting the Base Case (`map[0] = 1` or `map[0] = -1`):** Failing to initialize the hashmap for prefix sum `0` misses valid subarrays starting at index `0`.
*   ❌ **Updating Map Before Lookup:** Checking target state after inserting the current prefix state causes self-matching when target is `0` or remainder is `0`.
*   ❌ **Un-normalized Negative Remainders:** Relying on language-dependent `%` operators without normalizing negative remainders via `((rem % k) + k) % k`.
*   ❌ **Overwriting Earliest Indices:** Overwriting stored indices in maximum length problems reduces subarray length calculations. Only record the index on the first encounter.

---

## Interview Takeaways

*   **Non-Monotonic Arrays:** Whenever a contiguous subarray sum problem involves negative numbers, sliding window will fail. Immediately pivot to Prefix Sum + HashMap.
*   **Equation Rearrangement:** Always state the target range condition mathematically and isolate the unknown previous state to determine what to store in the hashmap.
*   **Frequency vs. Earliest Index:** Use frequency maps for counting problems, and first-occurrence index maps for length optimization problems.
