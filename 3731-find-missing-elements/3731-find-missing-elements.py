class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        m = min(nums)
        ma = max(nums)

        num = set(nums)
        for i in range(m,ma+1):
            if i not in num:
                res.append(i)
        return res