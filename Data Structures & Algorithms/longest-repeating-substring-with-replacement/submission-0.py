class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        char_freq = {}
        max_count = 0

        for end in range(len(s)):
            if not s[end] in char_freq:
                char_freq[s[end]] = 0
            char_freq[s[end]] += 1

            char_count = end - start + 1
            if char_count - max(char_freq.values()) <= k:
                max_count = max(max_count, char_count)

            else:
                char_freq[s[start]] -= 1
                if not char_freq[s[start]]:
                    char_freq.pop(s[start])
                start += 1

        return max_count