class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x =  ""
        dig_sum = 0
        for ch in str(n):
            if ch != '0':
                x += ch
                dig_sum += int(ch)
        if x == "":
            return 0
        return int(x) * dig_sum            
        