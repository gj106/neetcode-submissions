class TrieNode:
    def __init__(self):
        self.children = {}
        # Storing the word directly at the end node saves us from passing 
        # a string builder through the DFS recursive calls.
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        ROWS, COLS = len(board), len(board[0])
        res = set() # Use a set to prevent duplicate words in the output
        visit = set()

        def dfs(r, c, node):

            if (r < 0 or c < 0 or r >= ROWS or c >=COLS or board[r][c] not in node.children or (r,c) in visit):
                return
            
            visit.add((r,c))

            curr = node.children[board[r][c]]

            if curr.word:
                res.add(curr.word)
            
            dfs(r + 1, c, curr)
            dfs(r - 1, c, curr)
            dfs(r, c + 1, curr)
            dfs(r, c - 1, curr)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        
        return list(res)



        