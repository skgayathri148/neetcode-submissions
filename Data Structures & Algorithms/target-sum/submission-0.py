class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(i, currSum):
            if i >= len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0

            res = dfs(i + 1, currSum + nums[i])
            res += dfs(i + 1, currSum - nums[i])

            return res

        return dfs(0,0)