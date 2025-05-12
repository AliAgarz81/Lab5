import math

def f(x):
    return (math.exp(x) - 1 / x - 1)

x = 0.6
for i in range(100):
    x_new = x - 0.1 * f(x)
    if abs(x_new - x) < 0.000001:
        break
    x = x_new

print(x)
