class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        chars = set()
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen