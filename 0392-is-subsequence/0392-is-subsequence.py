class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        first = 0
        last = 0
        while first < len(s) and last < len(t):
            if s[first] == t[last]:
                first +=1
            last +=1
        return first == len(s)        

