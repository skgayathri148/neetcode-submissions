class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.recursive([], nums, [False] * len(nums))
        return self.res

    def recursive(self, curr, nums, track):
        if len(curr) == len(nums):
            self.res.append(curr.copy())
            return

        for i in range(len(nums)):
            if not track[i]:
                curr.append(nums[i])
                track[i] = True
                self.recursive(curr, nums, track)
                curr.pop()
                track[i] = False
            
