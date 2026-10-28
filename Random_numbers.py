import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# ---------- Part 1: estimate pi ----------
N = 100_000
x = rng.random(N)
y = rng.random(N)
inside = (x**2 + y**2) <= 1.0
pi_estimate = 4 * inside.mean()
running_pi = 4 * np.cumsum(inside) / np.arange(1, N + 1)

print(f"Pi estimate with N = {N:,}: {pi_estimate:.5f}")
print(f"Absolute error: {abs(pi_estimate - np.pi):.5f}")

# ---------- Part 2: project completion risk ----------
def simulate_project(n_trials, deadline, rng):
    task_a = rng.triangular(5, 8, 12, n_trials)
    task_b = rng.triangular(10, 14, 22, n_trials)
    task_c = rng.triangular(4, 6, 10, n_trials)
    total = task_a + task_b + task_c
    p_on_time = np.mean(total <= deadline)
    std_error = np.sqrt(p_on_time * (1 - p_on_time) / n_trials)
    return total, p_on_time, std_error

deadline = 30
total, p, se = simulate_project(100_000, deadline, rng)

print(f"\nMean project duration: {total.mean():.2f} days")
print(f"P(finish within {deadline} days) = {p:.3f} (+/- {se:.3f})")
print(f"95th percentile duration: {np.percentile(total, 95):.1f} days")

# ---------- Graphs ----------
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].semilogx(np.arange(1, N + 1), running_pi)
axes[0].axhline(np.pi, color="red", linestyle="--", label="True pi")
axes[0].set_xlabel("Number of random points N")
axes[0].set_ylabel("Estimate of pi")
axes[0].set_title("Monte Carlo convergence")
axes[0].legend()

axes[1].hist(total, bins=60, color="steelblue", alpha=0.8)
axes[1].axvline(deadline, color="red", linestyle="--", label=f"Deadline = {deadline}")
axes[1].set_xlabel("Total project duration (days)")
axes[1].set_ylabel("Number of simulated projects")
axes[1].set_title("Project duration distribution")
axes[1].legend()

plt.tight_layout()
plt.savefig("task05_monte_carlo.png", dpi=150)
plt.show()