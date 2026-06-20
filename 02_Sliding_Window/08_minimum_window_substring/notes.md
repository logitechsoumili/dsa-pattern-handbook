<h2><a href="https://leetcode.com/problems/minimum-window-substring">Minimum Window Substring</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />

## Problem Summary

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

A **substring** is a contiguous sequence of characters within a string.

## Brute Force Approach

### Intuition

A naive approach checks every possible substring of `s`. For each substring, we check if it contains all the characters of `t` with their required frequencies. 

### Code

```python
from collections import Counter

def minWindow_bruteforce(s: str, t: str) -> str:
    if not s or not t:
        return ""
        
    t_count = Counter(t)
    min_len = float('inf')
    res = ""
    
    # Generate all possible substrings s[i:j+1]
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            sub_count = Counter(sub)
            
            # Verify if the substring contains all required characters of t
            is_valid = True
            for char, count in t_count.items():
                if sub_count[char] < count:
                    is_valid = False
                    break
            
            # If valid, check if it's the minimum window
            if is_valid:
                if len(sub) < min_len:
                    min_len = len(sub)
                    res = sub
    return res
```

- **Time Complexity:** $O(m^3)$ where $m$ is the length of `s`. There are $O(m^2)$ possible substrings, and verifying each substring takes $O(m)$ time to count character frequencies.
- **Space Complexity:** $O(m + n)$ to store counts of characters in the substring and string `t`.

## Why Brute Force is Inefficient

The brute force method recalculates the character counts for overlapping substrings from scratch. For instance, when analyzing `s[i:j]` and then `s[i:j+1]`, it re-scans all characters from index `i` to `j`. With string lengths up to $10^5$, an $O(m^3)$ algorithm is far too slow and will result in a Time Limit Exceeded (TLE) error.

---

## Optimized Sliding Window Approach

### Pattern Used

This problem belongs to the **Variable-Size Sliding Window** pattern. Specifically, it is a **Minimum Window Subarray** variant. Instead of trying to find the longest window that satisfies a condition, we expand our window to find a valid one, and then contract it from the left as much as possible to locate the smallest possible valid window.

### Core Insight

To optimize this to linear time $O(m + n)$, we use two pointers (`left` and `right`) to maintain a sliding window. 

However, checking if the window contains all characters in `t` by comparing the two frequency maps directly at each step would take $O(\Sigma)$ time, where $\Sigma$ is the alphabet size. To make the validation step $O(1)$, we track how many unique characters have met their required counts.

### Key Variables Explained

1. `need = Counter(t)`
   A frequency map storing the required counts for each unique character in `t`.
2. `window = Counter()`
   A frequency map tracking the counts of characters currently inside the active sliding window.
3. `formed`
   An integer tracking how many unique characters from `t` have met their required frequency count in the current window.
4. `required = len(need)`
   The total number of unique characters in `t` that must be satisfied.
5. **Why `formed == required` means the window is valid:**
   Since `required` represents the count of unique characters in `t`, and `formed` represents how many of those unique characters have been fully matched inside our window, the equation `formed == required` guarantees that every character from `t` is present in the current window with at least its required frequency.

### Frequency Matching Mechanics

#### 1. Why `window[ch] == need[ch]` is used to increase `formed`
As the `right` pointer expands the window, the count of `ch` in `window` increases. We only want to increment `formed` **exactly once** when the frequency requirement for `ch` is met. 
* If we used `window[ch] >= need[ch]`, we would increment `formed` multiple times as `window[ch]` continues to grow past the required count. This would incorrectly inflate `formed`.
* By checking for exact equality `window[ch] == need[ch]`, we guarantee that `formed` is incremented only at the exact moment the character's requirement is satisfied.

#### 2. Why `window[ch] < need[ch]` is used to decrease `formed` during shrinking
As the `left` pointer contracts the window, we remove characters. If we remove a character `ch` whose count in `window` was higher than needed (due to duplicate/excess characters in the window), the window remains valid for `ch`. 
* We should only decrement `formed` when the frequency of `ch` falls **strictly below** what is required.
* Thus, we check if `window[ch] < need[ch]` after decrementing. If it is, this character's requirement is no longer met, and we must decrement `formed`.

### Step-by-Step Algorithm

1. **Initialize** `left = 0`, `formed = 0`, `minLen = float('inf')`, and `res = ""`.
2. **Count requirements** by setting `need = Counter(t)` and initialize an empty `window = Counter()`.
3. **Expand** the window by moving `right` from `0` to `len(s) - 1`:
   - Retrieve the current character `s[right]` and increment its count in `window`.
   - If `s[right]` is in `need` and its count in `window` equals its count in `need`, increment `formed`.
4. **Contract** the window from the left while `formed == len(need)` (the window is valid):
   - Update `minLen` and `res` if the current window `right - left + 1` is smaller than `minLen`.
   - Retrieve the left character `s[left]` and decrement its count in `window`.
   - If `s[left]` is in `need` and its count in `window` falls below its count in `need`, decrement `formed`.
   - Increment `left` by 1 to shrink the window.
5. **Return** the minimum window substring `res`.

### Python Implementation

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = formed = 0
        minLen = float('inf')
        res = ''
        need = Counter(t)
        window = Counter()

        for right in range(len(s)):
            # Expand the window: Include s[right]
            char = s[right]
            window[char] += 1
            
            # If the current character's frequency matches the required frequency,
            # we have satisfied the requirement for this unique character.
            if char in need and window[char] == need[char]:
                formed += 1

            # Contract the window as long as it remains valid
            while formed == len(need):
                # Update the smallest valid window found so far
                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    res = s[left:right+1]

                # Remove the character at the left boundary from the window
                left_char = s[left]
                window[left_char] -= 1
                
                # If the leaving character is part of t and its frequency falls 
                # below the required count, this character requirement is no longer met.
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                
                left += 1

        return res
```

### Step-by-Step Walkthrough (Dry Run)

Let's trace the algorithm with `s = "ADOBECODEBANC"` and `t = "ABC"`.
* `need = {'A': 1, 'B': 1, 'C': 1}`
* `required = len(need) = 3`

| Step | `right` | `s[right]` | `window` State | `formed` | Action / Validity | Window `s[left:right+1]` | `minLen` / `res` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | 'A' | `{'A': 1}` | 1 | `window['A'] == need['A']` -> `formed = 1`. Invalid (`formed < 3`). | `"A"` | `inf` / `""` |
| 2 | 1 | 'D' | `{'A': 1, 'D': 1}` | 1 | Invalid (`formed < 3`). | `"AD"` | `inf` / `""` |
| 3 | 2 | 'O' | `{'A': 1, 'D': 1, 'O': 1}` | 1 | Invalid (`formed < 3`). | `"ADO"` | `inf` / `""` |
| 4 | 3 | 'B' | `{'A': 1, 'D': 1, 'O': 1, 'B': 1}` | 2 | `window['B'] == need['B']` -> `formed = 2`. Invalid. | `"ADOB"` | `inf` / `""` |
| 5 | 4 | 'E' | `{'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1}` | 2 | Invalid. | `"ADOBE"` | `inf` / `""` |
| 6 | 5 | 'C' | `{'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1, 'C': 1}` | 3 | `window['C'] == need['C']` -> `formed = 3`. **Valid** (`3 == 3`). | `"ADOBEC"` | `inf` / `""` |
| | | | **Shrink Loop** (while `formed == 3`): | | | | |
| | | | - Update res: `minLen = 6`, `res = "ADOBEC"` | 3 | Update match. | `"ADOBEC"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'A'`. `window['A']` becomes 0. | 3 | | | |
| | | | - Since `window['A'] < need['A']` (0 < 1), decrement `formed` to 2. | 2 | | | |
| | | | - Increment `left` to 1. **Invalid** (`formed < 3`). | 2 | Loop terminates. | `"DOBEC"` | `6` / `"ADOBEC"` |
| 7 | 6 | 'O' | `{'A': 0, 'D': 1, 'O': 2, 'B': 1, 'E': 1, 'C': 1}` | 2 | Invalid. | `"DOBECO"` | `6` / `"ADOBEC"` |
| 8 | 7 | 'D' | `{'A': 0, 'D': 2, 'O': 2, 'B': 1, 'E': 1, 'C': 1}` | 2 | Invalid. | `"DOBECOD"` | `6` / `"ADOBEC"` |
| 9 | 8 | 'E' | `{'A': 0, 'D': 2, 'O': 2, 'B': 1, 'E': 2, 'C': 1}` | 2 | Invalid. | `"DOBECODE"` | `6` / `"ADOBEC"` |
| 10 | 9 | 'B' | `{'A': 0, 'D': 2, 'O': 2, 'B': 2, 'E': 2, 'C': 1}` | 2 | `window['B']` count is 2 (not exact match). Invalid. | `"DOBECODEB"` | `6` / `"ADOBEC"` |
| 11 | 10 | 'A' | `{'A': 1, 'D': 2, 'O': 2, 'B': 2, 'E': 2, 'C': 1}` | 3 | `window['A'] == need['A']` -> `formed = 3`. **Valid**. | `"DOBECODEBA"` | `6` / `"ADOBEC"` |
| | | | **Shrink Loop** (while `formed == 3`): | | | | |
| | | | - Current length 10 is not < 6. No update. | 3 | | `"DOBECODEBA"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'D'`. `window['D'] = 1 >= need['D']`. | 3 | `left` becomes 2. | `"OBECODEBA"` | `6` / `"ADOBEC"` |
| | | | - Current length 9 is not < 6. No update. | 3 | | `"OBECODEBA"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'O'`. `window['O'] = 1 >= need['O']`. | 3 | `left` becomes 3. | `"BECODEBA"` | `6` / `"ADOBEC"` |
| | | | - Current length 8 is not < 6. No update. | 3 | | `"BECODEBA"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'B'`. `window['B'] = 1 >= need['B']`. | 3 | `left` becomes 4. | `"ECODEBA"` | `6` / `"ADOBEC"` |
| | | | - Current length 7 is not < 6. No update. | 3 | | `"ECODEBA"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'E'`. `window['E'] = 1 >= need['E']`. | 3 | `left` becomes 5. | `"CODEBA"` | `6` / `"ADOBEC"` |
| | | | - Current length 6 is not < 6. No update. | 3 | | `"CODEBA"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'C'`. `window['C']` becomes 0. <br> - Since `window['C'] < need['C']` (0 < 1), decrement `formed` to 2. | 2 | `left` becomes 6. **Invalid**. | `"ODEBA"` | `6` / `"ADOBEC"` |
| 12 | 11 | 'N' | `{'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1, 'C': 0, 'N': 1}` | 2 | Invalid. | `"ODEBAN"` | `6` / `"ADOBEC"` |
| 13 | 12 | 'C' | `{'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1, 'C': 1, 'N': 1}` | 3 | `window['C'] == need['C']` -> `formed = 3`. **Valid**. | `"ODEBANC"` | `6` / `"ADOBEC"` |
| | | | **Shrink Loop** (while `formed == 3`): | | | | |
| | | | - Current length 7 is not < 6. No update. | 3 | | `"ODEBANC"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'O'`. `window['O'] = 0 >= need['O']`. | 3 | `left` becomes 7. | `"DEBANC"` | `6` / `"ADOBEC"` |
| | | | - Current length 6 is not < 6. No update. | 3 | | `"DEBANC"` | `6` / `"ADOBEC"` |
| | | | - Remove `s[left] = 'D'`. `window['D'] = 0 >= need['D']`. | 3 | `left` becomes 8. | `"EBANC"` | `6` / `"ADOBEC"` |
| | | | - Current length 5 < 6! Update: `minLen = 5`, `res = "EBANC"`. | 3 | Update match. | `"EBANC"` | `5` / `"EBANC"` |
| | | | - Remove `s[left] = 'E'`. `window['E'] = 0 >= need['E']`. | 3 | `left` becomes 9. | `"BANC"` | `5` / `"EBANC"` |
| | | | - Current length 4 < 5! Update: `minLen = 4`, `res = "BANC"`. | 3 | Update match. | `"BANC"` | `4` / `"BANC"` |
| | | | - Remove `s[left] = 'B'`. `window['B']` becomes 0. <br> - Since `window['B'] < need['B']` (0 < 1), decrement `formed` to 2. | 2 | `left` becomes 10. **Invalid**. | `"ANC"` | `4` / `"BANC"` |

**Final Result:** `"BANC"`

### Complexity Analysis

#### Time Complexity
- **$O(m + n)$** where $m = \text{len}(s)$ and $n = \text{len}(t)$.
  - Creating the initial `need` map takes $O(n)$ time.
  - The `right` pointer iterates through `s` exactly once, taking $O(m)$ steps.
  - The `left` pointer moves forward at most $m$ times over the entire execution, meaning each index is visited at most once by `left`.
  - All hash map operations run in $O(1)$ average time.

#### Space Complexity
- **$O(m + n)$** in the worst case to store the counts in `need` and `window`. If the character set is bounded (e.g. ASCII), this is **$O(1)$** auxiliary space because the maps will hold at most a constant number of unique characters.

---

## Common Mistakes

- **Direct Map Comparisons:** Comparing the `window` map directly with the `need` map inside the loops (e.g. `window == need`). This costs $O(\Sigma)$ time on every check, degrading performance.
- **Incorrect Validity Increments:** Incrementing `formed` on `window[ch] >= need[ch]` rather than checking exact equality (`==`). This results in counting duplicate matches multiple times.
- **Forgetting to check the character is in `need`:** Adjusting `formed` based on characters that are not even present in string `t`.
- **Inefficient String Slicing:** Slicing the string `s` inside the loop to store intermediate results. Slicing takes $O(\text{window len})$ time.
  - *Better practice:* Store the `(best_left, best_right)` indices and perform a single slice at the end of the algorithm.

---

## Key Takeaways

- **The Requirements Tracking Pattern:** When checking if a window satisfies a multi-character condition, do not compare the entire frequency structures. Instead, use a single `formed` counter that tracks how many unique characters have met their target counts.
- **Minimum vs. Maximum Windows:** For *maximum* sliding window problems, we update our answer when expanding. For *minimum* sliding window problems, we only update our answer when contracting the window, since we want to find the smallest valid configuration.
- **Index-Only Slicing:** Avoid expensive copy operations (like string slicing) inside performance-critical loops. Save the pointers and generate the substring only once after completing the iteration.
