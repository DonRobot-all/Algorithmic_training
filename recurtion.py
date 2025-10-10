
# Сумма чисел от 1 до n
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

print(sum_n(5))  # 15


# Факториал числа
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))  # 24

# Числа Фибоначчи
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8


# Обратная строка
def reverse(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse(s[:-1])

print(reverse("abc"))  # "cba"


# Сумма цифр числа
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(123))  # 6

# Проверка палиндрома
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False


# Вывод чисел от 1 до n
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n, end=" ")

print_numbers(5)  # 1 2 3 4 5
