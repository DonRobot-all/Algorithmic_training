class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word
            if word[i] == '.':
                return any(dfs(children, i+1) for children in node.children.values())
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            return False

        return dfs(self.root, 0)