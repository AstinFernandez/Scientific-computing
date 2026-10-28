1. Mathematical Concept

Numerical optimization finds the input x that makes a function f(x) as small (or as large) as possible. At a minimum, the slope is zero and the curve bends upward:

f′(x*) = 0 and f″(x*) > 0

When no neat formula exists, algorithms such as gradient descent or bounded Brent search find x* by repeatedly improving a guess.

2. Example

Take f(x) = 12x + 4800/x.

f′(x) = 12 − 4800/x², which equals 0 when x² = 400, so x* = 20.
f(20) = 240 + 240 = 480.
3. Real-World Applications

Cloud resource allocation, network routing, machine-learning training (minimizing loss), scheduling, engineering design, cost reduction and parameter tuning.

4. Real-World Problem and Solution Approach

Problem: A cloud team rents n servers at $12 per server-hour. Too few servers cause slow responses, which cost an SLA penalty modelled as 4800/n dollars per hour. How many servers minimize total hourly cost?

Approach: Write total cost as C(n) = 12n + 4800/n and let scipy.optimize.minimize_scalar search for the minimum. Compare it with the analytic answer n* = √(b/a) and with a brute-force grid search.
B. Inputs and mathematical operation
Inputs: a = 12 (server price), b = 4800 (penalty scale), the search interval 1 ≤ n ≤ 100, and the cost function C(n).
Operation: minimize C(n) = an + b/n numerically, then verify against the exact solution n* = √(b/a) = 20.
C. Changing a parameter
Change	Analytic n*	Minimum cost	Effect
Baseline (a = 12, b = 4800)	20	$480	none
b = 7500 (stricter SLA)	25	$600	more servers are worth paying for
a = 48 (pricier servers)	10	$960	the optimum shifts to fewer servers

Since n* = √(b/a), the optimum grows with the penalty and shrinks with the server price. Because of the square root, quadrupling a only halves n*.

D. Meaning of the output and graph

The program prints the best number of servers (about 20) and its hourly cost (about $480). All three methods agree, which confirms the optimizer is correct.

In the graph, the rising dashed line is server cost and the falling dashed line is the penalty. Their sum, the solid curve, is U-shaped. The red dot at the bottom of the U is the minimum, where adding one more server saves less in penalty than it costs to rent. Note that the curve is flat near the minimum, so 18 or 22 servers cost only slightly more than 20.

E. Related case: optimal order quantity (inventory)

This has the same shape, cost = a·Q + b/Q, with different meanings. A shop sells D = 12,000 units/year, each order costs S = $50, and holding one unit costs h = $3/year. The cost is holding plus ordering: C(Q) = hQ/2 + DS/Q.