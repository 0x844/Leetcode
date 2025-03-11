# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        if not root:
            return 0

        if not root.right and not root.left:
            return 1

        def dfs(root, count):
            if not root:
                return count
            
            left = dfs(root.left, count + 1)
            right = dfs(root.right, count + 1)

            return max(left, right)       
            
        return dfs(root, 0)
