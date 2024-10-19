from collections import *
s = input()
cnt = Counter (s)
half = ""
mid = ""
for c in sorted(cnt.keys()):
    half += c * (cnt[c] // 2)
    if cnt[c] % 2 and not mid:
        mid = c
ans = half + mid + half[::-1]
print(ans)