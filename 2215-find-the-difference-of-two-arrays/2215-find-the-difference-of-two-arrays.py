class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = set(nums1)
        answer2 = set(nums2)
        return [list(answer1 - answer2), list(answer2 - answer1)]

        