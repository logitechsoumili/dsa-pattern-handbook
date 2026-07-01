class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> targetFreq;
        unordered_map<char, int> windowFreq;

        // creating map of characters in t
        for (char ch : t)
        {
            targetFreq[ch]++;
        }

        int required = targetFreq.size();
        int formed = 0, left = 0;
        int minLen = INT_MAX;
        int start = 0;

        for (int right = 0; right < s.size(); right++){
            
            // expanding from right
            char ch = s[right];
            windowFreq[ch]++;

            // if the character exists and satisfies the number of characters in targetFreq,
            // formed++ to match required which stores the targetFreq.size()
            if (targetFreq.count(ch) && targetFreq[ch] == windowFreq[ch]) formed++;

            // valid condition
            while (formed == required){
                int windowLen = right - left + 1;

                // 1. update answer
                if (windowLen < minLen){
                    minLen = windowLen;
                    start = left;
                }

                // 2. shrink from left
                char lc = s[left];
                windowFreq[lc]--;

                // 3. if the window becomes invalid, stop shrinking.
                if (targetFreq.count(lc) && windowFreq[lc] < targetFreq[lc]) formed--;
                left++;
            }
        }

        return minLen == INT_MAX ? "" : s.substr(start, minLen);
    }
};