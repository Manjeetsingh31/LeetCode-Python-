class Solution:
    def minimumPushes(self, word: str) -> int:
        nuo = 0

        for i in range(len(word)):
            nuo += (i // 8) + 1

        return nuo
        