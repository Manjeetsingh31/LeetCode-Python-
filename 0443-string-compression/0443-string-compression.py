class Solution:
    def compress(self, chars: List[str]) -> int:
        store = 0
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j +=1
            chars[store] = chars[i]
            store +=1
            count = j - i
            if count > 1:
                for digit in str(count):
                    chars[store] = digit
                    store +=1
            i = j
        return store                

        