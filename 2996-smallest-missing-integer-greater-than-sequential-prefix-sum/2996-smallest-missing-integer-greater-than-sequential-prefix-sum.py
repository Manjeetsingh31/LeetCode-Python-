class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        tot = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            tot += nums[i]
        while tot in nums:
            tot +=1
        return tot            
        