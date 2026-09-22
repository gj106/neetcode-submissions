# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):

            if root is None:
                return
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)

        # result = 0
        for i, val in enumerate(res):
            if i == k-1:
                return val
                # break
        # return result



            

        