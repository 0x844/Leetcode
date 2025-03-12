class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        for string in arr:
            if string == "..":
                if stack:
                    stack.pop()
            elif string and string != ".":
                stack.append(string)
        
        return "/" + "/".join(stack)
