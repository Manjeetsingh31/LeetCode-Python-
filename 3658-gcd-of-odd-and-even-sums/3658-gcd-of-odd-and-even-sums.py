class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = n * n
        even = n *(n +1)
        return gcd(odd, even)
    def gcd(a, b):
        while (b != 0):
            temp = b
            b = a% b
            a = temp
        return a 

        