import numpy as np
import matplotlib.pyplot as plt
import random


np.seterr(invalid='ignore', over='ignore')  # suppress warning caused by division by inf

def f(x):
    return 1/(1 + np.exp(3*(x-3))) * 10 * x**2  + 1 / (1 + np.exp(-3*(x-3))) * (0.5*(x-10)**2 + 50)

def fprime(x):
    return 1 / (1 + np.exp((-3)*(x-3))) * (x-10) + 1/(1 + np.exp(3*(x-3))) * 20 * x + (3* np.exp(9))/(np.exp(9-1.5*x) + np.exp(1.5*x))**2 * ((0.5*(x-10)**2 + 50) - 10 * x**2) 

def run(start, lr, loop):
    x = start
    values = []
    values.append([start, f(start)])
    for i in range(loop):
        x = x - fprime(x) * lr
        values.append([x, f(x)])
    return values



# x = np.linspace(-5,20,100)
# plt.plot(x,f(x), 'k')
# plt.plot()
# plt.show()

start = random.randrange(-5, 20)
lr = 4
loop = 200
values = run(start, lr, loop)

points = np.array(values)
x_vals = points[:, 0]
y_vals = points[:, 1]

x = np.linspace(-5, 20, 100)
plt.plot(x, f(x), 'k', label='f(x)')

# Vẽ các bước descent
plt.plot(x_vals, y_vals, 'ro-', markersize=4, label='GD Steps')

# Chú thích điểm đầu và cuối
plt.annotate("Start", xy=(x_vals[0], y_vals[0]), xytext=(x_vals[0]+0.5, y_vals[0]+10),
             arrowprops=dict(facecolor='green', arrowstyle='->'), fontsize=10)

plt.annotate("End", xy=(x_vals[-1], y_vals[-1]), xytext=(x_vals[-1]-2, y_vals[-1]-10),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
