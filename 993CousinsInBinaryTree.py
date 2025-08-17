# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        levels = {root.val: count} # node.val: level
        parents = {root.val: -1} # node.val: parent
        def bfs(root):
            count = 0
            if not root:
                return
            queue = deque([root])
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    print(levels)
                    if curr.left:
                        parents[curr.left.val] = curr.val
                        levels[curr.left.val] = count + 1
                        queue.append(curr.left)
                    if curr.right:
                        parents[curr.right.val] = curr.val
                        levels[curr.right.val] = count + 1
                        queue.append(curr.right)
                count += 1
        bfs(root)
        if levels[x] == levels[y] and parents[x] != parents[y]:
            return True
        return False
