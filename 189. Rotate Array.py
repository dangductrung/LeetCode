class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        remain = k % len(nums)
        if remain == 0:
            return

        position = len(nums) - remain
        head = nums[position:]
        tail = nums[0: position]
        nums[:] = head + tail