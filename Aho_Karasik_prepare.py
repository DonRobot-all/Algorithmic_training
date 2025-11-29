from collections import deque, defaultdict

def build_trie(patterns):
    ...

def build_automaton(edges, fail, output):
    ...

def search(text, edges, fail, output, patterns):
    ...

# Пример использования:
patterns = ["ababac", "bababab", "ab", "bab"]
text = "ababababacbababab"
edges, fail, output = build_trie(patterns)  # Строим бор
build_automaton(edges, fail, output)       # Строим суффиксные ссылки
matches = search(text, edges, fail, output, patterns)  # Ищем вхождения

for pattern, positions in matches.items():
    print(f"Паттерн '{pattern}' найден на позициях {positions}")
