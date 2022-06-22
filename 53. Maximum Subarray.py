class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0] 
        sum = 0
        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            maxValue = max(sum, maxValue)
        return maxValue