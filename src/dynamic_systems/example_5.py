from fibonacci_simulation import FibonacciSimulation

a = 1
b = 1
start_x = 1.0
start_y = 1.0

simulation = FibonacciSimulation(a, b)
simulation.run(start_x, start_y)
simulation.display()
simulation.display_phase_space()