# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(node1, node2):
            if not node1 and not node2: # both nodes null, accept
                return True
            if not node1 or not node2: # one node null, decline
                return False
            # check if vals same, then traverse opposite nodes and check symmetry
            return node1.val == node2.val and mirror(node1.left, node2.right) and mirror(node1.right, node2.left)
        return mirror(root.left, root.right)
