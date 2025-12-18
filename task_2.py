import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x):
    return x**2

def monte_carlo_integrate(func, a, b, num_samples=10000):
    x_rand = np.random.uniform(a, b, num_samples)
    y_rand = np.random.uniform(0, func(b), num_samples)
    
    under_curve = y_rand < func(x_rand)
    
    return x_rand, y_rand, under_curve

a = 0
b = 2
samples = 15000

x_rand, y_rand, under_curve = monte_carlo_integrate(f, a, b, samples)
integral_approx = (np.sum(under_curve) / samples) * ((b - a) * f(b))

quad_result, error = spi.quad(f, a, b)

print(f"Monte Carlo Result: {integral_approx}")
print(f"Quad Result: {quad_result}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.scatter(x_rand[under_curve], y_rand[under_curve], color='blue', s=1, alpha=0.5, label='Points under curve')
ax.scatter(x_rand[~under_curve], y_rand[~under_curve], color='orange', s=1, alpha=0.3, label='Points above curve')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Monte Carlo Integration: f(x) = x^2 from {a} to {b}')
ax.legend()
plt.grid()
plt.show()