from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        q = deque([(startGene, 0)])

        while q:
            word, steps = q.popleft()

            if word == endGene:
                return steps

            for i in range(len(word)):
                for ch in ["A", 'C', 'G', 'T']:
                    transformed = word[:i] + ch + word[i+1:]
                    if transformed in bank and transformed not in visited:
                        q.append((transformed, steps+1))
                        visited.add(transformed)
            print(q)
        return -1
    
a = Solution()
print(a.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # 1
print(a.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))  # 2
print(a.minMutation("AACCGGTT", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))  # 2