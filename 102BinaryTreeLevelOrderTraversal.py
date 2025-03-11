# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        # bfs
        def bfs(root):
            if not root:
                return []

            queue = deque([root])

            while queue:
                length = len(queue)
                level = [] # local storage for nodes on same level
                for i in range(length):
                    curr = queue.popleft()
                    level.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                results.append(level)
        bfs(root)
        return results        
