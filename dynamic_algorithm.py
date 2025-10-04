def longest_common_substring(s1: str, s2: str):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0
    end_pos = 0 

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0

    substring = s1[end_pos - max_len:end_pos]
    return substring, max_len


s1 = "hish"
s2 = "fish"

substring, length = longest_common_substring(s1, s2)
print("Самая длинная общая подстрока:", substring)
print("Длина:", length)
