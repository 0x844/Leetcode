class Solution:
    def reverseWords(self, s: str) -> str:
        stack = s.split()
        length = len(stack)
        result = ""
        for i in range(length):
            if i + 1 == length:
                result += stack.pop()
            else:
                result += stack.pop() + " "
    
        return result
