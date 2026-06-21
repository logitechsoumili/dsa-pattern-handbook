<h2><a href="https://leetcode.com/problems/linked-list-cycle">Linked List Cycle</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## Problem Summary

Given `head`, the head of a singly linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Return `true` if there is a cycle, and `false` otherwise. The solution must use constant extra space.

## Brute Force Approach

### Intuition

A naive approach uses a hash set to keep track of all visited nodes. We traverse the linked list node by node. For each node, we check if it is already present in the hash set. If it is, we have detected a loop. If we reach the end of the list (`None`), there is no cycle.

### Code

```python
def hasCycle_bruteforce(head) -> bool:
    visited = set()
    curr = head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False
```

- **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list. We traverse the list once, and hash set lookups take $O(1)$ on average.
- **Space Complexity:** $O(n)$ to store each node's reference in the hash set.

## Why Brute Force is Inefficient

The brute force method requires allocating $O(n)$ auxiliary memory to store visited node references. For large linked lists or in environments with strict memory constraints, this is sub-optimal. An ideal solution should detect the cycle without using any extra tracking memory, meeting the $O(1)$ space constraint.

---

## Optimized Slow & Fast Pointers Approach

### Pattern Used

This problem belongs to the **Slow & Fast Pointers** pattern (also known as Floyd's Cycle Detection Algorithm or the "Tortoise and Hare" algorithm). Instead of tracking the nodes we have already visited, we coordinate two pointers moving through the list at different speeds.

### Core Insight

To optimize this to constant auxiliary space $O(1)$, we use two pointers (`slow` and `fast`) starting at the `head` node. The `slow` pointer advances by 1 node at each step, while the `fast` pointer advances by 2 nodes at each step. 

* **No Cycle:** The `fast` pointer will reach the end of the list (`None`) first and the algorithm terminates, returning `False`.
* **Cycle Present:** If there is a cycle, the `fast` pointer will enter the cycle first. When the `slow` pointer eventually enters the cycle, both pointers will traverse the loop indefinitely. Because the `fast` pointer gains 1 step on the `slow` pointer with each iteration, they will eventually meet.

### Key Variables Explained

1. `slow`
   A pointer initialized to `head` that advances $1$ node per step (`slow = slow.next`).
2. `fast`
   A pointer initialized to `head` that advances $2$ nodes per step (`fast = fast.next.next`).
3. **Why the relative speed difference guarantees collision:**
   Once both pointers are inside the cycle, let the distance from the `fast` pointer to the `slow` pointer (along the direction of traversal) be $D$. In each step:
   * The `slow` pointer moves 1 step forward.
   * The `fast` pointer moves 2 steps forward.
   * The distance between them decreases by exactly $2 - 1 = 1$ step.
   
   Since the gap decreases by exactly $1$ at each step, the gap will eventually reach $0$ (a collision). This mathematically guarantees that the pointers will meet, and they will do so in at most $C$ steps, where $C$ is the length of the cycle.

### Step-by-Step Algorithm

1. **Initialize** both `slow` and `fast` pointers at the `head` of the linked list.
2. **Traverse** the list using a while loop as long as `fast` and `fast.next` are not null:
   - Move the `slow` pointer forward by 1 step: `slow = slow.next`.
   - Move the `fast` pointer forward by 2 steps: `fast = fast.next.next`.
   - **Check for Collision:** If `slow == fast`, they point to the exact same node reference. A cycle exists, so return `True`.
3. **Return** `False` if the loop terminates because `fast` or `fast.next` becomes null, indicating the end of the list was reached and no cycle exists.

### Python Implementation

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

### Step-by-Step Walkthrough (Dry Run)

Let's trace the algorithm with a linked list `1 -> 2 -> 3 -> 4` where Node `4` points back to Node `1` (forming a cycle).
* `head` = Node 1
* Pointers initialized: `slow` = Node 1, `fast` = Node 1

| Step | `slow` Node | `fast` Node | `slow` Next | `fast` Next | Comparison / Validity | Note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Init** | `1` | `1` | `2` | `3` | `slow == fast` (at init) | We do not check equality before moving the pointers. |
| **Step 1** | `2` | `3` | `3` | `1` | `slow != fast` | `slow` moves to `2`, `fast` moves to `3`. |
| **Step 2** | `3` | `1` | `4` | `3` | `slow != fast` | `slow` moves to `3`, `fast` loops back to `1` (via `3.next.next`). |
| **Step 3** | `4` | `3` | `1` | `1` | `slow != fast` | `slow` moves to `4`, `fast` moves to `3` (via `1.next.next`). |
| **Step 4** | `1` | `1` | - | - | `slow == fast` | `slow` loops back to `1` (via `4.next`), `fast` loops back to `1` (via `3.next.next`). **Collision!** Returns `True`. |

**Final Result:** `True` (Cycle detected)

### Complexity Analysis

#### Time Complexity
- **$O(n)$** where $n$ is the total number of nodes in the linked list.
  - If there is no cycle, the `fast` pointer reaches the end of the list in $n/2$ steps, taking $O(n)$ time.
  - If there is a cycle, let the non-cyclic prefix have length $K$ and the cycle have length $C$ (where $K + C = n$). The `slow` pointer takes $K$ steps to reach the start of the cycle, at which point the `fast` pointer is already inside the cycle. The distance between them is at most $C$. Since the distance decreases by 1 in each step, it takes at most $C$ steps for the `fast` pointer to catch up to the `slow` pointer. The total steps taken are $K + C = n$, resulting in $O(n)$ time.

#### Space Complexity
- **$O(1)$** auxiliary space because we only maintain two pointer references (`slow` and `fast`) to traverse the list, requiring constant memory regardless of the size of the list.

---

## Common Mistakes

- **Checking Pointers Before Moving:** Comparing `slow == fast` at the very beginning of the loop. Because both pointers are initialized to `head`, checking equality immediately will result in a false positive, returning `True` for any valid linked list.
- **Forgetting Boundary Checks:** Failing to check if `fast` and `fast.next` are valid before advancing. Since `fast` moves by two steps (`fast.next.next`), calling this on a list without a cycle will throw an `AttributeError` (or `NullPointerException`) when `fast` or `fast.next` is null.
- **Comparing Values Instead of Nodes:** Checking `slow.val == fast.val` rather than comparing node identity references `slow == fast`. Since linked lists can contain duplicate values in different nodes, value-based comparison leads to false positives.
- **Using a HashSet:** Storing visited nodes in a set is a common sub-optimal approach. While it is $O(n)$ in time, it uses $O(n)$ space, failing the constant space requirement of the problem.

---

## Key Takeaways

- **The Tortoise and Hare Strategy:** Coordinating two pointers at different speeds is the standard approach for detecting cycles, finding loops, or identifying periodic sequences without caching history.
- **Relative Speed Difference:** When one pointer moves 1 step and the other moves 2 steps, the distance between them decreases by exactly 1 in each step. This guarantees that they will eventually meet within a cycle of length $C$ in at most $C$ steps, avoiding infinite loops.
- **Connection to Other Problems:**
  - **[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)**: Once a collision is detected, resetting `slow` to `head` and moving both `slow` and `fast` at the same speed (1 step at a time) will cause them to meet at the start node of the cycle.
  - **[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)**: Moving the fast pointer twice as fast as the slow pointer means that when `fast` reaches the end of the list, `slow` will be exactly at the middle node.
  - **[Happy Number](https://leetcode.com/problems/happy-number/)**: Finding if a number is happy can be modeled as cycle detection on a sequence of sum-of-squares of digits.
  - **[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)**: An array of numbers where indices map to values can be modeled as a linked list with a cycle. We can find the duplicate value (cycle entrance) using Floyd's algorithm.
