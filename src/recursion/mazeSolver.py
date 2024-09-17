
from typing import LiteralString


MAZE = """
#######################################################################
#S#                 #       # #   #     #         #     #   #         #
# ##### ######### # ### ### # # # # ### # # ##### # ### # # ##### # ###
# #   #     #     #     #   # # #   # #   # #       # # # #     # #   #
# # # ##### # ########### ### # ##### ##### ######### # # ##### ### # #
#   #     # # #     #   #   #   #         #       #   #   #   #   # # #
######### # # # ##### # ### # ########### ####### # # ##### ##### ### #
#       # # # #     # #     # #   #   #   #     # # #   #         #   #
# # ##### # # ### # # ####### # # # # # # # ##### ### ### ######### # #
# # #   # # #   # # #     #     #   #   #   #   #   #     #         # #
### # # # # ### # # ##### ####### ########### # ### # ##### ##### ### #
#   # #   # #   # #     #   #     #       #   #     # #     #     #   #
# ### ####### ##### ### ### ####### ##### # ######### ### ### ##### ###
#   #         #     #     #       #   # #   # #     #   # #   # #   # #
### ########### # ####### ####### ### # ##### # # ##### # # ### # ### #
#   #   #       # #     #   #   #     #       # # #     # # #   # #   #
# ### # # ####### # ### ##### # ####### ### ### # # ####### # # # ### #
#     #         #     #       #           #     #           # #      E#
#######################################################################
""".split("\n")

# consts use in program
EMPTY = ' '
START = 'S'
EXIT = 'E'
PATH = '.'

# maze size settings
HEIGHT = len(MAZE)
WIDTH = 0

for row in MAZE:
    if len(row) > WIDTH:
        WIDTH = len(row)
    
for i in range(len(MAZE)):
    MAZE[i] = list(MAZE[i])
    if len(MAZE[i]) != WIDTH:
        MAZE[i] = [EMPTY]*WIDTH
        
def printMaze(maze: list[LiteralString]) -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(maze[y][x], end='')
        print()
    print()
    
def findStart(maze: list[LiteralString]) -> tuple[int, int]:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if maze[y][x] == START:
                return (y, x)
            
def solveMoze(maze: list[LiteralString], x = None, y = None, visited = None) -> bool:
    if x == None or y == None:
        x, y = (3, 2)
        maze[y][x] = EMPTY
        
    if visited == None:
        visited = []
        
    if maze[y][x] == EXIT:
        return True
    
    maze[y][x] = PATH
    visited.append(str(x) + ',' + str(y))
    #printMaze(maze) # Uncomment to show evry step in alghoritm
    
    if y + 1 < HEIGHT and maze[y + 1][x] in (EMPTY, EXIT) and str(x) + ',' + str(y + 1) not in visited:
        if solveMoze(maze, x, y + 1, visited):
            return True
        
    if y - 1 < HEIGHT and maze[y + 1][x] in (EMPTY, EXIT) and str(x) + ',' + str(y - 1) not in visited:
        if solveMoze(maze, x, y - 1, visited):
            return True
        
    if x + 1 < WIDTH and maze[y][x + 1] in (EMPTY, EXIT) and str(x + 1) + ',' + str(y) not in visited:
        if solveMoze(maze, x + 1, y, visited):
            return True
        
    if x - 1 < WIDTH and maze[y][x - 1] in (EMPTY, EXIT) and str(x - 1) + ',' + str(y) not in visited:
        if solveMoze(maze, x - 1, y, visited):
            return True
    
    maze[y][x] = EMPTY
    # printMaze(maze) # Uncomment to show evry step in alghoritm
    
    return False


print(HEIGHT) 
print(WIDTH) 
print(findStart(MAZE))
x, y = findStart(MAZE)
print(MAZE[y][x])

printMaze(MAZE)
print(solveMoze(MAZE))
printMaze(MAZE)
