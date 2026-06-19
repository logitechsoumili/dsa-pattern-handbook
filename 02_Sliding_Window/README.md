# Sliding Window Pattern

## Overview

The Sliding Window pattern is a vital algorithmic technique used to perform operations on contiguous sequences of elements (subarrays, substrings, or sublists) within linear data structures. Rather than analyzing every possible subarray from scratch (which usually leads to O(n^2) or O(n^3) brute-force solutions), sliding window maintains a dynamic window boundary and updates target metrics (sums, frequencies, counts) incrementally in O(1) step time, achieving an overall O(n) runtime complexity.

## Recognition Signals

Consider using this pattern when:
- The problem involves contiguous elements of an array, list, or string (subarrays or substrings).
- You are asked to find a subarray that satisfies a specific condition (e.g., maximum sum, minimum length, longest sequence with unique characters).
- The naive solution requires nested loops, where the inner loop recalculates values that overlap heavily with the previous iteration.

## Core Concepts

- **Window State:** A set of variables (such as running sums, counters, or hash maps) that represent properties of elements currently inside the window.
- **Incremental Update:** Updating the window state in O(1) by adding the new element at the right boundary and removing the old element at the left boundary.
- **Fixed-Size Window:** The window length remains constant. The window shifts by one position in each step.
- **Variable-Size Window:** The window expands or contracts dynamically based on constraints. Typically, a right pointer expands the window, and a left pointer contracts it when the constraint is violated or satisfied.

## Template

### Fixed-Size Sliding Window

```python
def fixed_window_template(arr, k):
    if len(arr) < k:
        return 0
        
    window_val = initial_state(arr[:k])
    result = window_val
    
    for i in range(k, len(arr)):
        incoming = arr[i]
        outgoing = arr[i - k]
        window_val = update_state(window_val, incoming, outgoing)
        result = compute_optimal(result, window_val)
        
    return result
```

### Variable-Size Sliding Window (Constraint-Based)

```python
def variable_window_template(arr, constraint_val):
    left = 0
    result = initial_result()
    window_state = {}
    
    for right in range(len(arr)):
        window_state = add_to_state(window_state, arr[right])
        
        while not is_window_valid(window_state, constraint_val):
            window_state = remove_from_state(window_state, arr[left])
            left += 1
            
        result = update_result(result, left, right)
        
    return result
```

### Character Replacement Variant

The window remains valid while:
```python
windowLen - maxFreq <= k
```
- `maxFreq` represents the frequency of the most common character in the current sliding-window history.
- The remaining characters are the ones that would need replacement.
- If replacements required exceed `k`, shrink from the left until the window becomes valid again.

## Common Variations

- **Fixed-Size Window:** The window size remains exactly `k` (e.g., Max Sum Subarray of Size K).
- **Variable-Size Window (Longest Subarray):** Expand as much as possible, shrinking only when a constraint is violated, to find the maximum valid length (e.g., Longest Substring with K Uniques, Fruit Into Baskets).
- **Variable-Size Window (Minimum Subarray):** Expand until the condition is met, then shrink from the left as much as possible to find the minimum length (e.g., Minimum Size Subarray Sum).
- **Frequency Map Window:** A hash map or frequency array is used to maintain characters or elements inside the window (e.g., Longest Substring Without Repeating Characters).

## Complexity Characteristics

- **Time Complexity:** O(n) because each element enters and leaves the window at most once. Hash map operations or math updates at each step run in O(1).
- **Space Complexity:**
  - O(1) for numeric window states (like running sums).
  - O(k) or O(min(n, m)) for frequency maps, where `k` is the number of distinct elements allowed, and `m` is the alphabet/character set size.

## Problems Solved

| # | Problem | Key Lesson |
| - | ------- | ---------- |
| 1 | [Max Sum Subarray of Size K](./01_max_subarray_sum) ([Notes](./01_max_subarray_sum/notes.md)) | Incrementally update fixed-size window sums in O(1) time. |
| 2 | [Minimum Size Subarray Sum](./02_minimum_size_subarray_sum) ([Notes](./02_minimum_size_subarray_sum/notes.md)) | Shrink the window from the left immediately upon satisfying the target condition. |
| 3 | [Longest Substring with K Uniques](./03_longest_substring_with_k_uniques) ([Notes](./03_longest_substring_with_k_uniques/notes.md)) | Track window validity based on unique map size and delete keys at zero frequency. |
| 4 | [Fruit Into Baskets](./04_fruit_into_baskets) ([Notes](./04_fruit_into_baskets/notes.md)) | Map dynamic story constraints to a maximum subarray containing at most 2 distinct types. |
| 5 | [Longest Substring Without Repeating Characters](./05_longest_substring_without_repeating_characters) ([Notes](./05_longest_substring_without_repeating_characters/notes.md)) | Compare window size to map size to detect duplicate characters mathematically. |
| 6 | [Longest Repeating Character Replacement](./06_longest_repeating_character_replacement) ([Notes](./06_longest_repeating_character_replacement/notes.md)) | Use frequency counts and the formula `windowLen - maxFreq` to determine how many replacements are needed inside the current window. |

## Common Mistakes

- Recomputing the window state (e.g., using `sum(arr[i:j])`) inside the loop, which reverts the complexity to O(n * k) or O(n^2).
- Forgetting to delete elements from the frequency map when their frequency reaches `0`. If a key remains with a value of `0`, the map's size metric is incorrect.
- Using an `if` statement instead of a `while` statement when contracting a variable-size window.
- Out-of-bounds index errors when accessing `arr[i - k]`.

## Interview Takeaways

- Sliding window is the go-to technique for subsegment problems on strings or arrays when linear time O(n) is expected.
- Be clear on whether the window is fixed or variable in size.
- Pay close attention to pointer boundaries (`left` and `right`) and always ensure that map size checks accurately represent unique elements currently within the pointers.
