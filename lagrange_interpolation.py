import numpy as np
import matplotlib.pyplot as plt

# Data
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk interpolasi Lagrange
def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (xi - x[j]) / (x[i] - x[j])
        yi += y[i] * L
    return yi

# Plotting hasil interpolasi
x_range = np.linspace(5, 40, 400)
y_lagrange = [lagrange_interpolation(x_data, y_data, xi) for xi in x_range]

plt.plot(x_data, y_data, 'o', label='Data', color='black')
plt.plot(x_range, y_lagrange, label='Interpolasi Lagrange', color='red')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.legend()
plt.title('Interpolasi Lagrange')
plt.grid(True)
plt.show()

# Testing
print("Hasil interpolasi Lagrange di x=12:", lagrange_interpolation(x_data, y_data, 12))
