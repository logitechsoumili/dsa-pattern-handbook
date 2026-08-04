<h2><a href="https://leetcode.com/problems/subarray-sum-equals-k">560. Subarray Sum Equals K</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />

---

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the *total number of subarrays whose sum equals to `k`*.

A subarray is a contiguous **non-empty** sequence of elements within an array.

### Constraints:
*   $1 \le \text{nums.length} \le 2 \times 10^4$
*   $-1000 \le \text{nums}[i] \le 1000$
*   $-10^7 \le k \le 10^7$

---

# 1. Problem Intuition

- We need to count contiguous subarrays whose sum equals $k$.
- A subarray is determined by a left boundary $L$ and right boundary $R$.
- Since this involves sums of contiguous ranges, prefix sum is a natural tool to investigate.
- Do NOT immediately reveal the hashmap trick. Build toward it.

# 2. Brute Force — O(n^3)

Derive the most obvious solution:
- Pick every $L$.
- Pick every $R \ge L$.
- Use a third loop to calculate `nums[L...R]`.
- If the sum equals $k$, increment count.

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        
        for L in range(n):
            for R in range(L, n):
                current_sum = 0
                for i in range(L, R + 1):
                    current_sum += nums[i]
                if current_sum == k:
                    count += 1
                    
        return count
```

### Complexity Analysis
- **Choosing $L$**: $O(n)$
- **Choosing $R$**: $O(n)$
- **Calculating each subarray sum**: $O(n)$
- **Total Time Complexity**: $O(n^3)$
- **Space Complexity**: $O(1)$

---

### What repeated work are we doing?

**Answer:** We repeatedly calculate sums of overlapping ranges.

This motivates us to precompute range sums using **Prefix Sums**.

---

# 3. First Optimization: Prefix Sum — O(n^2)

Use the prefix convention:

$$\text{prefix}[0] = 0$$
$$\text{prefix}[i + 1] = \text{prefix}[i] + \text{nums}[i]$$

Therefore:

$$\text{sum}(L \dots R) = \text{prefix}[R + 1] - \text{prefix}[L]$$

### Why does this subtraction give the range sum?

Consider a small example array: `nums = [1, 2, 3]`.
- `prefix[0] = 0`
- `prefix[1] = 1`
- `prefix[2] = 1 + 2 = 3`
- `prefix[3] = 1 + 2 + 3 = 6`

To get the sum of subarray `nums[1...2]` (`[2, 3]`):
$$\text{sum}(1 \dots 2) = \text{prefix}[3] - \text{prefix}[1] = 6 - 1 = 5$$

`prefix[R + 1]` contains the sum of all elements from index $0$ up to $R$, while `prefix[L]` contains the sum of elements from index $0$ up to $L - 1$. Subtracting `prefix[L]` removes the unwanted prefix before index $L$, leaving exactly the sum of elements in `nums[L...R]`.

Now:
- Precompute prefix sums in $O(n)$.
- Still enumerate every $L$ and $R$.
- Calculate each range sum in $O(1)$.

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        count = 0
        for L in range(n):
            for R in range(L, n):
                if prefix[R + 1] - prefix[L] == k:
                    count += 1
                    
        return count
```

### Complexity Analysis
- **Prefix construction**: $O(n)$
- **All $(L, R)$ pairs**: $O(n^2)$
- **Each range sum**: $O(1)$
- **Total Time Complexity**: $O(n^2)$
- **Space Complexity**: $O(n)$

---

# 4. Why O(n^2) Is Still Not Enough

The problem constraint specifies $n \le 2 \times 10^4$.
With $n = 20,000$, an $O(n^2)$ solution requires roughly $(2 \times 10^4)^2 = 4 \times 10^8$ operations, which will cause a **Time Limit Exceeded (TLE)** in Python.

Trying every pair of boundaries is still too expensive.

> [!IMPORTANT]
> **Key Optimization Question:**
> We still have two changing boundaries $L$ and $R$. Can we fix one boundary and mathematically determine what the other boundary must satisfy?

---

# 5. Deriving the O(n) Solution Algebraically

Start with the target condition for a valid subarray:

$$\text{sum}(L \dots R) = k$$

Using prefix sums:

$$\text{prefix}[R + 1] - \text{prefix}[L] = k$$

Now fix $R$ (our current position as we traverse from left to right).

Since we are at position $R$, $\text{prefix}[R + 1]$ is **known** (let's call it $\text{currentPrefix}$).

Rearrange the equation to isolate $\text{prefix}[L]$:

$$\text{prefix}[L] = \text{prefix}[R + 1] - k$$

### Significance

We no longer need to loop over every possible left boundary $L$!

At the current position, we only need to answer:

> *"How many previous prefix sums are equal to $\text{currentPrefix} - k$?"*

Intuitively and geometrically:

$$\text{previousPrefix} + \text{wantedSubarray} = \text{currentPrefix}$$

Therefore:

$$\text{wantedSubarray} = \text{currentPrefix} - \text{previousPrefix} = k$$

So:

$$\text{previousPrefix} = \text{currentPrefix} - k$$

```text
[------ previous prefix ------][--- wanted subarray ---]
              P                         k
[--------------- current prefix ----------------------]
                           P + k
```

---

# 6. Why a HashMap?

While traversing from left to right, at each step we need to repeatedly ask:

> *"How many times have I previously seen prefix sum $X$?"*

where:

$$X = \text{currentSum} - k$$

Therefore, we use a **frequency hashmap**:

$$\text{prefix sum} \to \text{number of times previously seen}$$

Do NOT treat the hashmap as a memorized trick. The data structure follows naturally from the exact operation we need:
- If we only needed to check **existence**, a `HashSet` would suffice.
- Because we need the **COUNT of previous occurrences** (since duplicate prefix sums can exist), we require a **frequency HashMap**.

---

# 7. Why Frequency Matters

Multiple previous indices can produce the **same** prefix sum value (especially when `0`s or negative numbers exist in `nums`).

Consider `nums = [0, 0, 0]` and `k = 0`:
- Before starting: prefix sum `0` seen `1` time (at imaginary index `-1`).
- Index 0 (`num = 0`): `currentSum = 0`. `freq[currentSum - k] = freq[0] = 1`. Count becomes `1`. Then record `0` (now seen 2 times).
- Index 1 (`num = 0`): `currentSum = 0`. `freq[currentSum - k] = freq[0] = 2`. Count becomes `1 + 2 = 3`. Then record `0` (now seen 3 times).
- Index 2 (`num = 0`): `currentSum = 0`. `freq[currentSum - k] = freq[0] = 3`. Count becomes `3 + 3 = 6`.

Each previous occurrence represents a **different valid cut / start position** $L$.

Therefore, if:

$$\text{freq}[\text{currentSum} - k] = 3$$

there are $3$ distinct valid subarrays ending at the current index.

Hence:

```python
count += freq.get(currentSum - k, 0)
```

---

# 8. Why freq = {0: 1}?

There is conceptually a prefix sum of `0` before the array begins (at index `-1`).

Initializing `freq = {0: 1}` accounts for subarrays that start at index `0` and sum to $k$.

### Example:
`nums = [1, 2]`, `k = 3`

At index 1 (`num = 2`):
- `currentSum = 3`
- `currentSum - k = 3 - 3 = 0`

If `freq` did not contain `{0: 1}`, `freq.get(0, 0)` would return `0`, missing the valid subarray `nums[0...1]` (`[1, 2]`) which sums to `3`!

The base entry `{0: 1}` represents the empty prefix before index 0, allowing any prefix sum that equals $k$ directly to be counted.

---

# 9. Optimal Solution — O(n)

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        freq = {0: 1}
        count = 0

        for num in nums:
            currentSum += num

            count += freq.get(currentSum - k, 0)

            freq[currentSum] = freq.get(currentSum, 0) + 1

        return count
```

### Explanation of Key Lines

1. `currentSum += num`: Maintains the cumulative running sum up to the current element.
2. `count += freq.get(currentSum - k, 0)`:
   - **Meaning:** *"How many previous cut-points would leave a subarray of exactly $k$ between that point and my current position?"*
3. `freq[currentSum] = freq.get(currentSum, 0) + 1`:
   - **Meaning:** *"After checking subarrays ending here, record this prefix sum so future positions can use the current position as a possible cut-point."*

> [!IMPORTANT]
> **Lookup Order Matters:** We must check `freq.get(currentSum - k, 0)` **BEFORE** updating `freq[currentSum]`.
> If $k = 0$, adding `currentSum` to `freq` first would cause an index to match with itself as a non-empty subarray, producing false positive empty subarrays when $k=0$.

### Complexity Analysis
- **Time Complexity**: $O(n)$ average, since we traverse `nums` once and each HashMap lookup/insertion takes $O(1)$ average time.
- **Space Complexity**: $O(n)$, to store up to $n + 1$ unique prefix sums in the frequency hashmap.

---

# 10. Full Optimization Journey

```text
Brute Force O(n^3)
    ↓
Repeatedly calculating range sums
    ↓
Prefix Sum
    ↓
O(n^2): range sums are O(1), but still trying every (L, R)
    ↓
Fix R / current prefix
    ↓
prefix[R + 1] - prefix[L] = k
    ↓
prefix[L] = prefix[R + 1] - k
    ↓
Don't search every L
    ↓
Look up how many previous prefixes equal currentPrefix - k
    ↓
Frequency HashMap
    ↓
O(n)
```

---

# 11. Problem-Solving Takeaway

Instead of blindly memorizing "Prefix Sum + HashMap", apply this reusable 9-step reasoning pattern:

1. **Start with brute force.**
2. **Identify repeated work.**
3. **Use preprocessing** if it eliminates repeated work.
4. **Check whether the resulting complexity satisfies constraints.**
5. **If two variables/boundaries remain, try fixing one.**
6. **Write the validity condition mathematically.**
7. **Rearrange it to determine what the other value must be.**
8. **Ask what operation is now needed:**
   - existence? $\to$ `HashSet` / `HashMap`
   - frequency? $\to$ frequency `HashMap`
   - min/max? $\to$ monotonic queue / variable
   - ordered lookup? $\to$ balanced BST / segment tree
9. **Choose the data structure based on that operation.**

### Core Reusable Transformation

> *"I know the CURRENT value. What PREVIOUS value would make the condition valid?"*

- If I need to know **whether** that previous value existed $\to$ `HashSet` / `HashMap`.
- If I need to know **how many times** it existed $\to$ frequency `HashMap`.

---

# 12. Connection to Two Sum

Notice the exact structural parallel between **Two Sum** and **Subarray Sum Equals K**:

### Two Sum:
$$a + b = \text{target}$$
$$b = \text{target} - a$$
- Fix $a$ $\to$ determine exact $b$ needed $\to$ `HashMap` lookup.

### Subarray Sum Equals K:
$$\text{currentPrefix} - \text{previousPrefix} = k$$
$$\text{previousPrefix} = \text{currentPrefix} - k$$
- Fix $\text{currentPrefix}$ $\to$ determine exact $\text{previousPrefix}$ needed $\to$ frequency `HashMap` lookup.

Both problems share the exact same meta-pattern: **Fix one variable, derive its required counterpart algebraically, and eliminate search loops using state storage.**

---

# 13. Recognition Cues

Keep an eye out for these signals:

- **Contiguous subarray** range problems.
- Need sum or count of subarrays matching a condition.
- **Presence of negative numbers** (which prevents ordinary sliding-window / two-pointer reasoning because the sum is non-monotonic).
- **Prefix sum** transforms a subarray sum into a difference between two prefix states.
- The condition equation can be **rearranged** to isolate a required previous prefix state.
- Need the **frequency** of previously seen prefix states $\to$ frequency `HashMap`.
