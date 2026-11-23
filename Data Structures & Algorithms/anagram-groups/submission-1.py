from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        res = []
        for word in strs:
            s = tuple(sorted(word))
            words[s].append(word)
        for word in words:
            res.append(words[word])
        return res