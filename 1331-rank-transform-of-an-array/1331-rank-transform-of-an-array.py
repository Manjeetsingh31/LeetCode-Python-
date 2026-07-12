class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        r = {}
        for i , num in enumerate(sorted(set(arr)), 1):
            r[num] = i
        return [r[num] for num in arr]    
            
        