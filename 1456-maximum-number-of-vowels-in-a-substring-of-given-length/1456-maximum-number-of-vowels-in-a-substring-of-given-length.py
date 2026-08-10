class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        count  = 0
        for i in range(k):
            if s[i] in vowel:
                count +=1
        maximum = count
        for j in range(k , len(s)):
            if s[j -k] in vowel :
                count -=1
            if s[j] in vowel:
                count +=1 

            maximum = max(maximum, count)
        return maximum                   
            