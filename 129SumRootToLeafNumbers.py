# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def sumNumbers(self, root):

        def DFS(node, sum):

            # if node null
            if not node:
                return 0

            # sum starts as 0, so
            # 0 * 10 + 1 == 1
            # 1 * 10 + 2 == 12 (left subtree)
            # 1 * 10 + 3 == 13 (right subtree)
            sum = sum * 10 + node.val

            # if leaf, return sum
            if not node.right and not node.left:
                return sum

            left = DFS(node.left, sum)
            right = DFS(node.right, sum)

            return left + right

        return DFS(root, 0)
