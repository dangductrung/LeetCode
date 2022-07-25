class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums: List[int], target: int):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        pivot = binary_search(nums, target)

        if pivot == -1:
            return [-1, -1]

        left, right, count = pivot, pivot, len(nums) - 1

        while left >= 0 and nums[left] == target:
            left = left - 1
        while right <= count and nums[right] == target:
            right = right + 1
        return [left + 1, right - 1]

