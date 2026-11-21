class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        words = dict()
        for word in s:
            words.setdefault(word, 0)
            words[word] += 1
        for word in t:
            if word not in words or words[word] == 0:
                return False
            words[word] -= 1
        return True