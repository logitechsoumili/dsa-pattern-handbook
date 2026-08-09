<h2><a href="https://leetcode.com/problems/contiguous-array">525. Contiguous Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />

---

## Problem Statement

Given a binary array `nums`, return the *maximum length of a contiguous subarray with an equal number of `0`s and `1`s*.

### Constraints:
*   `1 <= nums.length <= 10^5`
*   `nums[i]` is either `0` or `1`.

---

# 1. Problem Intuition

- We need to find the longest contiguous subarray where the count of `0`s equals the count of `1`s:
  `count(0) == count(1)`
- At first glance, counting two distinct values inside dynamic ranges looks like a 2D window problem. However, by transforming the values, we can map this directly into a **Prefix Sum / Prefix Balance** problem.

---

# 2. Brute Force — O(n^2)

A naive solution examines every possible subarray `(L, R)`:
1. Pick a start index `L`.
2. Pick an end index `R >= L`.
3. Count the number of `0`s and `1`s in `nums[L...R]`.
4. If `count(0) == count(1)`, compute length `R - L + 1` and update the maximum length found so far.

```text
Algorithm: Brute Force
----------------------
max_length = 0
for L from 0 to n - 1:
    zeros = 0
    ones = 0
    for R from L to n - 1:
        if nums[R] == 0:
            zeros += 1
        else:
            ones += 1
        if zeros == ones:
            max_length = max(max_length, R - L + 1)
return max_length
```

### Complexity Analysis
- **All `(L, R)` pairs**: $O(n^2)$
- **Counting 0s and 1s incrementally**: $O(1)$ per iteration
- **Total Time Complexity**: $O(n^2)$
- **Space Complexity**: $O(1)$

---

# 3. Why O(n^2) Is Inefficient

With `n = 10^5`, an $O(n^2)$ solution requires `(10^5)^2 = 10^10` operations, causing a **Time Limit Exceeded (TLE)**.

We need a single-pass $O(n)$ strategy. But how can prefix sums help when we have binary counts (`0` and `1`) instead of normal numeric sums?

---

# 4. Step-by-Step Derivation to Optimal O(n) Solution

To solve this efficiently, we transform the problem step-by-step:

```text
Equal 0s and 1s  ──>  Balance Representation (+1 / -1)  ──>  Prefix Balance  ──>  Repeated Balances & Earliest Index HashMap
```

---

## Step 4.1: Value Transformation (Balance Representation)

Instead of maintaining separate counts for `0`s and `1`s, let me re-map the array elements:
- Treat `1` as `+1`
- Treat `0` as `-1`

Why does this transformation work?

Consider a subarray `nums[L...R]`:
- Every `1` adds `+1` to the sum.
- Every `0` subtracts `1` from the sum.

If a subarray has an **equal number of `0`s and `1`s**, then:

`count(1) * (+1) + count(0) * (-1) = 0`

> [!IMPORTANT]
> **Core Mathematical Transformation:**
> Finding a contiguous subarray with an equal number of `0`s and `1`s is **identical** to finding a contiguous subarray whose transformed sum equals **0**.

---

## Step 4.2: Expressing Range Sum as Difference of Prefix Balances

Let `balance[i]` be the prefix sum of the transformed array from index `0` to index `i`:

`balance[i] = sum of transformed elements from index 0 to i`

The sum of elements in subarray `nums[L...R]` is:

`sum(L...R) = balance[R] - balance[L - 1]`

For the subarray sum to equal 0:

`balance[R] - balance[L - 1] = 0` implies `balance[R] == balance[L - 1]`

### Key Observation:
Whenever the prefix balance at current index `R` is **equal** to the prefix balance at a previous index `L - 1`, the subarray between `L` and `R` has a net sum of 0, meaning it contains an equal number of `0`s and `1`s!

```text
Index:             -1    0    1    2    3    4    5
nums:                    0    1    0    1    1    0
transformed:            -1   +1   -1   +1   +1   -1
Prefix Balance:     0   -1    0   -1    0   +1    0
                    ^         ^         ^         ^
```

Notice how `balance = 0` occurs at index `-1`, index `1`, index `3`, and index `5`.
The subarray between index `2` and index `5` (`[0, 1, 1, 0]`) has balance `0` at both index `1` and index `5`, so its sum is `(-1) + 1 + 1 + (-1) = 0`.

---

## Step 4.3: Why Earliest Index is Necessary for Maximizing Length

The length of a valid subarray ending at index `R` starting after index `L - 1` is:

`length = R - (L - 1)`

To **maximize** this length for a fixed current index `R`, we want `L - 1` to be as **small** (as early) as possible!

Therefore:
- When we encounter a new balance value for the **first time**, we record its index in a HashMap / Dictionary (`first_seen[balance] = index`).
- If we encounter the **same** balance value again at a later index `R`, we do **NOT** update the recorded index in our map.
- Instead, we compute candidate length:
  `length = R - first_seen[balance]`
  and update our global maximum length `max_len = max(max_len, length)`.

> [!TIP]
> **Why do we keep only the earliest index?**
> Overwriting the stored index with a later index would decrease `R - first_seen[balance]`, giving a shorter subarray length. To get the *longest* valid subarray, we must measure distance from the *earliest* occurrence of that balance.

---

# 5. Base HashMap State — `first_seen[0] = -1`

Before processing any elements (at index `-1`), the prefix balance is `0`.

Initializing `first_seen[0] = -1` accounts for valid subarrays that start at index `0`.

### Example:
`nums = [0, 1]`
- Before loop: `first_seen = {0: -1}`
- `i = 0` (`num = 0`): `balance = 0 + (-1) = -1`. Not in map. Store `first_seen[-1] = 0`.
- `i = 1` (`num = 1`): `balance = -1 + 1 = 0`. Balance `0` is in map at index `-1`!
- Subarray length = `1 - (-1) = 2`. Maximum length = 2 (`[0, 1]`).

Without `first_seen[0] = -1`, a subarray starting at index `0` with equal 0s and 1s would not have its initial boundary recorded properly.

---

# 6. Optimal Solution — O(n)

### Language-Neutral Pseudocode

```text
Algorithm: Contiguous Array (Equal 0s and 1s)
----------------------------------------------
Initialize balance = 0
Initialize max_length = 0
Initialize first_seen = hashmap (or map equivalent)
first_seen[0] = -1  // Base case: prefix balance 0 before array starts

For i from 0 to len(nums) - 1:
    // Update balance: +1 for 1, -1 for 0
    if nums[i] == 1:
        balance += 1
    else:
        balance -= 1

    // If this balance was seen before, compute subarray length from earliest index
    if balance exists in first_seen:
        length = i - first_seen[balance]
        max_length = max(max_length, length)
    else:
        // Record only the EARLIEST index for this balance
        first_seen[balance] = i

Return max_length
```

### Complexity Analysis
- **Time Complexity**: $O(n)$, single pass through the array. Map lookup and insertion take $O(1)$ average time.
- **Space Complexity**: $O(n)$, in the worst case (e.g. array of all `1`s), the hashmap stores up to `n + 1` unique balance keys.

---

# 7. Full Optimization Journey

```text
Brute Force O(n^2) (Count 0s & 1s in all pairs)
    ↓
Transform problem: 0 -> -1 and 1 -> +1
    ↓
Subarray with equal 0s & 1s  <=>  Subarray sum equals 0
    ↓
Express subarray sum as prefix balance difference: balance[R] - balance[L-1] = 0
    ↓
Implies equal balances: balance[R] == balance[L-1]
    ↓
Maximize length R - (L-1) by storing the EARLIEST index of each balance
    ↓
HashMap storing balance -> earliest_index (with base state map[0] = -1)
    ↓
O(n) Time | O(n) Space Optimal Solution
```

---

# 8. Problem-Solving Takeaway

This problem showcases two key techniques:

1. **Indicator Transformation**: Converting binary choices (`0` vs `1`, or `A` vs `B`) into `+1` and `-1` allows tracking relative counts using a single numeric balance scalar.
2. **First-Occurrence HashMap Pattern**:
   - When **counting** subarrays $\to$ store **frequencies** in HashMap.
   - When **maximizing length** of subarray with sum 0 $\to$ store **earliest index** in HashMap.

---

# 9. Comparison across Prefix Sum + HashMap Problems

| Problem | Target | HashMap Key | HashMap Value | Map Update Rule |
| :--- | :--- | :--- | :--- | :--- |
| **Subarray Sum Equals K** | Sum `= k` | Prefix Sum | Frequency | Increment count on every occurrence |
| **Subarray Sums Divisible by K** | Sum `% k == 0` | Remainder `rem` | Frequency | Increment count on every occurrence |
| **Contiguous Array** | Sum `= 0` (after $0 \to -1$) | Prefix Balance | Earliest Index | Store index **only on first occurrence** |

---

# 10. Recognition Cues & Common Mistakes

*   **Recognition Cues**: Binary array, "equal number of X and Y", "longest contiguous subarray".
*   ❌ **Common Mistake — Overwriting stored index**: Overwriting `first_seen[balance]` with the latest index `i` reduces the calculated subarray length. Only set the value if the balance key is **not** present in the hashmap.
*   ❌ **Common Mistake — Forgetting base case**: Omitting `first_seen[0] = -1` causes valid prefix subarrays starting at index `0` to be ignored or computed with wrong length.
