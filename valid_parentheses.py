class Solution:
    #given a str containing just the characters '(',')','[',']','[',']'
    #open brackets closed by same type of bracket
    #open brackets must be closed in proper order
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[","}":"{"}

        for c in s:
            if c in closeToOpen:
                #make sure the opening and closing brace match
                if stack and stack[-1] == closeToOpen[c]
                else:
                    return False
            else:
                #if we get an open parenthese take that char and append to stack
                stack.append(c)
        #if stack is empty return true
        return True if not stack else False