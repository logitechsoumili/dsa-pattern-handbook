<h2><a href="https://leetcode.com/problems/longest-repeating-character-replacement/">Longest Repeating Character Replacement</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Statement

You are given a string `s` consisting of uppercase English letters and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Example

**Input:** `s = "ABAB", k = 2`  
**Output:** `4`  
**Explanation:** Replace the two 'A's with 'B's or vice versa to get "BBBB" or "AAAA", both of which have length 4.

**Input:** `s = "AABABBA", k = 1`  
**Output:** `4`  
**Explanation:** Replace the middle 'A' with 'B' to form "AABBBBA". The substring "BBBB" has the longest repeating character, which is 4.

## Brute Force Approach

### Intuition

A brute force solution checks all possible substrings. For each substring, we count the frequency of each character. To minimize the number of replacements needed to make all characters in the substring identical, we should keep the most frequent character and replace all other characters. 

The number of replacements needed is the length of the substring minus the frequency of the most frequent character. If this number is less than or equal to `k`, the substring is valid. We track the maximum length of any valid substring.

### Algorithm

1. Iterate over all possible starting indices `i` from `0` to `len(s) - 1`.
2. For each `i`, iterate over all possible ending indices `j` from `i` to `len(s) - 1`.
3. For each substring `s[i:j+1]`:
   - Calculate the frequency of each character inside the substring.
   - Find the maximum frequency (`max_freq`) of any character in the substring.
   - Check if `(j - i + 1) - max_freq <= k`.
   - If valid, update `max_len = max(max_len, j - i + 1)`.
4. Return `max_len`.

```python
def characterReplacement_bruteforce(s: str, k: int) -> int:
    max_len = 0
    for i in range(len(s)):
        freq = {}
        max_freq = 0
        for j in range(i, len(s)):
            char = s[j]
            freq[char] = freq.get(char, 0) + 1
            max_freq = max(max_freq, freq[char])
            
            if (j - i + 1) - max_freq <= k:
                max_len = max(max_len, j - i + 1)
    return max_len
```

```cpp
int characterReplacement_bruteforce(string s, int k) {
    int maxLen = 0;
    for (int i = 0; i < s.size(); i++) {
        unordered_map<char, int> freq;
        int maxFreq = 0;
        for (int j = i; j < s.size(); j++) {
            freq[s[j]]++;
            maxFreq = max(maxFreq, freq[s[j]]);
            if ((j - i + 1) - maxFreq <= k) {
                maxLen = max(maxLen, j - i + 1);
            }
        }
    }
    return maxLen;
}
```

- Time Complexity: O(n^2) because we use nested loops to inspect all possible substrings.
- Space Complexity: O(1) auxiliary space (or O(26) = O(1)) because the frequency map stores at most 26 uppercase English letters.

## Optimized Approach (Sliding Window)

### Pattern Used

This problem is solved using the **Variable-Size Sliding Window** pattern. We expand the window using a `right` pointer to include new characters and shrink it from the `left` when the window condition is violated.

### Key Observation

To make all characters in a substring identical using at most `k` replacements, we must always choose to keep the character that appears most frequently in that substring. Replacing all other characters to match this most frequent character requires the minimum number of replacements.

### Why `windowLen - maxFreq` represents replacements needed

Let the current window be represented by indices `[left, right]`.
- The length of the window is `windowLen = right - left + 1`.
- Let `maxFreq` be the frequency of the most common character within this window.
- If we decide to convert all characters in the window to this most common character, we must replace all other characters.
- The number of other characters is:
  $$\text{Replacements Needed} = \text{windowLen} - \text{maxFreq}$$

For example, in the window `"AABAB"`:
- `'A'` appears 3 times.
- `'B'` appears 2 times.
- The most frequent character is `'A'` with `maxFreq = 3`.
- `windowLen = 5`.
- Replacements needed = `5 - 3 = 2` (we need to change the two `'B'`s to `'A'`).

### Window Validity Condition

The window is valid if and only if the number of replacements needed does not exceed `k`:
$$\text{windowLen} - \text{maxFreq} \le k$$

### Detailed Sliding Window Logic

We maintain:
1. A `left` pointer to track the start of the window.
2. A `right` pointer to expand the window.
3. A frequency map `freq` to count the characters in the current window.
4. A variable `maxFreq` to track the maximum frequency of any character encountered.

#### Why do we keep track of `maxFreq`?
We track `maxFreq` to dynamically determine the maximum number of matching characters currently in our window. This allows us to calculate how many replacements are needed in O(1) time without scanning the frequency map.

#### Why does `maxFreq` only increase and is never decreased?
An important optimization is that **we do not need to decrement `maxFreq` when we shrink the window** (i.e., when `left` shifts to the right and a character is removed).
- We are looking for the *maximum* length of a valid window.
- A larger valid window can only be found if we encounter a character with a frequency higher than our historical maximum frequency (`maxFreq`).
- If we decrease `maxFreq`, it only makes the expression `windowLen - maxFreq` larger, which makes the window *less* likely to be valid. Decreasing `maxFreq` cannot help us find a window size larger than what we have already recorded.
- Thus, `maxFreq` acts as a "high-water mark" of the most frequent character seen so far. It only updates when a frequency exceeds the current `maxFreq`.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        freq = {}
        maxFreq = 0

        for right in range(len(s)):
            # Include s[right] in the window frequency map
            freq[s[right]] = freq.get(s[right], 0) + 1
            # Update the historical maximum frequency
            maxFreq = max(maxFreq, freq[s[right]])
            
            # If the replacements needed exceed k, shrink the window
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # Update the maximum valid window length found so far
            maxLen = max(maxLen, right - left + 1)

        return maxLen
```

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> freq;
        int maxFreq = 0, left = 0, maxLen = 0;

        for (int right = 0; right < s.size(); right++){
            freq[s[right]]++;
            maxFreq = max(maxFreq, freq[s[right]]);

            while ((right - left + 1) - maxFreq > k){
                freq[s[left]]--;
                left++;
            }

            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};
```

### Step-by-Step Walkthrough

Let's trace the algorithm with `s = "AABABBA"` and `k = 1`.

| Step | `right` | `s[right]` | `freq` Map | `maxFreq` | Window (`s[left:right+1]`) | `windowLen - maxFreq` | Action / Validity | `maxLen` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 'A' | `{'A': 1}` | 1 | `"A"` | `1 - 1 = 0 <= 1` | Valid. Update `maxLen`. | 1 |
| 2 | 1 | 'A' | `{'A': 2}` | 2 | `"AA"` | `2 - 2 = 0 <= 1` | Valid. Update `maxLen`. | 2 |
| 3 | 2 | 'B' | `{'A': 2, 'B': 1}` | 2 | `"AAB"` | `3 - 2 = 1 <= 1` | Valid. Update `maxLen`. | 3 |
| 4 | 3 | 'A' | `{'A': 3, 'B': 1}` | 3 | `"AABA"` | `4 - 3 = 1 <= 1` | Valid. Update `maxLen`. | 4 |
| 5 | 4 | 'B' | `{'A': 3, 'B': 2}` | 3 | `"AABAB"` | `5 - 3 = 2 > 1` | **Invalid**. Shrink from left. `left` becomes 1. | 4 |
| | | | `{'A': 2, 'B': 2}` | 3 | `"ABAB"` | `4 - 3 = 1 <= 1` | Validated after shrinking. | 4 |
| 6 | 5 | 'B' | `{'A': 2, 'B': 3}` | 3 | `"ABABB"` | `5 - 3 = 2 > 1` | **Invalid**. Shrink from left. `left` becomes 2. | 4 |
| | | | `{'A': 1, 'B': 3}` | 3 | `"BABB"` | `4 - 3 = 1 <= 1` | Validated after shrinking. | 4 |
| 7 | 6 | 'A' | `{'A': 2, 'B': 3}` | 3 | `"BABBA"` | `5 - 3 = 2 > 1` | **Invalid**. Shrink from left. `left` becomes 3. | 4 |
| | | | `{'A': 1, 'B': 3}` | 3 | `"ABBA"` | `4 - 3 = 1 <= 1` | Validated after shrinking. | 4 |

**Final Output:** `maxLen = 4`

### Complexity Analysis

#### Time Complexity

- **O(n)** because the `right` pointer iterates through the string of length `n` exactly once, and the `left` pointer only moves forward, visiting each index at most once. Frequency map updates and checks run in O(1) time.

#### Space Complexity

- **O(1)** because the frequency map `freq` stores at most 26 key-value pairs (for uppercase English letters), requiring constant auxiliary space.

## Common Mistakes

- **Recalculating `maxFreq` on shrink:** Attempting to scan the entire frequency map to decrement or find the new maximum frequency when a character is removed from the window. While this still runs in O(26) = O(1) time, it is conceptually redundant.
- **Incorrect validity checks:** Checking against `freq[s[right]]` instead of the historical `maxFreq`. The character at `right` might not be the most frequent character in the current window.
- **Off-by-one errors:** Calculating window size using `right - left` instead of `right - left + 1`.

## Key Takeaways

- **High-Water Mark Optimization:** This problem illustrates a powerful technique: we only care about finding a window larger than our current maximum. Hence, our criteria for window validity can rely on a historical maximum (`maxFreq`) that is never decreased.
- **Complementary Thinking:** Instead of asking "which characters should we change?", ask "how many characters do we not have to change?". A window of length $L$ can be made uniform with at most $k$ changes if the count of its most frequent character is at least $L - k$.
