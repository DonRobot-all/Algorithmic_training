from collections import deque, defaultdict

def build_trie(patterns):
    # edges - список словарей: для каждой вершины хранит переходы по символам
    edges = [{}]
    # output - список множеств, для каждой вершины набор индексов шаблонов, заканчивающихся тут
    output = [set()]
    # fail - список суффиксных ссылок, изначально все -1
    fail = [-1]
    num_nodes = 1  # счетчик вершин в боре (начинается с корня)

    # Строим бор из всех шаблонов
    for index, pattern in enumerate(patterns):
        current = 0  # начинаем с корня
        for char in pattern:
            # Если перехода по символу нет, создаём новую вершину
            if char not in edges[current]:
                edges[current][char] = num_nodes
                edges.append({})
                fail.append(-1)  # суффиксная ссылка для новой вершины пока -1
                output.append(set())  # выходные состояния для новой вершины пока пусты
                num_nodes += 1
            # Переходим в следующую вершину
            current = edges[current][char]
        # Отмечаем, что в данной вершине заканчивается шаблон с индексом index
        output[current].add(index)
    return edges, fail, output

def build_automaton(edges, fail, output):
    # print(f'Начало работы {edges}, {fail}, {output}')
    queue = deque()
    # Инициализируем очередь вершинами первого уровня,
    # устанавливаем им суффиксные ссылки в корень (0)
    for char, node in edges[0].items():
        fail[node] = 0
        queue.append(node)

    # print(fail, queue)
    # Строим суффиксные ссылки для остальных вершин
    while queue:
        r = queue.popleft()
        for char, u in edges[r].items():
            queue.append(u)
            f = fail[r]
            # Пытаемся найти переход по символу char из вершины с суффиксной ссылкой f,
            # если нет, переходим дальше по суффиксным ссылкам
            while f != -1 and char not in edges[f]:
                f = fail[f]
            # Если нашли переход, присваиваем его суффиксной ссылке
            fail[u] = edges[f][char] if f != -1 and char in edges[f] else 0
            # Объединяем выходные паттерны из суффиксной ссылки с текущей вершиной,
            # чтобы находить вложенные или пересекающиеся шаблоны
            output[u].update(output[fail[u]])

def search(text, edges, fail, output, patterns):
    result = defaultdict(list)  # словарь: шаблон -> список позиций вхождений
    state = 0  # начинаем с корня автомата
    for i, char in enumerate(text):
        # Пока нет перехода по символу char из текущего состояния,
        # переходим в состояние по суффиксной ссылке
        while state != -1 and char not in edges[state]:
            state = fail[state]
        # Если нашли переход, идём по нему, иначе возвращаемся в корень
        state = edges[state][char] if state != -1 and char in edges[state] else 0
        # Для всех шаблонов, которые заканчиваются в текущем состоянии,
        # вычисляем позицию вхождения и добавляем в результат
        for pattern_index in output[state]:
            pos = i - len(patterns[pattern_index]) + 1
            result[patterns[pattern_index]].append(pos)
    return result

# Пример использования:
patterns = ["ababac", "bababab", "ab", "bab"]
text = "ababababacbababab"
edges, fail, output = build_trie(patterns)  # Строим бор
build_automaton(edges, fail, output)       # Строим суффиксные ссылки
matches = search(text, edges, fail, output, patterns)  # Ищем вхождения

for pattern, positions in matches.items():
    print(f"Паттерн '{pattern}' найден на позициях {positions}")



# fail — массив суффиксных ссылок:
#     Для каждой вершины i содержит номер вершины fail[i], представляющей самый длинный собственный суффикс строки, соответствующей вершине i, который является префиксом какого-то шаблона.
#     Для корня fail[0] = 0 (или остается -1 в некоторых реализациях).
#     Для вершин первого уровня fail = 0 (корень).
#     Для остальных — переход по суффиксной цепочке к ближайшему суффиксу-префиксу.
# output — массив множеств индексов шаблонов:
#     Для каждой вершины i содержит все индексы шаблонов, которые заканчиваются в этой вершине ИЛИ в любой вершине по цепочке её суффиксных ссылок.
#     Изначально содержал только шаблоны, заканчивающиеся точно в этой вершине.
#     После объединения (output[u].update(output[fail[u]])) включает вложенные и пересекающиеся шаблоны.
