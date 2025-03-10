# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def DFS(node, sum):
            # if leaf, then exit
            if not node.right and not node.left:
                if sum + node.val == targetSum: # add current nodes val to sum
                    return True
                else:
                    return False
            if node.left and DFS(node.left, sum + node.val):
                return True
            if node.right and DFS(node.right, sum + node.val):
                return True
            return False

        return DFS(root, 0) 
