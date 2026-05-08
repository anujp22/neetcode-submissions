class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")" and len(stack) != 0:
                cmpr = stack.pop()
                if cmpr != "(":
                    return False
            elif s[i] == "]" and len(stack) != 0:
                cmpr = stack.pop()
                if cmpr != "[":
                    return False
            elif s[i] == "}" and len(stack) != 0:
                cmpr = stack.pop()
                if cmpr != "{":
                    return False
        return len(stack) == 0