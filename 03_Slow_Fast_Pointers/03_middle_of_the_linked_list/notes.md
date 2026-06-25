<h2><a href="https://leetcode.com/problems/middle-of-the-linked-list">876. Middle of the Linked List</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

---

## Problem Overview

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, the algorithm must return the second middle node.

---

## Pattern Recognition

### Signals

When analyzing this problem, several indicators suggest the Slow & Fast Pointers pattern:
*   **Linked List**: The underlying data structure is a singly linked list.
*   **Find Middle**: The objective requires dividing the traversal or locating the exact midpoint of the structure.
*   **One Pass**: The solution should identify the target node in a single traversal of the list.
*   **$O(1)$ Space**: Memory constraints prevent storing node references or values in secondary collections.
*   **Single Traversal**: Avoiding redundant traversals to maintain efficiency.

### Why Slow & Fast Pointers?

A naive approach to finding the middle node involves counting the total number of nodes first, then traversing a second time to locate the midpoint.

<details>
<summary><b>View Two-Pass Counting Approach (Sub-optimal)</b></summary>

We traverse the entire linked list to count its total length $n$. Then, we calculate the middle index as $\lfloor n / 2 \rfloor$. We perform a second traversal starting from the head, advancing exactly $\lfloor n / 2 \rfloor$ steps to return the middle node.

```python
def middleNode_twopass(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    
    middle_idx = count // 2
    curr = head
    for _ in range(middle_idx):
        curr = curr.next
    return curr
```

*   **Time Complexity**: $O(n)$ because we perform two traversals of the list (first traversal of $n$ nodes, second traversal of $n/2$ nodes, totaling $1.5n$ operations).
*   **Space Complexity**: $O(1)$ since we only use basic counter and pointer variables.

</details>

While the two-pass approach is simple, it is sub-optimal because it requires traversing the list one and a half times. In scenarios where nodes are retrieved via expensive network calls (e.g., distributed graphs) or when processing data streams that cannot be rewound, a single-pass solution is highly preferred. 

The **Slow & Fast Pointer** approach solves this in a single pass ($n/2$ iterations), visiting each node at most once, and requiring only $O(1)$ space.

---

## Core Insight

The core insight is modeled on a running track analogy:
> If Runner A (the `slow` pointer) moves at speed $v$, and Runner B (the `fast` pointer) moves at speed $2v$:
> When Runner B crosses the finish line (reaches the end of the list), Runner A will have covered exactly half the distance, placing them at the midpoint of the track.

*   The `slow` pointer advances by **1 node** per step: `slow = slow.next`.
*   The `fast` pointer advances by **2 nodes** per step: `fast = fast.next.next`.
*   By the time `fast` reaches the end of the list (`None` or the tail node), `slow` will have traversed exactly half the list, leaving it positioned directly at the middle node.

---

## Visual Walkthrough

Here is how the slow and fast pointers traverse lists of different lengths.

### Case 1: Odd-Length List (`1 -> 2 -> 3 -> 4 -> 5`)

#### 1. Initialization
Both `slow` and `fast` start at the `head` (Node 1).
```
 slow, fast
   ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │
└───┘    └───┘    └───┘    └───┘    └───┘
```

#### 2. Step 1
`slow` moves 1 step to Node 2. `fast` moves 2 steps to Node 3.
```
          slow     fast
            ↓        ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │
└───┘    └───┘    └───┘    └───┘    └───┘
```

#### 3. Step 2
`slow` moves 1 step to Node 3. `fast` moves 2 steps to Node 5.
```
                   slow              fast
                     ↓                 ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │
└───┘    └───┘    └───┘    └───┘    └───┘
```

#### 4. Termination
In the next check, `fast.next` is `None` (since Node 5 is the tail node). The loop terminates. The `slow` pointer points at Node 3, which is the middle node.

---

### Case 2: Even-Length List (`1 -> 2 -> 3 -> 4 -> 5 -> 6`)

#### 1. Initialization
Both `slow` and `fast` start at the `head` (Node 1).
```
 slow, fast
   ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
```

#### 2. Step 1
`slow` moves 1 step to Node 2. `fast` moves 2 steps to Node 3.
```
          slow     fast
            ↓        ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
```

#### 3. Step 2
`slow` moves 1 step to Node 3. `fast` moves 2 steps to Node 5.
```
                   slow              fast
                     ↓                 ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
```

#### 4. Step 3
`slow` moves 1 step to Node 4. `fast` moves 2 steps to `None` (moving beyond the tail Node 6).
```
                            slow                       fast = None
                              ↓                             ↓
┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐    ┌───┐
│ 1 │───>│ 2 │───>│ 3 │───>│ 4 │───>│ 5 │───>│ 6 │ ───> [None]
└───┘    └───┘    └───┘    └───┘    └───┘    └───┘
```

#### 5. Termination
Now, `fast` is `None`. The loop terminates. The `slow` pointer points at Node 4.
For an even-length list of 6 nodes, the two middle nodes are 3 and 4. The algorithm naturally returns Node 4, which is the **second middle node**, satisfying the requirements.

---

## Algorithm

Here is the step-by-step description of the algorithm:

1. **Initialize** both `slow` and `fast` pointers at the `head` of the linked list.
2. **Traverse** the list using a `while` loop as long as `fast` and `fast.next` are not null:
   - Move the `slow` pointer forward by 1 step: `slow = slow.next`.
   - Move the `fast` pointer forward by 2 steps: `fast = fast.next.next`.
3. **Return** the `slow` pointer once the loop terminates (when `fast` or `fast.next` becomes null). The `slow` pointer will be referencing the middle node.

### Python Implementation

Here is the clean, production-grade Python solution matching [solution.py](file:///d:/dsa-pattern-handbook/03_Slow_Fast_Pointers/03_middle_of_the_linked_list/solution.py):

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

---

## Dry Run

Here are the detailed dry run traces for both cases.

### Example 1 (Odd Length): `1 -> 2 -> 3 -> 4 -> 5`
*   `head` = Node 1
*   Pointers initialized: `slow` = Node 1, `fast` = Node 1

| Step | `slow` Node | `fast` Node | `slow.next` | `fast.next.next` | Loop Condition (`fast` and `fast.next`) | Note / Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | `1` | `1` | `2` | `3` | Valid (both non-null) | Pointers initialized at head. |
| **Step 1** | `2` | `3` | `3` | `5` | Valid (both non-null) | `slow` moves to 2, `fast` moves to 3. |
| **Step 2** | `3` | `5` | `4` | `None` | Invalid (`fast.next` is null) | `slow` moves to 3, `fast` moves to 5. Loop terminates. |

**Final Result**: Node 3 (Middle Node) is returned.

---

### Example 2 (Even Length): `1 -> 2 -> 3 -> 4 -> 5 -> 6`
*   `head` = Node 1
*   Pointers initialized: `slow` = Node 1, `fast` = Node 1

| Step | `slow` Node | `fast` Node | `slow.next` | `fast.next.next` | Loop Condition (`fast` and `fast.next`) | Note / Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | `1` | `1` | `2` | `3` | Valid (both non-null) | Pointers initialized at head. |
| **Step 1** | `2` | `3` | `3` | `5` | Valid (both non-null) | `slow` moves to 2, `fast` moves to 3. |
| **Step 2** | `3` | `5` | `4` | `None` | Valid (both non-null) | `slow` moves to 3, `fast` moves to 5. |
| **Step 3** | `4` | `None` | - | - | Invalid (`fast` is null) | `slow` moves to 4, `fast` moves to `None`. Loop terminates. |

**Final Result**: Node 4 (Second Middle Node) is returned.

---

## Complexity Analysis

| Metric | Complexity | Explanation |
| :--- | :--- | :--- |
| **Time Complexity** | $O(n)$ | We traverse the linked list using the `fast` pointer, which moves by 2 nodes at a time. The loop runs exactly $\lfloor n/2 \rfloor$ times. Thus, we visit each node at most once, which runs in linear time. |
| **Space Complexity** | $O(1)$ | We only maintain two auxiliary pointers (`slow` and `fast`) to traverse the list, requiring constant space regardless of the list size. |

---

## Common Mistakes

*   ❌ **Forgetting the Combined Loop Condition**: Using `while fast` or `while fast.next` alone instead of `while fast and fast.next`. In even-length lists, `fast` becomes `None` at the end, and calling `fast.next` on the next iteration will raise an `AttributeError` (or `NullPointerException`). In odd-length lists, `fast.next` becomes `None` at the end, and calling `fast.next.next` will fail. Both conditions must be verified before each step.
*   ❌ **Returning the Fast Pointer**: Returning `fast` instead of `slow` at the end of the algorithm. The `fast` pointer is used to find the end of the list and will end up as `None` (for even lengths) or pointing to the tail node (for odd lengths). It is the `slow` pointer that tracks and stops at the middle.
*   ❌ **Counting Nodes First**: Implementing a two-pass counting approach. While this is $O(n)$ in time, it requires traversing the list one and a half times ($1.5n$ traversals) and is considered sub-optimal in interviews.
*   ❌ **Confusion on Even-Length Lists**: Miscalculating whether the first or second middle node is returned. Starting both pointers at `head` and advancing them together naturally returns the second middle node. Returning the first middle node would require adjusting the initial pointer positions or loop termination checks.

---

## Interview Takeaways

*   **Standard One-Pass Optimization**: Finding the middle node of a linked list in $O(1)$ auxiliary space in a single pass is the benchmark solution.
*   **Building Block for Advanced Algorithms**: This algorithm is a crucial sub-step for more complex linked list problems, such as sorting a linked list (e.g., Merge Sort on Linked Lists), checking if a linked list is a palindrome (by splitting it at the middle and reversing the second half), or reordering a list.
*   **Pointer Mechanics**: Teaches candidates how to coordinate two pointers at different speeds, which translates directly to cycle detection, sliding windows, and array optimizations.

---

## Pattern Connection

This problem shares the underlying **Slow & Fast Pointers** technique with several other classical challenges:
*   **[Linked List Cycle (LeetCode 141)](https://leetcode.com/problems/linked-list-cycle/)**: Uses the same speed-differentiated pointers to detect if a cycle exists.
*   **[Linked List Cycle II (LeetCode 142)](https://leetcode.com/problems/linked-list-cycle-ii/)**: Once a cycle is detected, we reuse the pointer coordinates to find the entry point.
*   **[Happy Number (LeetCode 202)](https://leetcode.com/problems/happy-number/)**: Uses slow and fast pointers to detect cycles in number sequences.
*   **[Find the Duplicate Number (LeetCode 287)](https://leetcode.com/problems/find-the-duplicate-number/)**: Formulates array traversal as a linked list cycle detection problem.
*   **[Palindrome Linked List (LeetCode 234)](https://leetcode.com/problems/palindrome-linked-list/)**: Uses this exact middle-finding algorithm as its first phase to locate where to split the list before reversing the second half.

---

## Revision Notes

A quick 30-second summary for pre-interview review:

*   **Recognition Signals**: Singly linked list, find middle/split point, single traversal, $O(1)$ space.
*   **Core Intuition**: Move `slow` by 1 node and `fast` by 2 nodes. When `fast` reaches the end (`None` or tail node), `slow` will cover half the distance, pointing exactly at the middle node.
*   **Algorithm**:
    ```python
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow
    ```
*   **Complexity**: $O(n)$ Time, $O(1)$ Space.
*   **Key Takeaway**: A fundamental building block for list partitioning, reordering, and palindrome checks.
