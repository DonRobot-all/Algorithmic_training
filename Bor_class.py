class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True
        
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

# Использование
trie = Trie()
words = ["cat", "car", "cart", "dog"]
for w in words:
    trie.insert(w)

print(trie.search("car"))  # True
print(trie.search("cart"))  # True
print(trie.search("cars"))  # False
print(trie.search("dog"))  # True
