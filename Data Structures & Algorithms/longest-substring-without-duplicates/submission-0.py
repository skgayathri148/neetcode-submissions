class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, curr = 0, 0
        substring = ""
        for char in s:
            if char in substring:
                longest = max(longest, curr)
                char_pos = substring.find(char)
                substring = substring[char_pos + 1:] + char
                curr = len(substring)
            else:
                substring += char
                curr += 1
        return max(longest, curr)