# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        IOCE:
        input: root (treenode), val (node to find)
        output: list of treenodes
        constraints: return entire subtree of val including val
        examples: 
        Plan:
            curr = root
            if curr.val is None:
                return []
            if curr.val > val:
                traverse left
            if curr.val < val:
                traverse right
        '''
        def dfs(root, val):
            if not root:
                return root
            if root.val == val:
                return root
            if root.val > val:
                return dfs(root.left, val)
            if root.val < val:
                return dfs(root.right, val)
        return dfs(root,val)
