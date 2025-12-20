class Trie:
    def __init__(self):
        self.tree = dict()
        self.is_end_of_word = False


class Trienode:
    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.tree:
                node.tree[char] = Trie()
            node = node.tree[char]
        node.is_end_of_word = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # obj = Trienode()
        # obj.bor(words)
        obj = Trienode()
        for word in words:
            obj.insert(word)
        lenstring = len(words)
        lenstringdown = len(words[0])
        visited = set()
        result = []
        def dfs(x,y,node,path):
            print(node)
            if node.is_end_of_word == True:
                result.append(path)
                node.is_end_of_word = False
            #print(type(path))
            #print(path)
            visited.add((x,y))
            coords = [(0,1), (1,0), (0,-1), (-1,0)]
            for x2,y2 in coords:
                new_x = x+x2
                new_y = y+y2
                if new_x >= 0 and new_x < lenstring and new_x not in visited and new_y >= 0 and new_y < lenstring and new_y not in visited:
                    n = board[new_x][new_y]
                    if n in node.tree:
                        print(path+n)
                        dfs(new_x,new_y,node.tree[n],path+n)
            visited.remove((x,y))
        for i in range(lenstring):
            for j in range(lenstringdown):
                b = board[i][j]
                if b in obj.root.tree:
                    dfs(i,j,obj.root.tree[b],b)
        return list(result)


# obj = Trienode()
# obj.bor([["o","a","a","n"],["e","t","a","e"]])
board = [['a', 'b']]
words = ["ab"]
obj2 = Solution()
obj2.findWords(board, words)
print(obj2)
# print(obj)