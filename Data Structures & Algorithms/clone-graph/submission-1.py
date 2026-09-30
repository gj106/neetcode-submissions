"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # if node is None:
        #     return None

        # clones = {}
        # clones[node] = Node(node.val)
        # q = collections.deque([node])

        # while q:
        #     curr = q.popleft()

        #     for neigh in curr.neighbors:
        #         if neigh not in clones:
        #             #clone the nightbor as its not present in the clones dict
        #             clones[neigh] = Node(neigh.val)
        #             # append to 
        #             q.append(neigh)
        #         # append the clones of neighbours to the cloned current node
        #         clones[curr].neighbors.append(clones[neigh])
            
        # return clones[node]
        clones = {}

        def dfs(root):

            if root is None:
                return None
            
            if root in clones:
                return clones[root]
            
            if root not in clones:
                clones[root] = Node(root.val)
            
            for n in root.neighbors:
                clones[root].neighbors.append(dfs(n))
            
            return clones[root]
        
        return dfs(node)
                
                

        