# LeetCode 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = formed = 0
        minLen = float('inf')
        res = ''
        need = Counter(t)
        window = Counter()

        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                formed += 1

            while formed == len(need):
                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    res = s[left:right+1]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return res