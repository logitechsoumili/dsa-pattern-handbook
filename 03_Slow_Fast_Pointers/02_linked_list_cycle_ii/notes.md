<h2><a href="https://leetcode.com/problems/linked-list-cycle-ii">142. Linked List Cycle II</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

---

## Problem Overview

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `None` (or `null`).

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (0-indexed). It is `-1` if there is no cycle. *Note that `pos` is not passed as a parameter.*

### Key Difference from Linked List Cycle (LeetCode 141)

| Problem | Goal | Return Type |
| :--- | :--- | :--- |
| **LeetCode 141: Linked List Cycle** | Determine *if* a cycle exists in the list. | `bool` (`True` / `False`) |
| **LeetCode 142: Linked List Cycle II** | Find the *exact node* where the cycle begins. | `Optional[ListNode]` (Node reference or `None`) |

---

## Pattern Recognition

### Signals

When reading a problem, look for these key indicators that suggest this pattern:
* **Linked List**: The data structure is a linked list.
* **Cycle Detection**: The problem involves checking for loops or repeated traversals.
* **Find Cycle Entry**: The goal is to locate where the loop begins.
* **Circular Traversal**: The need to traverse elements that may form a cycle.
* **$O(1)$ Space Requirement**: A constraint to solve the problem using constant auxiliary memory.

### Why Slow & Fast Pointers?

To find the cycle's starting node, we could use a brute-force approach. However, it is sub-optimal:

<details>
<summary><b>View HashSet Brute Force Approach (Sub-optimal)</b></summary>

We can traverse the linked list and keep track of visited nodes using a Hash Set. The first node we encounter that already exists in the set is the entry point of the cycle.

```python
def detectCycle_bruteforce(head: Optional[ListNode]) -> Optional[ListNode]:
    visited = set()
    curr = head
    while curr:
        if curr in visited:
            return curr
        visited.add(curr)
        curr = curr.next
    return None
```

```cpp
ListNode *detectCycle_bruteforce(ListNode *head) {
    unordered_set<ListNode*> visited;
    ListNode* curr = head;
    while (curr != nullptr) {
        if (visited.count(curr)) {
            return curr;
        }
        visited.insert(curr);
        curr = curr->next;
    }
    return nullptr;
}
```

*   **Time Complexity**: $O(n)$ because we traverse each node at most once, and Set lookup is $O(1)$ on average.
*   **Space Complexity**: $O(n)$ to store node references in the Hash Set. This violates the $O(1)$ auxiliary space constraint.

</details>

Using the **Slow & Fast Pointers** (Floyd's Cycle Detection) pattern, we can achieve $O(1)$ auxiliary space. We coordinate two pointers moving at different speeds to detect the cycle, and then use mathematical symmetry to locate the cycle's starting node.

---

## Relationship to Problem 141

This problem is a direct extension of **LeetCode 141 (Linked List Cycle)**:

1. **Phase 1 is identical**: We run Floyd's Cycle Detection algorithm using two pointers (`slow` moving 1 step, `fast` moving 2 steps).
2. **If no cycle exists**: The `fast` pointer will hit `None` (or `fast.next` will be `None`), and we return `None` immediately.
3. **If a cycle exists**: The pointers will eventually collide inside the cycle. This collision triggers **Phase 2**, which uses mathematical relationships to find the entry point.

---

## Core Insight

> [!IMPORTANT]
> The **collision point** (where `slow` and `fast` first meet) is **NOT** necessarily the cycle entry point.

Consider this linked list where a cycle starts at Node `3`, but the collision occurs at Node `5`:

```
          Cycle Entry
             ↓
1 ---> 2 ---> 3 ---> 4
              ↑      |
              |      v
              6 <--- 5  ← Collision Point
```

*   **Cycle Entry Node**: `3`
*   **Collision Node**: `5`

Because the slow and fast pointers start at the head, the fast pointer enters the cycle earlier and loops around. By the time the slow pointer enters the cycle, the fast pointer catches up and collides with it. This collision point is usually offset from the cycle entry. We must transition to a second phase to bridge this offset.

---

## Floyd's Two-Phase Algorithm

The algorithm is divided into two distinct phases:

### Phase 1 — Detect Cycle

1. Initialize both `slow` and `fast` pointers at the `head`.
2. Move `slow` by 1 step (`slow = slow.next`) and `fast` by 2 steps (`fast = fast.next.next`).
3. If `slow == fast` at any point, a cycle exists. Save this collision node and proceed to Phase 2.
4. If `fast` or `fast.next` becomes `None`, the list has no cycle; return `None`.

### Phase 2 — Find Cycle Entry

1. Keep one pointer (e.g., `ptr2`) at the collision point.
2. Place a second pointer (e.g., `ptr1`) at the `head` of the linked list.
3. Move both pointers **one step at a time** (`ptr1 = ptr1.next` and `ptr2 = ptr2.next`).
4. The node where they meet is the start of the cycle. Return this node.

---

## Python Implementation

Here is the clean, production-grade Python solution matching [solution.py](file:///d:/dsa-pattern-handbook/03_Slow_Fast_Pointers/02_linked_list_cycle_ii/solution.py):

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        # Phase 1: Cycle Detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Collision detected
            if slow == fast:
                # Phase 2: Finding the Cycle Entry
                ptr1 = head
                ptr2 = slow

                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next

                return ptr1  # Both pointers meet at the cycle entry

        return None  # No cycle detected
```

```cpp
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
            
            if (slow == fast){
                slow = head;
                while (slow != fast){
                    slow = slow->next;
                    fast = fast->next;
                }
                return slow;
            }
        }
        return NULL;
    }
};
```

---

## Visual Walkthrough

Let's visualize the process using the linked list:
`1 -> 2 -> 3 -> 4 -> 5 -> 6` where `6.next = 3`.

```
                  ┌───────────────┐
                  ▼               │
1 ───> 2 ───> 3 ───> 4 ───> 5 ───> 6
```

### Phase 1: Cycle Detection (Collision)

#### 1. Initialization
`slow` and `fast` start at `head` (Node 1).
```
 slow, fast
   ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

#### 2. Step 1
`slow` moves 1 step to Node 2. `fast` moves 2 steps to Node 3.
```
          slow     fast
            ↓        ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

#### 3. Step 2
`slow` moves 1 step to Node 3. `fast` moves 2 steps to Node 5.
```
                   slow              fast
                     ↓                 ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

#### 4. Step 3
`slow` moves 1 step to Node 4. `fast` moves 2 steps (Node 5 -> Node 6 -> Node 3).
```
          fast             slow
            ↓                ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

#### 5. Step 4
`slow` moves 1 step to Node 5. `fast` moves 2 steps (Node 3 -> Node 4 -> Node 5).
They collide at Node 5!
```
                                     slow
                                     fast
                                       ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

---

### Phase 2: Finding the Cycle Entry

#### 1. Reset `ptr1` to Head
`ptr1` goes to Node 1. `ptr2` remains at the collision node (Node 5).
```
 ptr1                                 ptr2
   ↓                                   ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

#### 2. Step 1 (Phase 2)
Both pointers move 1 step. `ptr1` moves to Node 2. `ptr2` moves to Node 6.
```
          ptr1                                ptr2
            ↓                                  ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

#### 3. Step 2 (Phase 2)
Both pointers move 1 step. `ptr1` moves to Node 3. `ptr2` loops back to Node 3.
They meet at Node 3, which is the cycle entry!
```
                   ptr1
                   ptr2
                     ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
                    ▲                          │
                    └──────────────────────────┘
```

---

## Dry Run

Here is the tabular trace of the dry run for the linked list:
`1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3` (Cycle begins at Node 3)

### Phase 1: Cycle Detection

| Step | `slow` Node | `fast` Node | `slow.next` | `fast.next.next` | Action / Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | `1` | `1` | `2` | `3` | Pointers initialized at head. |
| **1** | `2` | `3` | `3` | `5` | `slow` moves to 2, `fast` moves to 3. |
| **2** | `3` | `5` | `4` | `3` | `slow` moves to 3, `fast` moves to 5. |
| **3** | `4` | `3` | `5` | `5` | `slow` moves to 4, `fast` loops from 5 to 3. |
| **4** | `5` | `5` | - | - | **Collision Detected!** Proceed to Phase 2. |

### Phase 2: Find Cycle Entry

*   Initialize: `ptr1 = head` (Node 1), `ptr2 = slow` (Node 5).

| Step | `ptr1` Node | `ptr2` Node | Comparison | Action / Result |
| :--- | :--- | :--- | :--- | :--- |
| **Init** | `1` | `5` | `ptr1 != ptr2` | Move both pointers by 1 step. |
| **1** | `2` | `6` | `ptr1 != ptr2` | Move both pointers by 1 step. |
| **2** | `3` | `3` | `ptr1 == ptr2` | **Meeting Point Found!** Return Node 3. |

**Final Result**: Node 3 (Cycle Entry).

---

## Mathematical Intuition

Let's understand why the Phase 2 resetting of one pointer to the head works mathematically.

<details>
<summary><b>View Mathematical Derivation</b></summary>

Let's define the following variables:
*   $a$: Distance from the `head` to the cycle entry node.
*   $b$: Distance from the cycle entry node to the collision node.
*   $c$: Remaining distance from the collision node back to the cycle entry node.
*   $L$: The total length of the cycle ($L = b + c$).

```
        a (distance to entry)       b (to collision)
head ────────────────────────→ entry ───────────────→ collision
                                 ▲                       │
                                 └───────────────────────┘
                                     c (to entry)
```

#### Step 1: Write distances traveled in Phase 1
When `slow` and `fast` meet at the collision node:
*   Distance traveled by `slow`: $d_{slow} = a + b$ (since `slow` enters the cycle and collides with `fast` before completing one full lap).
*   Distance traveled by `fast`: $d_{fast} = a + b + k \cdot L$ (where $k \ge 1$ is the number of full laps `fast` made inside the cycle).

#### Step 2: Establish the relationship
Since the `fast` pointer moves twice as fast as the `slow` pointer:
$$d_{fast} = 2 \cdot d_{slow}$$

Substitute the distance expressions:
$$a + b + k \cdot L = 2 \cdot (a + b)$$

Simplify the equation:
$$a + b + k \cdot L = 2a + 2b$$
$$k \cdot L = a + b$$

#### Step 3: Solve for $a$
Since $L = b + c$, we can substitute it back:
$$a = k \cdot L - b$$
$$a = (k - 1) \cdot L + (L - b)$$
$$a = (k - 1) \cdot L + c$$

#### Conclusion
The equation $a = (k - 1) \cdot L + c$ tells us that:
The distance from the `head` to the cycle entry ($a$) is equivalent to traveling the remaining distance from the collision node to the cycle entry ($c$), plus some integer number of full cycles ($(k-1) \cdot L$).

Therefore, if we place `ptr1` at `head` and `ptr2` at the collision node, and move them both at the same speed (1 step at a time):
*   `ptr1` will travel distance $a$ to reach the cycle entry.
*   `ptr2` will travel distance $c$ plus $(k-1)$ full loops, landing at the exact same cycle entry node.
*   They will meet at the cycle entry!

</details>

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | **Phase 1**: If a cycle exists, the slow pointer takes $O(n)$ time to enter the cycle and meet the fast pointer. If no cycle exists, the fast pointer reaches the end of the list in $n/2$ steps, taking $O(n)$ time.<br>**Phase 2**: Finding the cycle entry takes $a$ steps, where $a$ is the distance from head to entry ($a \le n$), which is $O(n)$ time. |
| **Space Complexity** | $O(1)$ | We only use a constant number of auxiliary pointer references (`slow`, `fast`, `ptr1`, `ptr2`) regardless of the size of the linked list. |

---

## Common Mistakes

*   ❌ **Returning the Collision Node Directly**: Returning the node where `slow` and `fast` meet in Phase 1. As shown in the walkthrough, the collision node (Node 5) is rarely the entry node (Node 3).
*   ❌ **Forgetting to Check if Cycle Exists First**: Attempting to run Phase 2 directly without confirming a collision in Phase 1. If the list is acyclic, it will lead to errors or infinite loops.
*   ❌ **Resetting Both Pointers**: Resetting both pointers to `head` in Phase 2. Only one pointer must be reset to the `head`; the other must remain at the collision point.
*   ❌ **Moving Pointers at Different Speeds in Phase 2**: Moving `ptr1` or `ptr2` at different speeds (e.g. 2 steps) in Phase 2. Both pointers must move at exactly the same speed (1 step at a time) for the mathematical relationship $a = c + (k-1)L$ to hold.
*   ❌ **Missing the Boundary Check**: Not checking if `fast` or `fast.next` is `None` in the `while` loop. In acyclic lists, trying to access `fast.next.next` when `fast` or `fast.next` is `None` will raise a `NullPointerException` or `AttributeError`.

---

## Interview Takeaways

*   **Floyd's Algorithm Extension**: This problem is the classic extension of LeetCode 141 (Cycle Detection). It tests if you can implement and mathematically justify the second phase of the algorithm.
*   **Pointer Symmetry**: This problem demonstrates how to use the relationship between relative speeds and distance offsets to solve structural problems without using extra memory.
*   **Connection to Other Problems**:
    *   **[Linked List Cycle (LeetCode 141)](https://leetcode.com/problems/linked-list-cycle/)**: The foundational problem of detecting the existence of a cycle.
    *   **[Find the Duplicate Number (LeetCode 287)](https://leetcode.com/problems/find-the-duplicate-number/)**: Uses the exact same two-phase Floyd's algorithm.
    *   **[Happy Number (LeetCode 202)](https://leetcode.com/problems/happy-number/)**: Can detect cycle patterns in number digit square sums.

---

## Revision Notes

A quick 30-second summary for pre-interview review:

*   **Phase 1 (Detection)**: Start `slow` and `fast` at `head`. `slow` moves by 1, `fast` moves by 2. If they collide, there is a cycle. If `fast` or `fast.next` is null, there is no cycle (return `None`).
*   **Phase 2 (Entry Point)**: Reset one pointer to `head`, keep the other at the collision node. Move both 1 step at a time. The node where they meet is the cycle entry.
*   **Key Formula**: $a = c + (k - 1) \cdot L$ (distance from head to entry equals the remaining distance from collision to entry plus some number of full laps).
*   **Complexity**: $O(n)$ Time, $O(1)$ Space.
