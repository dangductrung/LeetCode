class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            res.append(sum(nums[0:i+1]))
        return res