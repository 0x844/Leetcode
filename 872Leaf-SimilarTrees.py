# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # get leafs of each tree, store in list passed into dfs func
        def dfs(root, lst):
            if not root:
                return lst
            if not root.right and not root.left: # if leaf
                lst.append(root.val)
                
            right = dfs(root.right, lst)
            left = dfs(root.left, lst)
            return right and left

        return dfs(root1, []) == dfs(root2, [])
