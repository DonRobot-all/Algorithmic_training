from collections import deque

class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([('0000', 0)]) 
        visited = set('0000')
   
        while queue:
            current_combination, moves = queue.popleft()
            
            if current_combination == target:
                return moves
            
            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(current_combination[i]) + delta) % 10
                    new_combination = (
                        current_combination[:i] + str(new_digit) + current_combination[i+1:]
                    )
                    
                    if new_combination not in visited and new_combination not in deadends:
                        visited.add(new_combination)
                        queue.append((new_combination, moves + 1))
        
        return -1
    
a = Solution()
print(a.openLock(["0201","0101","0102","1212","2002"], "0202"))