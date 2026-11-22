class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        sorted_arr = sorted(strs, key=len)
        length = len(sorted_arr[0])
        for index in range(length):
            char = sorted_arr[0][index]
            for word in sorted_arr[1:]:
                if word[index] != char:
                    return prefix
            prefix += char
        return prefix
        
                