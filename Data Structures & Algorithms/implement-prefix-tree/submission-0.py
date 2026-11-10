class PrefixNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        root = PrefixTree()
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] =  PrefixNode()
            curr = curr.children[c]
        
        curr.end_of_word = True



    def search(self, word: str) -> bool:

        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        
        return True
        
        