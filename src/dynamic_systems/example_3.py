from multi_var_simulation import MultiVarSimulation

a = 0.5
b = -0.5
start_x = 1.0
start_y = 1.0

simulation = MultiVarSimulation(a, b, 3, 0.1)
simulation.run(start_x, start_y)
simulation.display()
simulation.display_phase_space()