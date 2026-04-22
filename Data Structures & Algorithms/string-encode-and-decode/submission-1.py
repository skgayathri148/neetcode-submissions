class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output = output + str(len(string)) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        res = []
        prev = 0
        while prev < len(s):
            curr = prev
            while s[curr] != '#':
                curr += 1
            length = int(s[prev:curr])
            prev = curr + 1
            curr = prev + length
            res.append(s[prev:curr])
            prev = curr

        return res
            
