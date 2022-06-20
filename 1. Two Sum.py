class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(0, len(nums)):
            delta = target - nums[index]
            if(delta in nums[index + 1 : len(nums)]):
                y = index + 1 + nums[index + 1 : len(nums)].index(delta)
                return [index, y]
        