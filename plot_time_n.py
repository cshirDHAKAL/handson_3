import time
import numpy as np
import matplotlib.pyplot as plt

# Function to analyze
def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

# Measure execution time for various n
n_values = np.arange(1, 101)  # n from 1 to 100
times = []

for n in n_values:
    start_time = time.time()
    f(n)
    times.append(time.time() - start_time)

# Fit a quadratic curve to the data
coefficients = np.polyfit(n_values, times, 2)
fitted_times = np.polyval(coefficients, n_values)

# Plot results
plt.figure(figsize=(8,6))
plt.scatter(n_values, times, color='blue', label='Measured Time')
plt.plot(n_values, fitted_times, color='red', label='Quadratic Fit', linewidth=2)
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime Analysis of Function f(n)')
plt.legend()
plt.grid()
plt.show()
