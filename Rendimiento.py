import numpy as np
import matplotlib.pyplot as plt
import time

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        if initial_state is None:
            self.board = np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])
        else:
            self.board = initial_state

    def step(self):
        new_board = self.board.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(i, j)
                if self.board[i, j] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_board[i, j] = 0  # Muere
                else:
                    if alive_neighbors == 3:
                        new_board[i, j] = 1  # Nace
        self.board = new_board

    def count_alive_neighbors(self, x, y):
        total = 0
        for i in range(max(0, x-1), min(self.rows, x+2)):
            for j in range(max(0, y-1), min(self.cols, y+2)):
                if (i, j) != (x, y):  # No contar la celda misma
                    total += self.board[i, j]
        return total

    def run(self, steps):
        for _ in range(steps):
            self.step()

def measure_performance(sizes, steps):
    times = []
    for size in sizes:
        rows, cols = size, size  # Grilla cuadrada
        game = GameOfLife(rows, cols)
        
        start_time = time.time()
        game.run(steps)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        avg_time_per_step = elapsed_time / steps
        times.append(avg_time_per_step)
        print(f'Tamaño: {size}x{size}, Tiempo promedio por iteración: {avg_time_per_step:.6f} segundos')
    return times

def plot_performance(sizes, times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'o-', label='Tiempo promedio por iteración')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (número de celdas)')
    plt.ylabel('Tiempo promedio por iteración (segundos)')
    plt.title('Rendimiento del Juego de la Vida de Conway')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    sizes = [32, 64, 128, 256, 512, 1024]  # Tamaños de la grilla
    steps = 10  # Número de iteraciones
    times = measure_performance(sizes, steps)
    plot_performance(sizes, times)
