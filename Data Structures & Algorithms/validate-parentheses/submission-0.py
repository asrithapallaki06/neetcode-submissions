class Solution:
    def isValid(self, s: str) -> bool:
        match = {")" : "(", "]" : '[', "}" : "{"}
        # create empty stack
        stack = []
        # loop through string
        for c in s:
            # if its opener push to stack
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                # if its empty return false
                if not stack:
                    return False
                # if closer doesnt match with the top most element in stack
                if stack[-1] != match[c]:
                    return False
                stack.pop()
        return len(stack) == 0

