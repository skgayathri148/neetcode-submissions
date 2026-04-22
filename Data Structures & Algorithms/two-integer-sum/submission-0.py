class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in key_dict:
                return [key_dict[difference], i]
            else:
                key_dict[nums[i]] = i
                