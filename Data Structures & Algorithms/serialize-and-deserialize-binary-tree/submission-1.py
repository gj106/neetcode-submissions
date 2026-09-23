# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        if root is None:
            return "N"
        res = []

            
        q = deque([])

        q.append(root)

        while q:
            t = q.popleft() # q=[1,2,3,N,N]
            if t is None:
                res.append("N") # 
            else:
                res.append(str(t.val)) # res=[1] [1,2,3] [1,2,3,N,N,4,5]
                q.append(t.left)
                q.append(t.right)
        
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data is "N":
            return None
        
        res = data.split(",")
        q = deque([])
        root = TreeNode(int(res[0]))
        q.append(root)

        i = 0

        while q:
            t = q.popleft()
            i +=1

            if res[i] != "N":
                t.left = TreeNode(res[i])
                q.append(t.left)
            
            i+=1

            if res[i] != "N":
                t.right = TreeNode(res[i])
                q.append(t.right)
        return root

            

