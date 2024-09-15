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

def floodFill(image: list[list[str]], x: int, y: int, newChar: str, oldChar: str = None) -> None:
    if oldChar == None:
        oldChar = image[y][x]
        
    if oldChar == newChar or image[y][x] != oldChar:
        return
    
    image[y][x] = newChar
    
    # printImage(image)
    
    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        floodFill(image, x, y + 1, newChar, oldChar)
        
    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        floodFill(image, x, y - 1, newChar, oldChar)
        
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        floodFill(image, x + 1, y, newChar, oldChar)
    
    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        floodFill(image, x - 1, y, newChar, oldChar)
        
    return

def printImage(image: list[list[str]]) -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')
    
printImage(im)

floodFill(im, 3, 3, '|')
printImage(im)

floodFill(im, 7, 7, 'x')
printImage(im)