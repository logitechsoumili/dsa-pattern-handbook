<h2><a href="https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1">Longest Substring with K Uniques</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Summary

Given a string `s` consisting only of lowercase alphabets and an integer `k`, find the length of the longest substring that contains exactly `k` distinct characters. If no such substring exists, return `-1`.

## Brute Force Approach

Generate all possible substrings. For each substring, use a set to track the unique characters. If the number of unique characters is exactly `k`, record the substring's length. If the unique character count exceeds `k`, stop extending that substring and move to the next starting position.

```python
def longestKSubstr_bruteforce(s, k):
    max_len = -1
    for i in range(len(s)):
        unique_chars = set()
        for j in range(i, len(s)):
            unique_chars.add(s[j])
            if len(unique_chars) == k:
                max_len = max(max_len, j - i + 1)
            elif len(unique_chars) > k:
                break
    return max_len
```

- Time Complexity: O(n^2) due to nested loops.
- Space Complexity: O(k) for the set storing at most `k + 1` unique characters.

## Optimized Approach

Use a variable-size sliding window with a `left` pointer, `right` pointer, and a frequency map `freq`. Expand the window by adding character `s[right]` to `freq`. If `len(freq)` exceeds `k`, shrink the window by decrementing the frequency of `s[left]`, deleting it from the map if its count drops to 0, and incrementing `left`. After making the window valid, if `len(freq) == k`, update the `max_len` with `right - left + 1`.

```python
class Solution:
    def longestKSubstr(self, s, k):
        left = 0
        max_len = -1
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            if len(freq) == k:
                max_len = max(max_len, right - left + 1)

        return max_len
```

- Key idea: Use a hash map to maintain the frequency of characters in the current window and dynamically size the window to satisfy the constraint.
- Why it works: We only shrink the window when the constraint is violated (`len(freq) > k`). Once the window becomes valid again, we check if it has exactly `k` uniques and update the maximum length accordingly.

## Pattern Recognition

This problem belongs to the Variable-Size Sliding Window pattern. The objective is to maximize the window length subject to the constraint of containing exactly `k` unique characters.

## Key Observation

The number of unique characters in the window is represented by `len(freq)`. We must only update our answer when `len(freq) == k` and not when `len(freq) < k`.

## Complexity Analysis

### Time Complexity

O(n) because both `left` and `right` pointers traverse the string at most once. Hash map insertions, updates, and deletions occur in O(1) average time.

### Space Complexity

O(k) auxiliary space to store character frequencies for at most `k + 1` unique characters in the map.

## Common Mistakes

- Updating `max_len` when `len(freq)` is less than `k`. The problem specifies *exactly* `k` distinct characters.
- Decrementing the character frequency in the map but forgetting to delete the key when its count reaches `0`. This leaves `len(freq)` unchanged.
- Using a shrinking condition of `len(freq) >= k` instead of `len(freq) > k`.
- Returning `0` instead of `-1` when no valid substring exists.

## Interview Notes

This problem evaluates dynamic sliding window adjustments using character hash maps/frequency tables, which is a staple pattern in string manipulation interviews.
