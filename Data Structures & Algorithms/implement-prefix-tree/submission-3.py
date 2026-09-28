class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False 

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        words = []
        node = self.root
        for c in prefix: 
            if c not in node.children:
                return False
            node = node.children[c]
        
        def dfs(node, path):
            if node.isEnd: 
                words.append(''.join(path))
            
            for c, child_node in node.children.items():
                dfs(child_node, path + [c])

        dfs(node, list(prefix))
        if len(words) > 0: 
            return True
        return False