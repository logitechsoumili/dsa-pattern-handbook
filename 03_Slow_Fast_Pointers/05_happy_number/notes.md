<h2><a href="https://leetcode.com/problems/happy-number">202. Happy Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

---

## Problem Overview

Given a positive integer $n$, determine if it is a **happy number**.

A happy number is defined by the following iterative process:
1.  Replace the number with the sum of the squares of its digits.
2.  Repeat the process.
3.  The process will terminate in one of two ways:
    *   The number becomes **$1$**, where it will remain in a self-loop ($1^2 = 1$).
    *   The sequence enters a **cycle** that does not include $1$, looping endlessly.

Numbers that eventually reach $1$ are **happy numbers** (return `true`), while numbers that loop endlessly in a cycle are **not happy numbers** (return `false`).

---

## Pattern Recognition

### Signals

Look for these key indicators that suggest this pattern:
*   **Repeated Transformation**: Performing the exact same deterministic computation on the output of the previous step.
*   **Infinite Loop**: The possibility that a sequence will repeat the same states indefinitely.
*   **Cycle Detection**: The core task requires identifying whether a sequence repeats or terminates.
*   **Constant Space**: The need to solve the problem in $O(1)$ extra space, preventing the caching of sequence history.
*   **Number Sequence**: Transitions occur over mathematical states rather than structural list nodes.

### Why Slow & Fast Pointers?

repeatedly applying the same operation creates a sequence of values that behaves exactly like a singly linked list. Because the transformation function is deterministic, any given number $n$ will always map to exactly one "next" number:
$$n \to \text{squareSum}(n)$$

This creates a directed functional graph where every node has an out-degree of exactly 1. Because each state maps to a single successor, starting from any number $n$ must eventually lead to either a self-loop at $1$ or a cycle of other values. Floyd's Cycle Detection Algorithm allows us to detect these loops in $O(1)$ space without storing visited numbers.

---

## Core Insight

Every number maps deterministically to a unique next value. 

For a **happy number** (e.g., $19$), the sequence converges directly to $1$:
$$19 \to 82 \to 68 \to 100 \to 1 \to 1 \dots$$

For a **non-happy number** (e.g., $2$), the sequence eventually repeats a previously visited value, forming a cycle:
$$2 \to 4 \to 16 \to 37 \to 58 \to 89 \to 145 \to 42 \to 20 \to 4 \dots$$

Once the sequence enters the cycle ($4 \to 16 \to 37 \to 58 \to 89 \to 145 \to 42 \to 20 \to 4$), it loops infinitely. Detecting whether the sequence reaches $1$ or enters this loop is equivalent to cycle detection.

---

## Functional Graph Interpretation

We map the transitions of the number sequence to the node transitions of a linked list:

```
Linked List:    [ Node: val ] ───────────────────────────> [ Node.next ]
                                  (Pointer dereference)

Happy Number:   [ Number: n ] ──────────────────────────> [ squareSum(n) ]
                                  (Deterministic Function)
```

The transformation $n \to \text{squareSum}(n)$ acts exactly like traversing a node's `.next` pointer.

---

## Floyd's Cycle Detection

Unlike cycle entry detection problems, this variation only requires determining if the terminal state is $1$ or a non-happy loop.

### Phase 1 — Cycle Detection

1.  Initialize both `slow` and `fast` pointers to the starting number $n$.
2.  Advance the pointers at different speeds:
    *   Move `slow` by 1 transformation step: `slow = square(slow)`.
    *   Move `fast` by 2 transformation steps: `fast = square(square(fast))`.
3.  Continue this traversal until either:
    *   `fast` reaches $1$, indicating the number is happy (returns `true`).
    *   `slow` and `fast` collide (`slow == fast`) at a value other than $1$, indicating a non-happy loop (returns `false`).

### Why Phase 2 is Unnecessary

Unlike **Linked List Cycle II** or **Find the Duplicate Number**, we do not need to identify the exact number where the cycle begins. We only need to determine if a cycle exists. If `slow` and `fast` meet at any value other than $1$, we know a cycle exists, allowing us to return `false` immediately without running a second pointer phase.

---

## Visual Walkthrough

Here is how the slow and fast pointers transition through both scenarios.

### Case 1: Happy Number Example ($n = 19$)

#### 1. Initialization
`slow` and `fast` start at $19$.
```
slow, fast
  ↓
 [19] ───> [82] ───> [68] ───> [100] ───> [1] ───> [1] (self-loop)
```

#### 2. Step 1
`slow` moves 1 step to $82$. `fast` moves 2 steps to $68$.
```
           slow     fast
             ↓        ↓
 [19] ───> [82] ───> [68] ───> [100] ───> [1] ───> [1] (self-loop)
```

#### 3. Step 3
`slow` moves 1 step to $68$. `fast` moves 2 steps to $1$.
```
                    slow              fast
                      ↓                 ↓
 [19] ───> [82] ───> [68] ───> [100] ───> [1] ───> [1] (self-loop)
```
`fast` has reached $1$. The loop terminates, returning `true`.

---

### Case 2: Non-Happy Number Example ($n = 2$)

The sequence enters an 8-node cycle ($4 \to 16 \to 37 \to 58 \to 89 \to 145 \to 42 \to 20 \to 4$). We trace the pointer movements inside this cycle:

```
Cycle Structure:
   [4] ───> [16] ───> [37] ───> [58]
    ▲                            │
    │                            ▼
   [20] <─── [42] <─── [145] <── [89]
```

At **Step 8**, both pointers collide at $20$:
```
                               slow
                               fast
                                 ↓
   [4] ───> [16] ───> [37] ───> [58]
    ▲                            │
    │                            ▼
   [20] <─── [42] <─── [145] <── [89]
```

Because `slow == fast` and the value is not $1$, the cycle is detected and the algorithm returns `false`.

---

## Mathematical Intuition

Why is the state space guaranteed to be finite? Why doesn't the sequence grow to infinity?

Let's look at the upper bound of digit square sums:
*   A 3-digit number (e.g., $999$) has a maximum square sum of $9^2 + 9^2 + 9^2 = 243$.
*   A 4-digit number (e.g., $9999$) has a maximum square sum of $4 \times 81 = 324$.
*   For any number with $d$ digits ($d \ge 4$), the number is at least $10^{d-1}$, while the maximum possible sum of squares of its digits is $81d$.

Since $10^{d-1} > 81d$ for all $d \ge 4$, any number with 4 or more digits will **strictly decrease** in value at each step. Thus, any large number is guaranteed to shrink until it falls below $243$ (a 3-digit number).

Once the sequence falls within the small, bounded range of $[1, 243]$, the Pigeonhole Principle guarantees that continuing to compute transitions must eventually cause a value to repeat. Consequently, the sequence will either reach $1$ or cycle endlessly within a small set of integers.

---

## Dry Run

Here are the complete dry run traces.

### Example 1: $n = 19$
*   Pointers initialized: `slow = 19`, `fast = 19`

| Step | `slow` Value | `fast` Value | `slow` Next | `fast` Next | Comparison / Check | Note / Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | `19` | `19` | `82` | `68` | `fast != 1` | Initialize slow and fast to 19. |
| **Step 1** | `82` | `68` | `68` | `1` | `fast != 1` | `slow` moves to 82, `fast` to 68. |
| **Step 2** | `68` | `1` | `100` | `1` | `fast == 1` | `slow` moves to 68, `fast` to 1. Loop terminates. |

**Final Result**: `True` (Happy Number)

---

### Example 2: $n = 2$
*   Pointers initialized: `slow = 2`, `fast = 2`

| Step | `slow` Value | `fast` Value | `slow` Next | `fast` Next | Comparison | Note / Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | `2` | `2` | `4` | `16` | `fast != 1` | Initialize pointers at 2. |
| **Step 1** | `4` | `16` | `16` | `58` | `slow != fast` | `slow` moves to 4, `fast` to 16. |
| **Step 2** | `16` | `58` | `37` | `145` | `slow != fast` | `slow` moves to 16, `fast` to 58. |
| **Step 3** | `37` | `145` | `58` | `20` | `slow != fast` | `slow` moves to 37, `fast` to 145. |
| **Step 4** | `58` | `20` | `89` | `37` | `slow != fast` | `slow` moves to 58, `fast` to 20. |
| **Step 5** | `89` | `37` | `145` | `89` | `slow != fast` | `slow` moves to 89, `fast` to 37. |
| **Step 6** | `145` | `89` | `42` | `145` | `slow != fast` | `slow` moves to 145, `fast` to 89. |
| **Step 7** | `42` | `145` | `20` | `20` | `slow != fast` | `slow` moves to 42, `fast` to 145. |
| **Step 8** | `20` | `20` | - | - | **`slow == fast`** | Collision detected at 20. Loop terminates. |

**Final Result**: `False` (Not a Happy Number)

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(\log n)$ | The number of digits in $n$ is $O(\log n)$. Summing the squares of digits takes $O(\log n)$ operations. A large number $n$ shrinks down to less than $243$ in $O(\log n)$ steps. Once under $243$, it takes a constant number of steps to cycle or reach $1$. Hence, the overall time is $O(\log n)$. |
| **Space Complexity** | $O(1)$ | We only maintain two integer pointers (`slow` and `fast`) to store state transitions, requiring constant extra memory. |

---

## Common Mistakes

*   ❌ **Recomputing from Original Input**: Forgetting to update pointers with their current values and instead re-applying transformations on the original $n$.
*   ❌ **Using a HashSet**: Storing values in a set to find duplicates, which takes $O(\log n)$ space and violates the $O(1)$ space requirement.
*   ❌ **Forgetting Double-Step Updates**: Forgetting that `fast` needs to move two steps in every iteration (`square(square(fast))`), causing the pointers to move at the same speed and fail to detect the loop.
*   ❌ **Attempting Phase 2**: Resetting pointers in an attempt to find the cycle entry point. Since the problem only asks *if* the number is happy, identifying the exact loop entrance is unnecessary.
*   ❌ **Confusing Happy Number with Cycle II**: Trying to run Phase 2 and returning the cycle entry value instead of returning `false`.

---

## Interview Takeaways

*   **Generalized Cycle Detection**: Demonstrates that Floyd's Cycle Detection applies to any state transition system with single-successor mapping, not just concrete linked lists.
*   **Mathematical Simplification**: Shows how bounded state spaces allow us to prove termination, changing an seemingly open-ended sequence search into a bounded cycle detection problem.
*   **Functional Graph Mapping**: Highlighting the transition $x \to f(x)$ as a directed graph path is a powerful technique for modeling mathematical problems in interviews.

---

## Pattern Connection

This problem shares the underlying **Slow & Fast Pointers** technique applied across the handbook:
*   **[Linked List Cycle (LeetCode 141)](https://leetcode.com/problems/linked-list-cycle/)**: The foundational problem of identifying loops.
*   **[Linked List Cycle II (LeetCode 142)](https://leetcode.com/problems/linked-list-cycle-ii/)**: Finding cycle entry points (requires Phase 2).
*   **[Middle of the Linked List (LeetCode 876)](https://leetcode.com/problems/middle-of-the-linked-list/)**: Uses pointer speed to find midpoints.
*   **[Find the Duplicate Number (LeetCode 287)](https://leetcode.com/problems/find-the-duplicate-number/)**: Uses array elements as next pointers to find cycle entry points.

---

## Revision Notes

A quick 30-second summary for pre-interview review:

*   **Recognition Signals**: Repeated mathematical transformations on a single variable, loop boundary detection, $O(1)$ space requirement.
*   **Core Intuition**: Modeling $n \to \text{squareSum}(n)$ as a node transition $curr \to curr.next$. Non-happy numbers will loop infinitely in a finite state space.
*   **Floyd's Algorithm**:
    *   Initialize `slow = fast = n`.
    *   Loop `while fast != 1`.
    *   Move `slow = square(slow)` and `fast = square(square(fast))`.
    *   If `slow == fast` and is not $1$, return `false`.
    *   If the loop finishes because `fast == 1`, return `true`.
*   **Complexity**: $O(\log n)$ Time, $O(1)$ Space.
