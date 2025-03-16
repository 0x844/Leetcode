class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            while stack and rock < 0 < stack[-1]:
                if abs(rock) > abs(stack[-1]):
                    stack.pop()
                elif abs(rock) == abs(stack[-1]):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(rock)
        return stack
