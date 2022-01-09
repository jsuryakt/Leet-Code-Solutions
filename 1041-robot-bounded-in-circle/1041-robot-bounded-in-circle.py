class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        direction = 'n'
        L = {'n':'w','s':'e','e':'n','w':'s'}
        R = {'w':'n','e':'s','n':'e','s':'w'}
          
        for _ in range(4):
            for char in instructions:
                if char == 'G':
                    if direction == 'n':
                        y += 1
                    elif direction == 's':
                        y -= 1
                    elif direction == 'e':
                        x += 1
                    elif direction == 'w':
                        x -= 1
                elif char == 'L':
                    direction = L[direction]
                elif char == 'R':
                    direction = R[direction]
                    
            if x == 0 and y == 0:
                return True
            
        return False