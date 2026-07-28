from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        first = []
        mid = ""
        for ch in sorted(freq):
            first.append(ch*(freq[ch]// 2))
            if freq[ch]% 2:
                mid = ch
        first = "".join(first)
        return first+mid+first[::-1]        