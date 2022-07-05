class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        data = sorted(list(set(nums)))
        start, end, maxLength = 0, 1, 0

        while end != len(data):
            if (data[end] - data[end - 1]) != 1:
                maxLength = max(maxLength, end - start)
                start = end
                
            end += 1
        maxLength = max(maxLength, end - start)
                
        return maxLength
        
