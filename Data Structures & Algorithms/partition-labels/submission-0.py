class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = defaultdict(int)
        for i in range(len(s)):
            lastIdx[s[i]] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIdx[c])
            if i == end:
                res.append(size)
                size = 0
        return res
        