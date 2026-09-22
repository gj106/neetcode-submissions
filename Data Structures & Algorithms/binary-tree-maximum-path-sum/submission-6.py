# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        msum = float('-inf')
        def dfs(root):
            nonlocal msum

            if root is None:
                return 0

            left_branch = max(dfs(root.left), 0) # take out -ves by considering 0
            right_branch = max(dfs(root.right), 0) 
            csum = root.val + left_branch + right_branch 
            msum = max(msum, csum)


            return root.val + max(left_branch, right_branch)


        
        dfs(root)
        return msum
        
