n, k = map(int, input().split())
i = max(n // k, 1)
ans = abs(n - k * i)
i += 1
ans2 = abs(n - k * i)
print(min(ans, ans2))