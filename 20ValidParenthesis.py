class Solution:

    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        stack = []

        valid = {'(': ')', '{': '}', '[': ']'}

        for letter in s:
            if letter in valid.keys():  # if opening bracket
                stack.append(letter)
            elif letter in valid.values():  # if closing bracket
                # check corresponding key to see if it matches
                if len(stack) == 0 or valid[stack.pop()] != letter:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
