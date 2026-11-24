class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first = 0
        second = 0
        res = ""
        while first < len(word1) and second < len(word2):
            res += word1[first] + word2[second]
            first += 1
            second += 1
        res += word1[first:]
        res += word2[second:]
        return res