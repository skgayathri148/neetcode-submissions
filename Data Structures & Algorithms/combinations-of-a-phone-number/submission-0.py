class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
        '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0:
            return []
            
        res = []
        choice= ""

        def recursion(i, choice):
            if i >= len(digits):
                res.append(choice[::])
                return
            digit = digits[i]
            for j in range(0, len(num_char[digit])):
                choice += num_char[digit][j]
                recursion(i+1, choice)
                choice = choice[:i]
        
        recursion(0, choice)
        return res
            