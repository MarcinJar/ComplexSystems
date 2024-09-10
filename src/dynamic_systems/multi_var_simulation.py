import matplotlib.pyplot as plt

class MultiVarSimulation:
    def __init__(self, a: float, b: float = 0, end_time: float = 3.0, t_interval: float = 0.1) -> None:
        self.a = a
        self.b = b
        self.t_interval = t_interval
        self.end_time = end_time
        self.x_result: list[float] = []
        self.y_result: list[float] = []
        self.timesteps: list[float] = []

    def run(self, start_x: float = 1.0, start_y: float = 1.0, start_t: float = 0.0) -> None:
        self.initialize(start_x, start_y, start_t)
        while self.timesteps[-1] < self.end_time:
            self.update()
            
    def display(self) -> None:
        plt.plot(self.x_result, 'b-')
        plt.plot(self.y_result, 'g--')
        plt.show()
        
    def display_phase_space(self) -> None:
        plt.plot(self.x_result, self.y_result)
        plt.show()

    def initialize(self, start_x: float = 1.0, start_y: float = 1.0, start_t: float = 0.0) -> None:
        self.x_result.append(start_x)
        self.y_result.append(start_y)
        self.timesteps.append(start_t)

    def update(self) -> None:
        new_x = self.a * self.x_result[-1] + self.y_result[-1]
        new_y = self.b * self.x_result[-1] + self.y_result[-1]
        self._observe(new_x, new_y)

    def _observe(self, new_x: float, new_y: float) -> None:
        self.x_result.append(new_x)
        self.y_result.append(new_y)
        t = self._calculate_next_t()
        self.timesteps.append(t)

    def _calculate_next_t(self) -> float:
        return self.timesteps[-1] + self.t_interval

        