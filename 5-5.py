n = list(map(int, input().split()))
print('OK' if max(n) == len(n) and len(set(n)) == len(n) else 'BAD')


from collections import Counter
n = list(map(int, input().split()))
l = Counter(n)
print('OK' if max(n) == len(n) and max(l.values()) == 1 else 'BAD')