class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        data = nums1[0:m] + nums2[0:n]
        data.sort()
        nums1[:] = data 
        