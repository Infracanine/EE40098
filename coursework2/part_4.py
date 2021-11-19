from random import randint, random
from operator import add
from functools import reduce
import matplotlib.pyplot as plt

def int_to_binary_encode(integer):
    return

def binary_to_int_decode(integer):
    return
    
def individual(min, max):
    # Create a binary representation of integer x in range min -> max
    return format(randint(min, max)) 

def population(count, min, max):
# Create a number of individuals (i.e. a population).

# count: the number of individuals in the population
# length: the number of values per individual
# min: the minimum possible value in an individual's list of values
# max: the maximum possible value in an individual's list of values
    return [ individual(min, max) for x in range(count) ]

def fifth_order_polynomial_fitness(individual, y):
    # Evaluate suitability of individual for curve 5th-order polynomial at y
    a = 25
    b = 18
    c = 31
    d = -14
    e = 7
    f = -19
    result = (a * (individual ** 5)) + (b * (individual ** 4)) + (c * (individual ** 3)) + (d * (individual ** 2)) + (e * individual) + f
    return abs(y - result)

def grade(pop, target):
    # Find average fitness for a population.
    summed = reduce(add, (fifth_order_polynomial_fitness(x, target) for x in pop))
    return summed / (len(pop) * 1.0)

def evolve(pop, target, min, max, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [ (fifth_order_polynomial_fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]
    pos_to_mutate = 0
    # randomly add other individuals to
    # promote genetic diversity
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)
    # mutate some individuals
    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual)-1)
        # this mutation is not ideal, because it
        # restricts the range of possible values,
        # but the function is unaware of the min/max
        # values used to create the individuals,
        individual = randint(min, max)
    # crossover parents to create children
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = int(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)     
    parents.extend(children)
    return parents

if __name__ == "__main__":
    # Example code
    # Target number 
    target = 0

    # Size of population 
    p_count = 100
    i_min = 0
    i_max = 100
    p = population(p_count, i_min, i_max)
    fitness_history = [grade(p, target),]
    for i in range(100):
        p = evolve(p, target, min=i_min, max=i_max)
        fitness_history.append(grade(p, target))

    for datum in fitness_history:
        print(datum)

    plt.plot(fitness_history)
    plt.xlabel("Iteration")
    plt.ylabel("Fitness evaluation")
    plt.show()