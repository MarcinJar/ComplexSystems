from symulation import Simulation

a = 1.05
b = 2.0
start_x = 10.0

simulation = Simulation(a, b)
simulation.run(start_x)
simulation.display()