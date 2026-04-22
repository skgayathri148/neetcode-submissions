class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque([])
        braces_map = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for char in s:
            if char in braces_map:
                if not queue:
                    return False
                elif queue[-1] != braces_map[char]:
                    return False
                else:
                    queue.pop()

            else:
                queue.append(char)
        
        return len(queue) == 0