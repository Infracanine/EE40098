import numpy as np 
import math
import random
import matplotlib.pyplot as plt 

def acceptance_probability(old_cost, new_cost, T):
    return math.exp((old_cost-new_cost)/T)

def cost(supply, demand):
    delta = np.subtract(demand, supply)
    delta2 = np.square(delta)
    average = np.average(delta2)
    dcost = math.sqrt(average)
    return dcost

def neighbour(solution, d):
    delta = np.random.random((10,10))
    scale = np.full((10, 10), 2*d)
    offset = np.full((10, 10), 1.0 - d)
    var = np.multiply(delta, scale)
    m = np.add(var, offset)
    new_solution = np.multiply(solution, m)
    return new_solution

def anneal(solution, target, alpha, iterations, var):
    old_cost = cost(solution, target)
    cost_values = list()
    cost_values.append(old_cost)
    T = 1.0
    T_min = 0.000001
    while T > T_min:
        for i in range(1, iterations):
            print(f"Iteration: {i}, Cost: {old_cost}")
            new_solution = neighbour(solution, var)
            new_cost = cost(new_solution, target)
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random.random():
                solution = new_solution
                old_cost = new_cost
            cost_values.append(old_cost)
        T=T*alpha
    return solution, old_cost, cost_values

supply = np.full((10, 10), 0.5)
demand = np.random.random((10, 10))
print(f"Supply\n {supply}\n")

print(f"Demand\n {demand}\n")

rms = cost(supply, demand)
print("RMS = " + str(rms))

alpha = 0.9
iterations = 200
var = 0.01

final_solution, final_cost, cost_values = anneal(supply, demand, alpha, iterations, var)

print(demand)
print(final_solution)
print(final_cost)

plt.subplot(232)
plt.title("Error function in Simulated annealing")
plt.plot(cost_values)
plt.grid(True)

plt.subplot(234)
plt.title("Initial Supply matrix")
plt.imshow(supply, cmap='hot')

plt.subplot(235)
plt.title("Optimised Supply matrix")
plt.imshow(final_solution, cmap='hot')

plt.subplot(236)
plt.title("Demand matrix")
plt.imshow(demand, cmap='hot')

plt.show()