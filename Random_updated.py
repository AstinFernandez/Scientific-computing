import numpy as np

rng = np.random.default_rng(42)
n_days = 1_000_000
p_server = 0.90

servers_up = rng.random((n_days, 3)) < p_server   # True = server works
cluster_ok = servers_up.sum(axis=1) >= 2

estimate = cluster_ok.mean()
std_error = np.sqrt(estimate * (1 - estimate) / n_days)
print(f"Simulated availability: {estimate:.4f} (+/- {std_error:.4f})")
print("Exact availability    : 0.9720")