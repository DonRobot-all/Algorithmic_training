def kmp_search(text, pattern):
    if not pattern:
        return 0  # Пустой образец всегда найден в начале строки
    
    n = len(text)
    m = len(pattern)
    
    # Если образец длиннее текста, он не может быть найден
    if m > n:
        return -1
    
    # Вычисляем префикс-функцию для образца
    pi = compute_prefix_function(pattern)
    
    # Ищем образец в тексте
    j = 0  # Указатель на текущую позицию в образце
    
    for i in range(n):
        # Если символы не совпадают, используем префикс-функцию для сдвига
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]
        
        # Если символы совпадают, увеличиваем указатель образца
        if text[i] == pattern[j]:
            j += 1
        
        # Если достигли конца образца, значит образец найден
        if j == m:
            return i - m + 1  # Возвращаем индекс начала найденного образца
    
    return -1  # Образец не найден

# Вспомогательная функция для расчета префикс-функции
def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    
    k = 0
    for i in range(1, m):
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k-1]
        
        if pattern[k] == pattern[i]:
            k += 1
        
        pi[i] = k
    
    return pi


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

position = kmp_search(text, pattern)
if position != -1:
    print(f"Образец найден в позиции {position}")
else:
    print("Образец не найден")