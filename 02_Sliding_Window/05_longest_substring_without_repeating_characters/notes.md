# Longest Substring Without Repeating Characters

## Problem Summary

Given a string `s`, find the length of the longest substring without repeating characters. A substring is a contiguous sequence of characters within a string.

## Brute Force Approach

Generate all possible substrings. For each substring, traverse and check if any duplicate character exists using a set. If a duplicate is found, stop expanding. Track the maximum valid substring length.

```python
def lengthOfLongestSubstring_bruteforce(s):
    max_len = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len
```

- Time Complexity: O(n^2) due to nested loops.
- Space Complexity: O(n) or O(min(n, m)) where `m` is the size of the character set (needed for duplicate tracking).

## Optimized Approach

Use a variable-size sliding window with a `left` pointer, `right` pointer, and a frequency map `freq`. Iterate `right` across the string and add `s[right]` to `freq`. Check if the window contains duplicates by comparing the current window length (`right - left + 1`) to the number of unique keys in `freq` (`len(freq)`). If the window length exceeds the count of unique keys, it means a character is duplicated. Shrink the window from the left by decrementing the count of `s[left]`, deleting the key if the count becomes 0, and incrementing `left` until all characters in the window are unique. Record the maximum window length at each step.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            window_len = right - left + 1

            while window_len > len(freq):
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
                window_len = right - left + 1

            max_len = max(max_len, right - left + 1)

        return max_len
```

- Key idea: A window has no duplicates if and only if its length equals the number of unique keys in its frequency map.
- Why it works: Shrinking the window whenever `window_length > len(freq)` guarantees that the window is brought back to a state where all characters are unique, allowing us to find the longest unique substring.

## Pattern Recognition

This problem belongs to the Variable-Size Sliding Window pattern. The goal is to maximize the window size under the constraint that no character is repeated.

## Key Observation

A duplicate character in a window creates an inequality: `window_length > len(freq)`. This mathematical inequality is a clean way to detect duplicates in a frequency-based sliding window. Alternatively, one can store the last seen index of each character to skip the left pointer directly past the duplicate.

## Complexity Analysis

### Time Complexity

O(n) because the `right` pointer scans the string once and the `left` pointer moves forward at most `n` times.

### Space Complexity

O(min(n, m)) where `n` is the length of the string and `m` is the size of the alphabet/character set. The frequency map stores at most `m` distinct characters.

## Common Mistakes

- Decrementing the frequency of a character in the map but forgetting to delete the key when its count drops to 0.
- Using a `while` statement instead of an `if` statement for checking condition, though both are technically possible depending on whether the duplicate is at the left boundary or inside. In frequency-based windowing, using `while` is robust.
- Updating the maximum length before checking and removing duplicates.
- Confusing a substring (must be contiguous) with a subsequence (does not need to be contiguous).

## Interview Notes

This is one of the most famous sliding window questions. Candidates are evaluated on their ability to manage the window boundaries, maintain unique constraints, and explain the difference between substrings and subsequences.
