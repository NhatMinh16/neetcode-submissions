class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"]": "[",
                    "}": "{",
                    ")": "("}

        brackets = []
        for bracket in s:
            if bracket in "({[":
                brackets.append(bracket)
            else:
                if len(brackets) > 0 and brackets[-1] == matches[bracket]:
                    brackets.pop()
                else:
                    return False
        return len(brackets) == 0