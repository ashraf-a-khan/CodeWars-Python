"""
Leetcode: 349. Intersection of Two Arrays

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        for i in nums1:
            if i in nums2:
                intersect.append(i)

        return set(intersect)