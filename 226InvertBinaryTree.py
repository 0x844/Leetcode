# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        def dfs(root):
            if not root:
                return root  

            temp = root.right
            root.right = root.left
            root.left = temp

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return root  
