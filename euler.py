import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plot

# Re-define mathematical function as necessary
# f(x) is the derivative function
def square(x):
    return x**2

def identity(x):
    return x

def y_prime(y):
    k = 3
    return k*y

# y(x_i) = y_i
# f is y'
# n is number of steps
# [x_i, x_f] interval
def euler(f, x_i, x_f, n, y_i):

    x_list = []
    y_list = []

    delta_x = (float(x_f) - float(x_i))/n

    x_list.append(x_i)
    y_list.append(y_i)

    for i in range(1, n + 1):
        x_i = x_list[i - 1] + delta_x
        y_i = y_list[i - 1] + f(y_list[i - 1]) * delta_x
        x_list.append(x_i)
        y_list.append(y_i)


    print x_list
    print y_list
    return x_list, y_list

print y_prime(3)
x, y = euler(identity, 0.0, 1.0, 50, 1.0)

def truefunc(x):
    return math.exp(x)

def true_generator(f, x_i, x_f, n):
    delta_x = (float(x_f) - float(x_i))/n

    x_list = [x_i + i * delta_x for i in range(n + 1)]
    y_list = [f(x_list[i]) for i in range(n + 1)]

    return x_list, y_list

def simple_plot(x, y, color, true, truecolor):
    fig, ax = plot.subplots()
    ax.plot(x, y, color)

    x2, y2 = true_generator(true,  0.0, 1.0, 50)
    ax.plot(x2, y2, truecolor)

    ax.set(xlabel = 'x axis', ylabel = 'y axis', title='y versus x')
    ax.grid()

    plot.show()

simple_plot(x,y, '.r-', truefunc, '.g-')
