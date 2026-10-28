import numpy as np
from scipy.optimize import minimize_scalar

D, S, h = 12_000, 50.0, 3.0
cost = lambda Q: h * Q / 2 + D * S / Q

res = minimize_scalar(cost, bounds=(1, 5000), method="bounded")
print(f"Optimal order size : {res.x:.1f} units")
print(f"Analytic sqrt(2DS/h): {np.sqrt(2 * D * S / h):.1f} units")
print(f"Minimum yearly cost: ${res.fun:.2f}")