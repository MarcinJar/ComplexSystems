
class OneVarSimulation:
    def __init__(self, a: float, b: float = 0, end_time: float = 3.0, t_interval: float = 0.1) -> None:
        """
        Initializes the OneVarSimulation object with the given parameters.
        Args:
            a (float): The coefficient of the variable in the simulation equation.
            b (float, optional): The constant term in the simulation equation. Defaults to 0.
            end_time (float, optional): The end time of the simulation. Defaults to 3.0.
            t_interval (float, optional): The time interval between each simulation step. Defaults to 0.1.
        """
        self.a = a
        self.b = b
        self.t_interval = t_interval
        self.end_time = end_time
        self.result: list[float] = []
        self.timesteps: list[float] = []

    def run(self, start_x: float = 1.0, start_t: float = 0.0) -> None:
        """
        Runs the simulation from the given start values.
        Args:
            start_x (float, optional): The initial value of the variable. Defaults to 1.0.
            start_t (float, optional): The initial time. Defaults to 0.0.
        """
        self.initialize(start_x, start_t)
        while self.timesteps[-1] < self.end_time:
            self.update()

    def initialize(self, start_x: float = 1.0, start_t: float = 0.0) -> None:
        """
        Initializes the result and timesteps lists with the given start values.
        Args:
            start_x (float, optional): The initial value of the variable. Defaults to 1.0.
            start_t (float, optional): The initial time. Defaults to 0.0.
        """
        self.result.append(start_x)
        self.timesteps.append(start_t)

    def update(self) -> None:
        """
        Updates the variable value based on the simulation equation and observes the new value.
        """
        new_x = self.a * self.result[-1] + self.b
        self._observe(new_x)

    def display(self) -> None:
        """
        Displays the simulation results using matplotlib.
        """
        import matplotlib.pyplot as plt
        plt.plot(self.timesteps, self.result)
        plt.show()

    def _observe(self, new_x: float) -> None:
        """
        Observes the new value of the variable and updates the result and timesteps lists.
        Args:
            new_x (float): The new value of the variable.
        """
        self.result.append(new_x)
        t = self._calculate_next_t()
        self.timesteps.append(t)

    def _calculate_next_t(self) -> float:
        """
        Calculates the next time step based on the current time and the time interval.
        Returns:
            float: The next time step.
        """
        return self.timesteps[-1] + self.t_interval

        