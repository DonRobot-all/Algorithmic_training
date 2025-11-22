def compute_prefix_function(pattern):
    """
    Строим массив LPS (Longest Prefix-Suffix).
    lps[i] = длина самого длинного суффикса подстроки pattern[:i+1],
             который одновременно является её префиксом.
    """
    lps = [0] * len(pattern)
    j = 0  # длина текущего совпавшего префикса

    for i in range(1, len(pattern)):
        # если несовпадение — откатываем j по LPS таблице
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        # если совпало — удлиняем текущий префикс
        if pattern[i] == pattern[j]:
            j += 1

        lps[i] = j

    return lps


def kmp_search(text, pattern):
    """
    Возвращает индекс первого вхождения pattern в text.
    Если нет — возвращает -1.
    """
    if not pattern:
        return 0

    lps = compute_prefix_function(pattern)
    j = 0  # индекс в pattern

    for i in range(len(text)):  # i — индекс в text
        # если несовпадение — откатываем j по lps
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        # если совпало — двигаемся дальше
        if text[i] == pattern[j]:
            j += 1

        # если дошли до конца шаблона — нашли вхождение
        if j == len(pattern):
            return i - j + 1  # позиция начала вхождения

    return -1


# --- Пример из задания ---

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

position = kmp_search(text, pattern)

if position != -1:
    print(f"Образец найден в позиции {position}")
else:
    print("Образец не найден")
