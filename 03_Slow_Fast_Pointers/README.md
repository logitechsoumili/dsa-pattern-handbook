# Slow & Fast Pointers Pattern

## Overview

The Slow & Fast Pointers pattern (also known as Floyd's Cycle Detection Algorithm or the "Tortoise and Hare" algorithm) is a pointer-based traversal technique used to analyze sequential structures, linked lists, and state machines. By moving two pointers at different speeds (typically one moving at speed 1 and the other at speed 2), we can uncover hidden structural properties, detect circular dependencies, find loops, or locate middle nodes. Although frequently introduced in the context of linked list traversal, this pattern is general and applies to any state transition system, mathematical sequence, or functional graph where elements point to a single successor.

---

## Recognition Signals

Consider using this pattern when:
- The problem involves traversing a singly linked list or a directed graph where each node has a single outgoing edge.
- You need to detect a cycle or loop in a list, number sequence, or state machine.
- You need to find the entry point (start node) of a cycle.
- You need to find the middle node or split a linked list into two halves.
- The problem involves repeated, deterministic transformations of an input value.
- You are constrained to $O(1)$ extra space and cannot use a hash set or tracking array to remember visited states.
- The sequence is guaranteed to either terminate or repeat a previous state (infinite loops or repeated states).

---

## Core Concepts

- **Slow Pointer**: A pointer initialized to the start of the structure that advances by exactly 1 step per iteration (`slow = slow.next` or `slow = next_state(slow)`).
- **Fast Pointer**: A pointer initialized to the start of the structure that advances by exactly 2 steps per iteration (`fast = fast.next.next` or `fast = next_state(next_state(fast))`).
- **Relative Speed**: The difference in pointer speeds. Since the fast pointer advances by 2 steps while the slow pointer advances by 1, the relative distance between them decreases by exactly 1 step in each iteration once both pointers enter a cycle.
- **Collision Point**: The specific node or state where both pointers meet. A collision mathematically guarantees the existence of a cycle.
- **Cycle Detection**: The process of identifying whether a sequence of nodes or states repeats endlessly.
- **Cycle Entry**: The first node where the cycle begins. Finding this node requires resetting one pointer to the start of the path and advancing both pointers at the same speed.
- **Functional Graph**: A directed graph where every node has exactly one outgoing edge, meaning each state transitions to a single, deterministic next state.
- **State Transition**: A rule or function that defines the next state given the current state.

---

## Floyd's Cycle Detection Algorithm

The algorithm operates in two phases:

### Phase 1 — Detect Cycle

Initialize both `slow` and `fast` pointers at the start node. Advance `slow` by 1 step and `fast` by 2 steps at each iteration. If `fast` or its successor reaches null, the sequence terminates and no cycle exists. If `slow == fast` at any point, a cycle is detected, and the pointers collide.

### Phase 2 — Find Cycle Entry

Reset one pointer (e.g., `slow`) to the start node of the path while keeping the other pointer (`fast`) at the collision point. Move both pointers one step at a time. The node where they meet is the start of the cycle. Note that this phase is only required when the problem asks for the starting point of the cycle.

---

## Pattern Templates

### Linked List Cycle Detection

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

```cpp
bool has_cycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true;
        }
    }
    return false;
}
```

### Find Cycle Entry

```python
def detect_cycle_entry(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Phase 2: Find cycle entry
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

```cpp
ListNode* detect_cycle_entry(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            // Phase 2: Find cycle entry
            slow = head;
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
    }
    return nullptr;
}
```

### Functional Graph Variant

```python
def functional_graph_cycle(x0, next_state):
    slow = fast = x0
    while True:
        slow = next_state(slow)
        fast = next_state(next_state(fast))
        if slow == fast:
            # Match condition for cycle detection or entry
            return slow
```

```cpp
template <typename T, typename F>
T functional_graph_cycle(T x0, F next_state) {
    T slow = x0;
    T fast = x0;
    while (true) {
        slow = next_state(slow);
        fast = next_state(next_state(fast));
        if (slow == fast) {
            // Match condition for cycle detection or entry
            return slow;
        }
    }
}
```

---

## Functional Graph Interpretation

Not every Slow & Fast Pointer problem involves an actual linked list. 

*   **Happy Number** forms a sequence of states based on digit square sums, where each number transitions to a single successor.
*   **Find the Duplicate Number** treats array indices as nodes, and `nums[i]` as the transition to the next node.

These relationships can be visualized as implicit graphs:

#### Happy Number State transitions (starting at 2)
```
[Number: 2] ───> [4] ───> [16] ───> [37] ───> [58]
                  ▲                            │
                  │                            ▼
                 [20] <─── [42] <─── [145] <── [89]
```

#### Find the Duplicate Number index transitions (array: [1, 3, 4, 2, 2])
```
[Index 0] ───> [Index 1] ───> [Index 3] ───> [Index 2] <─── [Index 4]
                                               │              ▲
                                               └──────────────┘
```

---

## Common Variations

- **Linked List Cycle Detection**: Determines if a cycle exists (e.g., Linked List Cycle). Terminates when the fast pointer reaches null or collides with slow.
- **Find Cycle Entry**: Locates the start node of the cycle (e.g., Linked List Cycle II). Resets one pointer to the head after collision, moving both at speed 1 until they meet.
- **Middle of Linked List**: Finds the exact middle node of a list (e.g., Middle of the Linked List). When the fast pointer reaches the end, the slow pointer points at the middle.
- **Functional Graph Cycle Detection**: Detects cycles in mathematical operations or value transformations (e.g., Happy Number). Uses function applications instead of pointer dereferences.
- **Functional Graph Cycle Entry**: Locates the duplicate in a bounded array (e.g., Find the Duplicate Number) by finding the cycle entrance of index transitions.

---

## Complexity Characteristics

- **Time Complexity**: $O(n)$ because each element or state is visited at most a constant number of times. In any cycle of length $C$ with a prefix path of length $K$, the pointers will collide in at most $K + C \le n$ iterations.
- **Space Complexity**: $O(1)$ auxiliary space. Unlike hash-set solutions that store visited nodes or elements, the Slow & Fast Pointer pattern only maintains two state variables (the pointers), requiring constant memory.

---

## Problems Solved

| # | Problem | Key Lesson |
| - | ------- | ---------- |
| 1 | [Linked List Cycle](./01_linked_list_cycle) ([Notes](./01_linked_list_cycle/notes.md)) | Detect a cycle using Floyd's algorithm. |
| 2 | [Linked List Cycle II](./02_linked_list_cycle_ii) ([Notes](./02_linked_list_cycle_ii/notes.md)) | Extend Floyd's algorithm to locate the cycle entry. |
| 3 | [Middle of the Linked List](./03_middle_of_the_linked_list) ([Notes](./03_middle_of_the_linked_list/notes.md)) | Different pointer speeds naturally locate the middle node. |
| 4 | [Find the Duplicate Number](./04_find_the_duplicate_number) ([Notes](./04_find_the_duplicate_number/notes.md)) | Model an array as a functional graph and apply Floyd's algorithm. |
| 5 | [Happy Number](./05_happy_number) ([Notes](./05_happy_number/notes.md)) | Treat repeated digit-square transformations as state transitions forming a cycle. |

---

## Advanced Slow & Fast Pointer Applications

The pattern extends beyond linked lists.
*   **Functional Graphs**: Permutations and mathematical transformations can be represented as states where each element has exactly one successor.
*   **State Machines**: Complex transitions can be traced with pointers to identify infinite loops or repeating patterns.
*   **Repeated Deterministic Transformations**: Operations like base transformations, checksums, or modular sequences can form graphs that contain loops.

Recognizing these hidden graph structures is a crucial interview skill. Many problems present themselves as array manipulation or mathematical tasks, but their constraints (such as read-only arrays, constant space, or detection of repeating patterns) make traditional approaches impossible. Recognizing that these problems can be modeled as state transitions on a functional graph allows candidates to apply Floyd's cycle detection algorithm directly. This structural transformation demonstrates graph theory abstraction and optimization.

---

## Common Mistakes

- **Comparing Pointers Before the First Movement**: Checking `slow == fast` at the beginning of Phase 1. Since both are initialized to the start, checking immediately causes a false collision.
- **Forgetting Boundary Checks**: Failing to verify `fast` and `fast.next` are not null before moving the fast pointer (`fast = fast.next.next`), leading to runtime crashes on acyclic lists.
- **Returning the Collision Point Instead of the Cycle Entry**: Confusing the meeting point in Phase 1 with the start of the cycle.
- **Thinking Every Problem Requires Phase 2**: Unnecessarily resetting pointers to find the cycle entrance (e.g. in Happy Number), when only cycle existence is required.
- **Recomputing Transitions from the Original State**: Re-applying transitions to the initial input instead of moving pointers forward from their current states.
- **Thinking a Real Linked List Must Be Constructed**: Unnecessarily allocating list node objects or structure mappings for functional graph problems (like Happy Number or Duplicate Number), violating space and time constraints.

---

## Interview Takeaways

- **Recognize Hidden Cycles**: Look for deterministic transitions where inputs map to a finite range of outputs.
- **Think in Transitions**: Model states as nodes and mapping functions as pointer dereferences.
- **Floyd's Algorithm is Versatile**: It is a mathematical cycle detection mechanism that applies to digit manipulation, arrays, and permutations.
- **Focus on Pattern Identification**: The code implementations are short and easy to write. The real challenge is mapping the problem constraints to the Tortoise and Hare pattern.
