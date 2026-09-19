# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        res = []

        from collections import deque

        # Convert your list to a deque
        q = deque([root])
        while q:
            tres = []
            tl = len(q)
            for i in range(tl):
                t = q.popleft()
                if t:
                    q.append(t.left)
                    q.append(t.right)
                    tres.append(t.val)
            if tres:
                res.append(tres)
                    

        return res


        