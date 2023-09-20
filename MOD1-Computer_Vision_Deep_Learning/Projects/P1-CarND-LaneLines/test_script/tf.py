import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the system of differential equations
def system(t, X, A, B):
    dXdt = np.dot(A, X) + B
    return dXdt

# Define the matrices A and B
A = np.array([[1, 2, 3, 4],
              [0, 1, 0, 1],
              [1, 0, 0, 0],
              [0, 0, 1, 0]])

B = np.array([1, 2, 3, 4])

# Define the initial conditions
initial_values = np.array([0, 0, 0, 0])  # Replace with your initial conditions

# Set the time span for integration
initial_time = 0
final_time = 10
num_points = 100

# Solve the system of differential equations
X0 = initial_values.reshape(-1, 1)
t_span = (initial_time, final_time)
solution = solve_ivp(system, t_span, X0, args=(A, B), t_eval=np.linspace(initial_time, final_time, num_points))

# Access the solution
t = solution.t
X_solution = solution.y

# Create individual plots for each component of X
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

for i in range(4):
    axs[i].plot(t, X_solution[i])
    axs[i].set_ylabel(f'X{i+1}')
    axs[i].grid(True)

axs[3].set_xlabel('Time')
plt.suptitle('Evolution of Each Component of X')
plt.show()
