class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        left = 1
        n = len(nums)

        for i in range(n):
            arr[i] = left
            left *=  nums[i]
        right = 1
        for i in range(n -1, -1, -1):
            arr[i] *= right
            right *= nums[i]
        return arr       

        