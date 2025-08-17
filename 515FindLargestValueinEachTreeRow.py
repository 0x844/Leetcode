# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        max_vals = [root.val]
        def bfs(root):
            if not root:
                return
            queue = deque([root])    
            while queue:
                local = []
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    if curr.left:
                        local.append(curr.left.val)
                        queue.append(curr.left)
                    if curr.right:
                        local.append(curr.right.val)
                        queue.append(curr.right)
                if local:
                    max_vals.append(max(local))
        bfs(root)
        return max_vals
            
