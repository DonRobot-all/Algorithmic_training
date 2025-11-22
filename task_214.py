class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        ts = s + "#" + r
        n = len(ts)
        pi = [0 for _ in range(n)]
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and ts[i] != ts[j]: j = pi[j - 1]
            if ts[i] == ts[j]: j += 1
            pi[i] = j

        return r[: len(r) - pi[-1]] + s