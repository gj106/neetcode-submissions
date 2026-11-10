class TrieNode:
    def __init__(self):
        # Maps a character to its child TrieNode
        self.children = {} 
        # Flags if a complete word ends at this node
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """Inserts a word into the trie."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        # Mark the last node as the end of the inserted word
        curr.is_end_of_word = True
        

    def search(self, word: str) -> bool:

        
        def dfs(index, root):
            curr = root

            for i in range(index, len(word)):
                c  = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.is_end_of_word
        return dfs(0, self.root)
                

        
