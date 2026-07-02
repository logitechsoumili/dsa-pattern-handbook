<h2><a href="https://leetcode.com/problems/find-the-duplicate-number">287. Find the Duplicate Number</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Overview

Given an array of integers `nums` containing $n + 1$ integers where each integer is in the range $[1, n]$ inclusive, there is only one repeated number in `nums`. The goal is to return this repeated number.

### Strict Constraints

To solve this problem, we must adhere to several strict constraints:
1.  **Read-Only Input**: We **cannot modify** the input array (e.g., sorting the array or marking elements by negating them is forbidden).
2.  **Constant Space**: We must use only **constant extra space** $O(1)$ (e.g., allocating a hash set, boolean array, or copying the array is forbidden).
3.  **Time Efficiency**: We need a solution that runs in **better than quadratic time** $O(n^2)$.

### Why Constraints Eliminate Common Approaches

*   **HashSet / visited array**: Storing elements in a set as we traverse allows us to check for duplicates in $O(n)$ time. However, this requires $O(n)$ auxiliary space, violating the constant space constraint.
*   **Sorting**: Sorting the array puts duplicates adjacent to each other, allowing a single linear check. However, in-place sorting modifies the input array. To avoid modifying it, we would have to copy the array first, taking $O(n)$ extra space, violating the space constraint.
*   **Array Marking / Negation**: Since values are between $1$ and $n$, we could use the array elements as indices and negate the values at those indices to mark them as "visited". However, this modifies the array, violating the read-only constraint.
*   **Brute Force (Nested Loops)**: Comparing every element with every other element uses $O(1)$ space and does not modify the array, but runs in $O(n^2)$ time, which violates the efficiency constraint.

---

## Pattern Recognition

### Signals

When reading this problem, look for these specific indicators that suggest the Slow & Fast Pointers pattern:
*   **Array with restricted bounds**: The array contains $n + 1$ elements, with all values strictly within $[1, n]$.
*   **Duplicate Element**: We need to find a value that is referenced multiple times.
*   **Constant Extra Space**: A strict $O(1)$ auxiliary space limit.
*   **Cannot Modify Array**: The input data must remain read-only.

### Why Slow & Fast Pointers?

Because the values in the array are strictly restricted to the range $[1, n]$ and the array has indices from $0$ to $n$, every value in the array is a valid index in the same array. 

By interpreting the array values as "next pointers" (where index $i$ points to index `nums[i]`), we can conceptualize the array as a directed graph. In this graph, each node has exactly one outgoing edge. Because there is a duplicate value, at least two different indices will point to the same value (node), meaning that node has multiple incoming edges. 

Consequently, traveling from node to node will inevitably lead us into a loop, making this problem a disguised application of **Floyd's Cycle Detection Algorithm (Linked List Cycle II)**.

---

## Core Insight

> [!IMPORTANT]
> **The array is never converted into a linked list.**

We treat the array index traversal as a state machine:
*   **Indices** represent the nodes in our graph.
*   **Values** `nums[i]` represent the transition function (or the `next` pointer) from node $i$.

Let's illustrate this with the array: `nums = [1, 3, 4, 2, 2]`

```
Indices: 0   1   2   3   4
Values:  1   3   4   2   2
```

We map the transitions starting from index `0`:
*   Start at index `0`. The next node is `nums[0] = 1`.
*   From index `1`, the next node is `nums[1] = 3`.
*   From index `3`, the next node is `nums[3] = 2`.
*   From index `2`, the next node is `nums[2] = 4`.
*   From index `4`, the next node is `nums[4] = 2`.
*   From index `2`, the next node is `nums[2] = 4` (cycle repeats).

We can visualize this transition graph:
```
0 ───> 1 ───> 3 ───> 2 <─── 4
                     │      ▲
                     └──────┘
```

Notice that both node `3` and node `4` point to node `2`. Because node `2` has multiple incoming edges (representing that the value `2` appears multiple times in the array), it acts as the entrance to the cycle. Finding the duplicate value is equivalent to finding the entry point of the cycle.

---

## Why Does a Cycle Exist?

This behavior is guaranteed by the **Pigeonhole Principle**:
1.  We have $n + 1$ nodes (indices $0$ to $n$).
2.  Each node (except possibly index 0) transitions to a value in the range $[1, n]$. This means there are $n + 1$ "pigeons" but only $n$ possible "pigeonholes" (destinations).
3.  By the Pigeonhole Principle, at least two nodes must point to the same destination value.
4.  Since index `0` is never pointed to by any value (all values are $\ge 1$), index `0` serves as the absolute entry point to our graph path. Starting at `0` guarantees we will traverse a line of nodes and enter a cycle, but we can never loop back to `0`.
5.  The node with multiple incoming edges is the duplicate value, which naturally forms the entrance to that cycle.

---

## Connection to Linked List Cycle II

Once we model the array as a transition graph, the algorithm becomes identical to **Linked List Cycle II (LeetCode 142)**. We map the pointer operations as follows:

| Singly Linked List | Array Representation |
| :--- | :--- |
| `slow = slow.next` | `slow = nums[slow]` |
| `fast = fast.next.next` | `fast = nums[nums[fast]]` |

The remainder of Floyd's Cycle Detection Algorithm remains completely unchanged.

---

## Floyd's Two-Phase Algorithm

The algorithm executes in two distinct phases:

### Phase 1 — Detect the Cycle

1.  Initialize both `slow` and `fast` pointers at index `0` (the start node).
2.  Traverse the graph:
    *   Move `slow` by 1 step: `slow = nums[slow]`.
    *   Move `fast` by 2 steps: `fast = nums[nums[fast]]`.
3.  Because a cycle is guaranteed, the pointers will eventually meet at a collision node inside the cycle (`slow == fast`). Once they collide, stop and transition to Phase 2.

### Phase 2 — Find the Cycle Entrance

1.  Reset one pointer to the start of the path: `slow = 0`. Keep the other pointer (`fast`) at the collision node.
2.  Move both pointers **one step at a time**:
    *   `slow = nums[slow]`
    *   `fast = nums[fast]`
3.  The node where they meet (`slow == fast`) is the entrance of the cycle, which represents the duplicate number. Return this value.

---

## Python & C++ Implementations

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
```

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];

        while (true){
            slow = nums[slow];
            fast = nums[nums[fast]];

            if (slow == fast){
                slow = nums[0];

                while (slow != fast){
                    slow = nums[slow];
                    fast = nums[fast];
                }
                return slow;
            }
        }
        return -1;
    }
};
```

---

## Visual Walkthrough

Using the array `nums = [1, 3, 4, 2, 2]`, we trace the pointers.

### Phase 1: Cycle Detection (Collision)

#### 1. Initialization
`slow` and `fast` start at index `0`.
```
 slow, fast
   ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

#### 2. Step 1
`slow` moves 1 step to Node 1. `fast` moves 2 steps (Node 0 -> Node 1 -> Node 3).
```
          slow             fast
            ↓                ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

#### 3. Step 2
`slow` moves 1 step to Node 3. `fast` moves 2 steps (Node 3 -> Node 2 -> Node 4).
```
                       slow              fast
                         ↓                 ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

#### 4. Step 3
`slow` moves 1 step to Node 2. `fast` moves 2 steps (Node 4 -> Node 2 -> Node 4).
```
                                 slow    fast
                                   ↓       ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

#### 5. Step 4
`slow` moves 1 step to Node 4. `fast` moves 2 steps (Node 4 -> Node 2 -> Node 4).
They collide at Node 4!
```
                                         slow
                                         fast
                                           ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

---

### Phase 2: Find Cycle Entrance

#### 1. Reset `slow` to Index 0
`slow` goes to Node 0. `fast` remains at the collision node (Node 4).
```
 slow                                fast
   ↓                                   ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

#### 2. Step 1
Both pointers move 1 step. `slow` moves to Node 1. `fast` moves to Node 2.
```
          slow                       fast
            ↓                          ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

#### 3. Step 2
Both pointers move 1 step. `slow` moves to Node 3. `fast` moves to Node 4.
```
                       slow              fast
                         ↓                 ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                             │         ▲
                             └─────────┘
```

#### 4. Step 3
Both pointers move 1 step. `slow` moves to Node 2. `fast` moves to Node 2.
They meet at Node 2, which is the cycle entry and the duplicate element.
```
                                 slow
                                 fast
                                   ↓
  [0] ───> [1] ───> [3] ───> [2] <─── [4]
                                 │         ▲
                                 └─────────┘
```

---

## Mathematical Intuition

The mathematical justification from Linked List Cycle II applies directly to this graph representation:

*   Let $a$ be the distance from the start node (index `0`) to the cycle entrance (the duplicate value).
*   Let $b$ be the distance from the cycle entrance to the collision node.
*   Let $c$ be the remaining distance from the collision node back to the cycle entrance.
*   Let $L$ be the length of the cycle ($L = b + c$).

Using the relationship that the fast pointer moves twice as fast as the slow pointer, we derive:
$$a = (k - 1) \cdot L + c$$

This formula mathematically proves that the distance from the start node to the cycle entrance ($a$) is equivalent to traveling the remaining distance from the collision node back to the entrance ($c$), plus an integer number of full laps around the cycle. 

Therefore, by resetting `slow` to `0` and keeping `fast` at the collision point, moving them both at a speed of 1 node per step ensures they will meet exactly at the cycle entrance (the duplicate value).

---

## Dry Run

Here is the trace table for the array `nums = [1, 3, 4, 2, 2]`.

### Phase 1: Cycle Detection
*   Pointers initialized: `slow = 0`, `fast = 0`

| Step | `slow` Node | `fast` Node | `nums[slow]` (slow next) | `nums[nums[fast]]` (fast next) | Comparison (`slow == fast`) | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | `0` | `0` | `1` | `3` | `slow == fast` (at init) | Initialize at index 0. |
| **1** | `1` | `3` | `3` | `4` | `slow != fast` | `slow` moves to 1, `fast` moves to 3. |
| **2** | `3` | `4` | `2` | `4` | `slow != fast` | `slow` moves to 3, `fast` moves to 4. |
| **3** | `2` | `4` | `4` | `4` | `slow != fast` | `slow` moves to 2, `fast` moves to 4 (loops back). |
| **4** | `4` | `4` | - | - | **Collision!** | Both pointers meet at Node 4. |

### Phase 2: Find Cycle Entry
*   Initialize: `slow = 0`, `fast = 4`

| Step | `slow` Node | `fast` Node | Comparison (`slow == fast`) | Action / Result |
| :--- | :--- | :--- | :--- | :--- |
| **Init** | `0` | `4` | `slow != fast` | Reset `slow` to 0. Keep `fast` at 4. |
| **1** | `1` | `2` | `slow != fast` | Move both pointers by 1 step. |
| **2** | `3` | `4` | `slow != fast` | Move both pointers by 1 step. |
| **3** | `2` | `2` | **Meeting Point Found!** | Both meet at Node 2. Return `2`. |

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | **Phase 1**: The slow pointer takes at most $n$ steps to enter the cycle and meet the fast pointer.<br>**Phase 2**: Finding the cycle entry takes at most $n$ steps. Thus, the total execution takes linear time. |
| **Space Complexity** | $O(1)$ | We only maintain two integer pointers (`slow` and `fast`) to traverse the array indices, requiring no auxiliary storage regardless of the array's size. |

---

## Common Mistakes

*   ❌ **Trying to Construct a Real Linked List**: Allocating node objects and pointers to map the array. This requires $O(n)$ auxiliary space, which violates the $O(1)$ space requirement. The array values should be accessed directly as indices.
*   ❌ **Returning the Collision Node**: Returning the index where `slow` and `fast` meet in Phase 1 (Node 4). As shown in the walkthrough, the collision node is rarely the cycle entry node.
*   ❌ **Forgetting the Offset Mapping**: Advancing pointers incorrectly (e.g. `fast = nums[fast + 1]`). The transition must strictly be `fast = nums[nums[fast]]`.
*   ❌ **Confusing Indices with Values**: Using index variables where value variables are required, or vice versa. The state variables (`slow` and `fast`) store array indices which are used to look up values.
*   ❌ **Using Set/Visited Arrays**: Allocating a hash set or boolean array to track visited values, which violates the $O(1)$ space constraint.

---

## Interview Takeaways

*   **Implicit Functional Graphs**: This problem teaches how to model arrays containing values restricted to index ranges as directed state graphs. This concept is useful in cyclic array partitioning and permutation cycles.
*   **Constraint-Driven Design**: The constraints ($O(1)$ space, read-only input, sub-quadratic time) narrow the solution space down to graph-based pointer tricks, proving that constraints can guide problem classification.
*   **Algorithmic Reduction**: Demonstrates a clean mathematical reduction of a static array problem to a classic cyclic linked list structure without modifying data.

---

## Pattern Connection

This problem uses the same **Slow & Fast Pointers** technique applied across the handbook:
*   **[Linked List Cycle (LeetCode 141)](https://leetcode.com/problems/linked-list-cycle/)**: The foundational problem of detecting cycles.
*   **[Linked List Cycle II (LeetCode 142)](https://leetcode.com/problems/linked-list-cycle-ii/)**: The exact same two-phase entry detection mechanism.
*   **[Middle of the Linked List (LeetCode 876)](https://leetcode.com/problems/middle-of-the-linked-list/)**: Uses pointer speeds to find midpoints.
*   **[Happy Number (LeetCode 202)](https://leetcode.com/problems/happy-number/)**: Uses cycles to detect loops in number sequences.

---

## Revision Notes

A quick 30-second summary for pre-interview review:

*   **Recognition Signals**: Array of size $n+1$, values within $[1, n]$, read-only constraint, $O(1)$ auxiliary space limit.
*   **Key Transformation**: Map array indices to nodes and `nums[i]` to `next` pointers. The duplicate number becomes the cycle entry point.
*   **Floyd's Algorithm**:
    *   **Phase 1**: Initialize `slow = fast = 0`. Move `slow = nums[slow]` and `fast = nums[nums[fast]]` until collision.
    *   **Phase 2**: Reset `slow = 0`. Move both pointers 1 step at a time until they meet. Return `slow`.
*   **Complexity**: $O(n)$ Time, $O(1)$ Space.
*   **Key Takeaway**: The duplicate is the start of the cycle because it is the value with multiple incoming pointers.
