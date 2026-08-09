<h2><a href="https://leetcode.com/problems/subarray-sums-divisible-by-k">974. Subarray Sums Divisible by K</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />

---

## Problem Statement

Given an integer array `nums` and an integer `k`, return the *number of non-empty subarrays that have a sum divisible by `k`*.

A **subarray** is a contiguous part of an array.

### Constraints:
*   $1 \le \text{nums.length} \le 3 \times 10^4$
*   $-10^4 \le \text{nums}[i] \le 10^4$
*   $2 \le k \le 10^4$

---

# 1. Problem Intuition

- We need to find the total count of contiguous subarrays whose sum is a multiple of $k$, meaning $\text{sum}(L \dots R) \pmod k = 0$.
- Because we are evaluating range sums over contiguous sequences, calculating prefix sums is a natural starting point.
- Instead of memorizing a remainder hashmap trick, let's derive how mathematical modulo properties naturally lead to the optimal algorithm.

---

# 2. Brute Force — O(n^3)

The most direct approach checks every possible subarray $(L, R)$:
1. Pick a starting index $L$.
2. Pick an ending index $R \ge L$.
3. Sum elements from $L$ to $R$.
4. Check if $\text{current\_sum} \pmod k == 0$. If so, increment count.

```text
Algorithm: Brute Force
----------------------
count = 0
for L from 0 to n - 1:
    for R from L to n - 1:
        current_sum = 0
        for i from L to R:
            current_sum += nums[i]
        if current_sum % k == 0:
            count += 1
return count
```

### Complexity Analysis
- **All $(L, R)$ pairs**: $O(n^2)$
- **Sum computation per pair**: $O(n)$
- **Total Time Complexity**: $O(n^3)$
- **Space Complexity**: $O(1)$

---

# 3. First Optimization: Prefix Sum — O(n^2)

We can eliminate the inner loop by precomputing cumulative prefix sums:

$$\text{prefix}[0] = 0$$
$$\text{prefix}[i + 1] = \text{prefix}[i] + \text{nums}[i]$$

The sum of subarray $\text{nums}[L \dots R]$ can be computed in $O(1)$ time:

$$\text{sum}(L \dots R) = \text{prefix}[R + 1] - \text{prefix}[L]$$

Now the condition for a subarray to be divisible by $k$ becomes:

$$(\text{prefix}[R + 1] - \text{prefix}[L]) \pmod k = 0$$

```text
Algorithm: Prefix Sum O(n^2)
----------------------------
prefix = array of size (n + 1) filled with 0
for i from 0 to n - 1:
    prefix[i + 1] = prefix[i] + nums[i]

count = 0
for L from 0 to n - 1:
    for R from L to n - 1:
        subarray_sum = prefix[R + 1] - prefix[L]
        if subarray_sum % k == 0:
            count += 1
return count
```

### Complexity Analysis
- **Prefix construction**: $O(n)$
- **Evaluating all pairs $(L, R)$**: $O(n^2)$
- **Total Time Complexity**: $O(n^2)$
- **Space Complexity**: $O(n)$

---

# 4. Why O(n^2) Is Still Not Enough

Constraints specify $n \le 3 \times 10^4$. An $O(n^2)$ approach requires approximately $(3 \times 10^4)^2 = 9 \times 10^8$ operations, exceeding typical execution limits and causing a **Time Limit Exceeded (TLE)**.

> [!IMPORTANT]
> **Key Optimization Question:**
> Can we process elements in a single pass ($R$) and determine algebraically what condition a previous prefix $L$ must satisfy to form a sum divisible by $k$?

---

# 5. Deriving the O(n) Solution Algebraically

Start with the target condition for a valid subarray ending at index $R$:

$$(\text{prefix}[R + 1] - \text{prefix}[L]) \pmod k = 0$$

According to modular arithmetic congruence rules:

$$A - B \equiv 0 \pmod k \iff A \equiv B \pmod k$$

Therefore:

$$\text{prefix}[R + 1] \pmod k = \text{prefix}[L] \pmod k$$

### Key Insight

Two prefix sums $\text{prefix}[R + 1]$ and $\text{prefix}[L]$ produce a subarray sum divisible by $k$ **if and only if they yield the exact same remainder when divided by $k$**.

```text
[------ prefix[L] (remainder r) ------][--- subarray sum (divisible by k) ---]
[-------------------- prefix[R + 1] (remainder r) --------------------]
```

When we subtract $\text{prefix}[L]$ from $\text{prefix}[R + 1]$, their identical remainders $r$ cancel out, leaving a range sum with a remainder of $0$ (a multiple of $k$).

Thus, as we traverse the array at index $R$, we don't need to check every previous index $L$. We only need to ask:

> *"How many previous prefix sums had the SAME remainder when divided by $k$ as my current prefix sum?"*

---

# 6. Handling Negative Remainders (Language-Independent Modulo Logic)

A crucial detail in this problem is handling arrays with negative integers.

In standard mathematical modulo arithmetic:
$$\text{remainder} \in [0, k - 1]$$

However, in programming languages like C++, Java, JavaScript, and C#, the `%` operator returns a negative remainder when the dividend is negative. For example:
$$-2 \% 5 = -2$$

Mathematically, $-2 \equiv 3 \pmod 5$ (since $-2 = -1 \times 5 + 3$). If one prefix sum gives a remainder of $-2$ and another gives $3$, a standard equality check between remainder variables would fail even though their difference is divisible by $5$ ($3 - (-2) = 5$).

### Universal Remainder Normalization Formula

To ensure remainders remain in $[0, k - 1]$ across all programming languages:

$$\text{rem} = ((\text{current\_sum} \pmod k) + k) \pmod k$$

*   **In languages like Python**, the `%` operator naturally returns remainders in $[0, k-1]$ for positive divisors $k$.
*   **In languages like C++ / Java**, adding $k$ and taking `% k` normalizes any negative result into the non-negative range $[0, k - 1]$.

---

# 7. Why a HashMap or Frequency Array?

As we iterate through `nums`, we compute the running prefix sum and its normalized remainder `rem`.

At each position, we need to know:
- How many times has this normalized remainder `rem` appeared previously?

Because $0 \le \text{rem} < k$, we can store remainder frequencies using:
1. A **frequency HashMap / Hash Table** (mapping `rem -> count`).
2. Or a **direct array / lookup vector** of size $k$ (where index `r` stores the frequency of remainder `r`).

---

# 8. Base HashMap State — `freq[0] = 1`

Before processing any elements (at imaginary index $-1$), the prefix sum is $0$, and $0 \pmod k = 0$.

Initializing remainder `0` with a frequency of `1` accounts for valid subarrays starting from index $0$ whose total sum is directly divisible by $k$.

### Example:
`nums = [4, 5]`, `k = 5`
- Index 0 (`num = 4`): `sum = 4`, `rem = 4 % 5 = 4`. Frequency of remainder `4` is 0. Record `freq[4] = 1`.
- Index 1 (`num = 5`): `sum = 9`, `rem = 9 % 5 = 4`. Remainder `4` was seen 1 time before (at index 0). Add 1 to count. Subarray `nums[1...1]` (`[5]`) has sum 5, which is divisible by 5.

If `nums = [5]`, `k = 5`:
- Index 0 (`num = 5`): `sum = 5`, `rem = 5 % 5 = 0`. Since `freq[0]` is initialized to 1, we immediately count 1 valid subarray (`[5]`).

---

# 9. Optimal Solution — O(n)

### Language-Neutral Pseudocode

```text
Algorithm: Subarray Sums Divisible by K
---------------------------------------
Initialize current_sum = 0
Initialize count = 0
Initialize freq = hashmap (or array of size k initialized to 0)
freq[0] = 1  // Base case: empty prefix has remainder 0

For each num in nums:
    current_sum += num
    
    // Normalize remainder to [0, k - 1]
    rem = ((current_sum % k) + k) % k
    
    // Add number of previous prefixes with the same remainder
    if rem exists in freq:
        count += freq[rem]
    
    // Record current remainder frequency
    freq[rem] = freq.get(rem, 0) + 1

Return count
```

### Complexity Analysis
- **Time Complexity**: $O(n)$, as we iterate through `nums` once and perform $O(1)$ lookup and insertion per element.
- **Space Complexity**: $O(\min(n, k))$ when using a Hash Table, or $O(k)$ when using a fixed frequency array of size $k$.

---

# 10. Full Optimization Journey

```text
Brute Force O(n^3)
    ↓
Repeated range sum calculations
    ↓
Prefix Sum O(n^2)
    ↓
O(n^2) still too slow for n = 30,000
    ↓
Isolate range condition: (prefix[R+1] - prefix[L]) % k == 0
    ↓
Apply Modulo Congruence: prefix[R+1] % k == prefix[L] % k
    ↓
Normalize remainders to [0, k - 1] to handle negative numbers
    ↓
Track frequency of seen remainders in HashMap / Frequency Array
    ↓
O(n) Time | O(k) Space Optimal Solution
```

---

# 11. Problem-Solving Takeaway

When solving subarray problems involving divisibility or remainders:

1. **Transform range sums to prefix differences**:
   $$\text{sum}(L \dots R) = \text{prefix}[R + 1] - \text{prefix}[L]$$
2. **Apply Modular Arithmetic**:
   $$(\text{prefix}[R + 1] - \text{prefix}[L]) \equiv 0 \pmod k \implies \text{prefix}[R + 1] \equiv \text{prefix}[L] \pmod k$$
3. **Normalize Remainders**: Ensure remainders are non-negative ($0 \le \text{rem} < k$) to make comparisons consistent across language implementations.
4. **Use Remainder Frequencies**: Instead of storing indices, store the frequency of remainders encountered so far.

---

# 12. Comparison: Subarray Sum Equals K vs. Divisible by K

| Feature | Subarray Sum Equals K | Subarray Sums Divisible by K |
| :--- | :--- | :--- |
| **Target Condition** | $\text{prefix}[R+1] - \text{prefix}[L] = k$ | $(\text{prefix}[R+1] - \text{prefix}[L]) \pmod k = 0$ |
| **Algebraic Shift** | $\text{prefix}[L] = \text{current\_prefix} - k$ | $\text{prefix}[L] \pmod k = \text{current\_prefix} \pmod k$ |
| **Map Key** | Prefix Sum Value | Normalized Remainder (`rem`) |
| **Negative Handling** | Direct arithmetic | Remainder normalization `((rem % k) + k) % k` |

---

# 13. Recognition Cues & Edge Cases

*   **Keywords**: "contiguous subarray", "sum divisible by $k$", "multiple of $k$".
*   **Negative Numbers**: Input elements can be negative. Always normalize remainders before looking up or updating frequencies.
*   **Array vs. HashMap**: If $k$ is small (e.g., $k \le 10^4$), a fixed-size array/vector of length $k$ can be used instead of a hash table for faster execution and lower space overhead.
