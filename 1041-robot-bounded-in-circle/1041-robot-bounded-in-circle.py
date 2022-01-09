class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        direction = 'n'
          
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
                    if direction == 'n':
                        direction = 'w'
                    elif direction == 's':
                        direction = 'e'
                    elif direction == 'e':
                        direction = 'n'
                    elif direction == 'w':
                        direction = 's'
                elif char == 'R':
                    if direction == 'w':
                        direction = 'n'
                    elif direction == 'e':
                        direction = 's'
                    elif direction == 'n':
                        direction = 'e'
                    elif direction == 's':
                        direction = 'w'
                # print(x,y, direction)
            if x == 0 and y == 0:
                return True
        return False