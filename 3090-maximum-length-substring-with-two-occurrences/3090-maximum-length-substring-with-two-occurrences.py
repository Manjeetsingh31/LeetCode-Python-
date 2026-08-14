class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        length = 0
        for rig in range(len(s)):
            count[s[rig]] = count.get(s[rig], 0)+1
            while count[s[rig]] > 2:
                count[s[left]] -=1
                left +=1
            length = max(length, rig - left +1) 
        return length       
        