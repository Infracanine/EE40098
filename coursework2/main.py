from random import randint, random
from operator import add
from functools import reduce
import matplotlib.pyplot as plt

def individual(length, min, max):
# Create a member of the population.
    return [ randint(min,max) for x in range(length) ]

def population(count, length, min, max):
# Create a number of individuals (i.e. a population).

# count: the number of individuals in the population
# length: the number of values per individual
# min: the minimum possible value in an individual's list of values
# max: the maximum possible value in an individual's list of values
    return [ individual(length, min, max) for x in range(count) ]

def fitness_list(population, target):
    output = []
    for each in population:
        output.append(fitness(each, target))
    return output
    
def fitness(individual, target):

    # Determine the fitness of an individual. Lower is better.

    # individual: the individual to evaluate
    # target: the target number individuals are aiming for
    sum = reduce(add, individual, 0)
    return abs(target-sum)

def grade(pop, target):
    # Find average fitness for a population.
    summed = reduce(add, (fitness(x, target) for x in pop))
    return summed / (len(pop) * 1.0)

def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [ (fitness(x, target), x) for x in pop]
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
            individual[pos_to_mutate] = randint(
            min(individual), max(individual))
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

def perform_ga_iterations(target, p_count, i_length, i_min, i_max, iterations):
    p = population(p_count, i_length, i_min, i_max)
    fitness_history = [grade(p, target),]
    for i in range(iterations):
        p = evolve(p, target)
        fitness_grade = grade(p, target)
        fitness_history.append(fitness_grade)
        if(0.0 in fitness_list(p, target)):
            print(f"Population reached fitness at iteration {i}, terminating prematurely.")
            break
        # Check for genetic stagnation
        stagnation_threshold = 10
        if(len(set(fitness_history[-stagnation_threshold:])) == 1):
            print(f"Population stagnated at iteration {i}, at population fitness of {fitness_grade}.")
            break
    return fitness_history

if __name__ == "__main__":
    # Example code
    # Target number 
    target = 75

    # Size of population 
    p_count = 50
    i_length = 1
    i_min = 0
    i_max = 100
    iterations = 100
    fitness_history = perform_ga_iterations(target, p_count, i_length, i_min, i_max, iterations)

    for datum in fitness_history:
        print(datum)

    plt.plot(fitness_history)
    plt.xlabel("Iteration")
    plt.ylabel("Fitness evaluation")
    plt.show()