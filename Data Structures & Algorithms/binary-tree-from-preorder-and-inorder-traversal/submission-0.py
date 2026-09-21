# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        io_dict = {val:idx for idx, val in enumerate(inorder)}

        po_index = 0
            
        def build(lidx, ridx):
            nonlocal po_index
            if lidx > ridx:
                return None
            
            po_val = preorder[po_index]
            Tnode = TreeNode(po_val)
            po_index += 1
            mid = io_dict.get(po_val)

            Tnode.left = build(lidx, mid-1)

            Tnode.right = build(mid+1, ridx)

            return Tnode
        return build(0, len(preorder)-1)
        


        