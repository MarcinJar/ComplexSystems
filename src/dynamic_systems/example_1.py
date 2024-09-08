import numpy as np
import matplotlib.pyplot as plt

a = 1.15

def initialize() -> None:
    global x, result, t, timesteps
    x = 1.0
    result = [x]
    t = 0.
    timesteps = [t]
    
def observe() -> None:
    global x, result, t, timesteps
    result.append(x)
    timesteps.append(t)
    
def update() -> None:
    global x, a, result, t, timesteps
    x = a * x
    t = t + 0.1
    observe()
    
def display() -> None:
    global result, timesteps
    plt.plot(timesteps, result)
    plt.show()
    
initialize()
while t < 3.0:
    update()
    
display()