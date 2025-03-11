# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        
        if not root:
            return []
        
        queue = deque([root])

        zigzag_flag = True # True means right to left, False means left to right

        while queue:
            length = len(queue)
            level = []

            for _ in range(length):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                
            if zigzag_flag:
                level.reverse()

            results.append(level)

            zigzag_flag = not zigzag_flag

        return results
