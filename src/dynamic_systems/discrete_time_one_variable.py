a = 1.1

def initialize() -> None:
    global x, result
    x = 1.0
    result = [x]
    
def observe() -> None:
    global x, result
    result.append(x)
    
def update() -> None:
    global x, a, result
    x = a * x
    observe()
    
def display() -> None:
    global result
    print(result)
    
initialize()
for t in range(30):
    update()
    
display()