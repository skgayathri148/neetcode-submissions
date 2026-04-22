class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_freq = [0] * 26
        for char1 in s1:
            s1_freq[ord(char1) - ord('a')] += 1
        
        start = 0
        while start <= len(s2) - len(s1):
            end = start + len(s1)
            s2_freq = [0] * 26
            for i in range(start, end):
                s2_freq[ord(s2[i]) - ord('a')] += 1
            if s2_freq == s1_freq:
                return True
            start += 1

        return False