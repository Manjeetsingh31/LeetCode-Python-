class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dist = {}
        maxi = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] in my_dist:
                left = max(left,my_dist[s[right]] +1)
            maxi = max(maxi, right - left +1)  
            my_dist[s[right]] = right
            right +=1
        return maxi      
        
        