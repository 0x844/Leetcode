# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, storage):
            if not root:
                return storage
            dfs(root.left,storage)
            storage.append(root.val)
            dfs(root.right, storage)
            return storage
        arr = dfs(root,[]) # check if arr is strictly increasing
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True
