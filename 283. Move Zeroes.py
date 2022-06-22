class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        
        nums[:] = [val for val in nums if val != 0] + [0 for val in range(0,count)]
        