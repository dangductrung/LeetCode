class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1.sort()
        nums2.sort()
        
        pivot1 = 0
        pivot2 = 0
        while pivot1 < len(nums1) and pivot2 < len(nums2): 
            if nums1[pivot1] == nums2[pivot2]:
                result.append(nums1[pivot1])
                pivot1 += 1
                pivot2 += 1
            elif nums1[pivot1] > nums2[pivot2]:
                pivot2 += 1
            elif nums1[pivot1] < nums2[pivot2]:
                pivot1 += 1
        return result