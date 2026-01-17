def build_trie(words):
    root = {}  # корень — просто пустой словарь

    for word in words:
        node = root  # начинаем с корня
        for ch in word:
            # если такого перехода ещё нет — создаём новый словарь
            if ch not in node:
                node[ch] = {}
            # переходим по букве
            node = node[ch]
        # после последней буквы отмечаем конец слова
        node['#'] = True

    return root

def find_prefix_node(root, prefix):
    node = root  # идём с корня

    for ch in prefix:
        # если нет перехода — значит слов с таким префиксом нет
        if ch not in node:
            return None
        node = node[ch]

    return node  # вершина после последнего символа префикса

def collect_words(node, prefix, result):
    # если есть пометка конца слова — записываем его в результат
    if '#' in node:
        result.append(prefix)

    # проходим по всем буквам (кроме символа '#')
    for ch in node:
        if ch != '#':  # пропускаем метку конца слова
            collect_words(node[ch], prefix + ch, result)

def autocomplete(root, prefix):
    start = find_prefix_node(root, prefix)
    if start is None:
        return []  # ни одно слово не подходит

    result = []
    collect_words(start, prefix, result)
    return result

words = ["cat", "car", "cartoon", "carbon", "dog", "door"]
trie = build_trie(words)
print(trie)
print(autocomplete(trie, "ca"))   # ['cat', 'car', 'cartoon', 'carbon']
print(autocomplete(trie, "do"))   # ['dog', 'door']
print(autocomplete(trie, "z"))    # []
