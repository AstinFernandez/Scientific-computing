1. Mathematical Concept

Monte Carlo methods estimate a quantity by random sampling. To estimate an integral or an average:

I = ∫ f(x) dx ≈ (b − a) · (1/N) Σ f(xᵢ), with xᵢ drawn uniformly from [a, b]

The typical error shrinks like σ/√N: to get 10 times more accuracy you need 100 times more samples. Probabilities are estimated as the fraction of trials in which an event happens.

2. Example

Estimating π: pick random points (x, y) in the unit square. The quarter circle x² + y² ≤ 1 has area π/4, so

π ≈ 4 × (points inside the circle) / (total points)

Out of 1,000 points, roughly 785 land inside, giving π ≈ 3.14.

3. Real-World Applications

Risk analysis, reliability, queue simulation, finance, uncertainty analysis, computer graphics, physical simulations and estimating difficult integrals.

4. Real-World Problem and Solution Approach

Problem: A software project has three sequential tasks with uncertain durations (days), given as (minimum, most likely, maximum): A (5, 8, 12), B (10, 14, 22), C (4, 6, 10). What is the probability the project finishes within a 30-day deadline?

Approach: Simulate 100,000 projects by drawing each task’s duration from a triangular distribution, add them up, and count the fraction finishing within the deadline. The program also estimates π to show how Monte Carlo error shrinks as N grows.
B. Inputs and mathematical operation
Inputs: the seed (42), N = 100,000 samples, the three triangular distributions, and the deadline of 30 days.
Operation: draw pseudo-random numbers, apply a rule to each sample (inside the circle? total ≤ deadline?), and average the results. The mean of the indicator values estimates the probability.
C. Changing a parameter
Deadline: The expected total is about 30.3 days with a standard deviation of about 3.1 days. A 30-day deadline gives roughly a 46% chance of finishing on time. Moving the deadline to 35 days raises this to about 93%, and cutting it to 27 days drops it to about 14%.
Sample size N: The standard error of the probability is √(p(1−p)/N). At N = 1,000 it is about ±0.016, and at N = 1,000,000 it is about ±0.0005. This is the 1/√N rule: 1,000 times more samples gives about 32 times less error.
Seed: Changing it gives slightly different numbers, but they agree within the standard error.
D. Meaning of the output and graphs
The program prints π to about two or three decimal places, the average project length, and the probability of meeting the deadline. A result near 0.46 means that, with the current uncertainty, the 30-day deadline is about a coin flip. The 95th percentile (roughly 35.5 days) is a safer figure to promise a client.

In the left graph, the estimate of π swings wildly for small N, then settles toward the red line at 3.14159. This is the 1/√N convergence. In the right graph, the histogram is a bell shape with a slightly longer right tail. Everything to the left of the red deadline line counts as on time, and the area to the right is the risk of being late. The tail is long because delays (up to 22 days for task B) are larger than the possible savings.

E. Related case: reliability of a 2-out-of-3 server cluster

A cluster stays online if at least 2 of its 3 servers work, and each server works with probability 0.90 on a given day. Monte Carlo can estimate the cluster’s availability, and the exact answer is 3(0.9²)(0.1) + 0.9³ = 0.972, so we can check the simulation.