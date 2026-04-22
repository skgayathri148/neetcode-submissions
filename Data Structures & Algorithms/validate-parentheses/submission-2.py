class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()
        match = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char not in match:
                queue.append(char)
            
            elif queue and match[char] == queue[-1]:
                queue.pop()
            
            else:
                return False
        
        return len(queue) == 0