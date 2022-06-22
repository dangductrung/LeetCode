class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers) - 1
        sum = 0
        while start != end:
            startValue = numbers[start]
            endValue = numbers[end]
            
            if (startValue + endValue) > target:
                end -= 1
            elif (startValue + endValue) < target:
                start += 1
            else:
                return [start + 1, end + 1]
            
        return []