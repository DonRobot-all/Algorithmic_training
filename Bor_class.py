# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def insert(self, word):
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end_of_word = True

#     def to_dict(self, node=None):
#         if node is None:
#             node = self.root
#         result = {}
#         for char, child_node in node.children.items():
#             result[char] = self.to_dict(child_node)
#         return result
       
#     def search(self, word):
#         node = self.root
#         for ch in word:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.is_end_of_word

# # Использование
# trie = Trie()
# words = ["cat", "car", "cart", "dog"]
# for w in words:
#     trie.insert(w)

# print(trie.to_dict())
# print(trie.search("car"))  # True
# print(trie.search("cart"))  # True
# print(trie.search("cars"))  # False
# print(trie.search("dog"))  # True


class Trie:
    def __init__(self):
        self.tree = dict()

class TrieNode:
    def __init__(self):
        self.root = Trie()

    def insert(self,word):
        node = self.root
        for i in word:
            if i not in node.tree:
                node.tree[i] = Trie()
            node = node.tree[i]

    def get(self, node=None):
        if node is None:
            node = self.root
        result = {}
        for char, child_node in node.tree.items():
            result[char] = self.get(child_node)
        return result 


trie = TrieNode()
print(trie.insert('cat'))
print(trie.get())