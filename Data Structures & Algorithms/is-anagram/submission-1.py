class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
            return False
        
        freq = [0] * 26
        
        for i in range(m):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        
        for val in freq:
            if val != 0:
                return False
        
        return True
