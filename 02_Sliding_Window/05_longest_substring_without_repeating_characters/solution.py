# LeetCode 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

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