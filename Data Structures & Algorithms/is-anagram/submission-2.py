class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen:
            return False
        
        sCount = [0] * 26
        tCount = [0] * 26

        for i in range(sLen):
            sCount[ord(s[i]) - ord('a')] += 1
            tCount[ord(t[i]) - ord('a')] += 1

        for c in range(26):
            if sCount[c] != tCount[c]:
                return False
        
        return True