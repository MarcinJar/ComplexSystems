
class Simulation:
    def __init__(self, a: float, b: float = 0, end_time: float = 3.0, t_interval: float = 0.1) -> None:
        self.a = a
        self.b = b
        self.t_interval = t_interval
        self.end_time = end_time
        self.result: list[float] = []
        self.timesteps: list[float] = []
        
    def run(self, start_x: float = 1.0, start_t: float = 0.0) -> None:
        self.initialize(start_x, start_t)
        while self.timesteps[-1] < self.end_time:
            self.update()
            
    def initialize(self, start_x: float = 1.0, start_t: float = 0.0) -> None:
        self.result.append(start_x)
        self.timesteps.append(start_t)
           
    def update(self) -> None:
        new_x = self.a * self.result[-1] + self.b
        self._observe(new_x)
        
    def display(self) -> None:
        import matplotlib.pyplot as plt
        plt.plot(self.timesteps, self.result)
        plt.show()
        
    def _observe(self, new_x: float) -> None:
        self.result.append(new_x)
        t = self._calculate_next_t()
        self.timesteps.append(t)
        
    def _calculate_next_t(self) -> float:
        return self.timesteps[-1] + self.t_interval
        