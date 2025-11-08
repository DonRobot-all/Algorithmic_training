# Заготовка
# -----------------------------------------
# Построение бора (trie)
# -----------------------------------------
def build_trie(words):
    ...


# -----------------------------------------
# Поиск узла, соответствующего префиксу
# -----------------------------------------
def find_prefix_node(root, prefix):
    ...


# -----------------------------------------
# DFS для сбора всех слов из вершины
# prefix — собранное слово на данный момент
# -----------------------------------------
def collect_words(node, prefix, result):
    ...


# -----------------------------------------
# Главная функция автодополнения
# -----------------------------------------
def autocomplete(root, prefix):
    ...

words = ["cat", "car", "cartoon", "carbon", "dog", "door"]
trie = build_trie(words)

print(autocomplete(trie, "ca"))   # ['cat', 'car', 'cartoon', 'carbon']
print(autocomplete(trie, "do"))   # ['dog', 'door']
print(autocomplete(trie, "z"))    # []
