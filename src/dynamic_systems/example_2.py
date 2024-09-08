from one_var_simulation import OneVarSimulation

a = 1.05
b = 2.0
start_x = 10.0

simulation = OneVarSimulation(a, b)
simulation.run(start_x)
simulation.display()