# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        results = []

        def bfs(root):
            if not root:
                return results
            queue = deque([root])
            
            while queue:
                level_size = len(queue)
                sum = 0
                for i in range(level_size):
                    curr = queue.popleft()
                    sum += curr.val

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                
                results.append(sum / level_size)
                
        bfs(root)

        return results
