import sys

im = [
    list('__####################________'),
    list('__#_________________#___###___'),
    list('__#___________#############_###'),
    list('__#_________________#___###___'),
    list('__#_________________#___###___'),
    list('__#_________________#___###___'),
    list('__###################___###___'),
    list('__###--------------##___###___'),
    list('__####--------#--####___###___'),
    list('__######---------####___###___'),
    list('__###################___###___'),
    list('__###################___###___'),
]

HEIGHT = len(im)
WIDTH = len(im[0])

def floodFillIterative(image: list[list[str]], x: int, y: int, newChar: str, oldChar: str = None) -> None:
    stack: list[(int, int)] = []   
    oldChar = image[y][x]
    
    if oldChar == newChar:
        return
    
    stack.append((y, x))

    while stack:
        y, x = stack.pop()
        image[y][x] = newChar
        
        if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
            stack.append((y + 1, x))
            
        if y - 1 >= 0 and image[y - 1][x] == oldChar:
            stack.append((y - 1, x))
            
        if x + 1 < WIDTH and image[y][x + 1] == oldChar:
            stack.append((y, x + 1))
        
        if x - 1 >= 0 and image[y][x - 1] == oldChar:
            stack.append((y, x - 1))
        
def printImage(image: list[list[str]]) -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')
    
printImage(im)

floodFillIterative(im, 3, 3, '|')
printImage(im)

floodFillIterative(im, 7, 7, 'x')
printImage(im)