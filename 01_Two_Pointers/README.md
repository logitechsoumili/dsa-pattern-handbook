# Two Pointers Pattern

## Overview

The Two Pointers pattern is a highly efficient algorithmic technique that uses two reference pointers (typically indices) to traverse a linear data structure (such as an array or a linked list) simultaneously. By coordinating the pointers, we can search, pair, partition, or process elements in a single pass, typically reducing time complexity from O(n^2) to O(n) and minimizing auxiliary space usage.

## Recognition Signals

Consider using this pattern when:
- The input data structure is sorted (or sorting it simplifies the problem).
- You need to find a set of elements (pairs, triplets, etc.) that satisfy a specific condition (e.g., sum, difference, or target match).
- The problem requires in-place modification of an array (e.g., partitioning, removing duplicates, segregating values).
- You need to search for combinations in linear time without checking every possible subset.

## Core Concepts

- **Opposite Ends Traversal:** One pointer starts at the beginning (index 0) and the other starts at the end (index n-1). They move toward each other based on comparison criteria.
- **Fast and Slow Traversal:** Pointers move in the same direction but at different speeds (e.g., finding the middle of a linked list or cycle detection).
- **Read and Write Boundaries:** One pointer scans the collection (read pointer) while another pointer tracks the target insertion location (write pointer).
- **Subarray Partitioning:** Pointers define distinct boundaries dividing elements into processed, unprocessed, or categorized sections.

## Template

### Opposite Ends (Two Sum variation)

```python
def opposite_ends_template(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_val = arr[left] + arr[right]
        if current_val == target:
            return [left, right]
        elif current_val < target:
            left += 1
        else:
            right -= 1
    return []
```

### Read/Write Boundary (Remove Duplicates variation)

```python
def read_write_template(arr):
    write_idx = 0
    for read_idx in range(len(arr)):
        if condition_to_write(arr[read_idx]):
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    return write_idx
```

## Common Variations

- **Inward Pointer Pairs:** Pointers starting at the extremes and moving inward (e.g., Two Sum II, 3Sum, Squares of a Sorted Array).
- **Slow/Fast Pointers (Tortoise and Hare):** One pointer moves one step at a time, the other moves two steps (commonly used in Linked Lists).
- **Multi-way Partitioning:** Three pointers that divide the array into multiple active regions (e.g., Dutch National Flag).
- **Two Arrays Merging:** Pointers traversing two separate sorted arrays simultaneously to merge them in-place (e.g., Merge Sorted Array).

## Complexity Characteristics

- **Time Complexity:** Typically O(n) because each element is visited at most a constant number of times. If sorting is required beforehand, the complexity is dominated by sorting: O(n log n).
- **Space Complexity:** Typically O(1) auxiliary space since the pointers only store integer indices or references.

## Problems Solved

| # | Problem | Key Lesson |
| - | ------- | ---------- |
| 1 | [Two Sum II](./01_two_sum) ([Notes](./01_two_sum/notes.md)) | Exploits sorted properties with inward pointers to achieve O(1) space. |
| 2 | [Segregate 0s and 1s](./02_segregate0and1) ([Notes](./02_segregate0and1/notes.md)) | Single-pass in-place partition using a write boundary pointer. |
| 3 | [Remove Duplicates](./03_remove_duplicates) ([Notes](./03_remove_duplicates/notes.md)) | Read/Write pointer comparison with predecessor in sorted arrays. |
| 4 | [Squares of a Sorted Array](./04_sortedSquares) ([Notes](./04_sortedSquares/notes.md)) | Symmetric properties of sorted array ends containing negative numbers. |
| 5 | [Merge Sorted Array](./05_mergeSortedArray) ([Notes](./05_mergeSortedArray/notes.md)) | Backward merge into empty buffer spaces to avoid overwriting. |
| 6 | [3Sum](./06_3sum) ([Notes](./06_3sum/notes.md)) | Fixing one element and reducing the problem to Two Sum on a sorted subarray. |
| 7 | [3Sum Closest](./07_3sumclosest) ([Notes](./07_3sumclosest/notes.md)) | Applying Two Sum pair search to minimize difference from a target. |
| 8 | [Triplets with Smaller Sum](./08_triplet_with_smaller_sum) ([Notes](./08_triplet_with_smaller_sum/notes.md)) | Counting sorted combinations mathematically in constant time instead of enumerating. |
| 9 | [Sort Colors](./09_sort_colors) ([Notes](./09_sort_colors/notes.md)) | Three-way partitioning (Dutch National Flag) to group elements into three regions. |
| 10 | [Move Zeroes](./10_move_zeroes) ([Notes](./10_move_zeroes/notes.md)) | Swapping non-zero elements to a write boundary while preserving order. |

## Common Mistakes

- Forgetting to sort the array before applying opposite-direction pointers.
- Incorrect boundary conditions (e.g., using `left <= right` instead of `left < right` for pair problems, which leads to using the same element twice).
- Failing to handle duplicate values, leading to duplicate combinations in the output.
- Incrementing or decrementing pointers incorrectly under specific branches (e.g., incrementing mid after swapping with high in Dutch National Flag).

## Interview Takeaways

- Look for sorted input constraints. If an array is sorted, think of Two Pointers immediately.
- Pay attention to memory constraints. Two Pointers is the preferred technique when you need to optimize space complexity from O(n) to O(1).
- Identify if the problem can be reduced to a simpler version (e.g., 3Sum to 2Sum, 4Sum to 3Sum) by fixing one pointer and scanning with the others.
