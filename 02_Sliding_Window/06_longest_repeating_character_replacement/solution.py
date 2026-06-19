# LeetCode 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        freq = {}
        maxFreq = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            windowLen = right - left + 1

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen