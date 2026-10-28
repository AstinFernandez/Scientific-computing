import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Inputs
a = 12.0      # cost per server-hour ($)
b = 4800.0    # SLA penalty scale ($ * servers / hour)

def total_cost(n):
    return a * n + b / n

# Numerical optimization
result = minimize_scalar(total_cost, bounds=(1, 100), method="bounded")

# Analytic check and brute-force check
n_analytic = np.sqrt(b / a)
grid = np.linspace(1, 100, 1000)
n_grid = grid[np.argmin(total_cost(grid))]

print(f"Optimizer result : n = {result.x:.3f}, cost = ${result.fun:.2f}/hour")
print(f"Analytic result  : n = {n_analytic:.3f}, cost = ${total_cost(n_analytic):.2f}/hour")
print(f"Grid search      : n = {n_grid:.3f}")

# Graph
plt.figure(figsize=(7, 4))
plt.plot(grid, total_cost(grid), label="Total cost C(n)")
plt.plot(grid, a * grid, "--", label="Server cost 12n")
plt.plot(grid, b / grid, "--", label="Penalty 4800/n")
plt.scatter([result.x], [result.fun], color="red", zorder=5, label="Minimum")
plt.xlabel("Number of servers n")
plt.ylabel("Cost per hour ($)")
plt.ylim(0, 1500)
plt.title("Cloud resource allocation")
plt.legend()
plt.tight_layout()
plt.savefig("task04_optimization.png", dpi=150)
plt.show()