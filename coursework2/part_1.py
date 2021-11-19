from random import randint, random
from operator import add
from functools import reduce
import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt

# Create binary string encoding a number
def individual(length):
    # Create a member of the population.
    return [ str(randint(0,1)) for _ in range(length) ]

# Decode binary string
def decode(binary_string):
    return int(''.join(binary_string), 2)

def population(count, length):
    # Create a number of individuals (i.e. a population).
    return [ individual(length) for x in range(count) ]

def fitness_list(population, target):
    output = []
    for each in population:
        output.append(fitness(each, target))
    return output

# Determine fitness of binary string by decoding to int and comparing to target
def fitness(individual, target):
    # individual: the individual to evaluate
    # target: the target number individuals are aiming for
    value = decode(individual)
    return abs(target-value)

def grade(pop, target):
    # Find average fitness for a population.
    summed = reduce(add, (fitness(x, target) for x in pop))
    return summed / (len(pop) * 1.0)

def roulette_selection(pop, target, retain_length):
    sum_fitness = reduce(add, (fitness(x, target) for x in pop))
    probabilities = ([ (fitness(x, target) / sum_fitness) for x in pop ])
    # print(sum(probabilities))
    result = []
    for i in range(retain_length):
        result.append(pop[npr.choice(len(pop), p=probabilities)])
    print(len(result))
    return result

def graded_selection(pop, target, retain_length, random_select):
    graded = [ (fitness(x, target), x) for x in pop]
    graded = [ x[1] for x in sorted(graded)]
    result = graded[:retain_length]
    # Probabilistically add some random individuals from the weaker elements of the population to our parents list (promotes genetic diversity)
    for individual in graded[retain_length:]:
        if random_select > random():
            result.append(individual)
    return result
    
def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.1, elitism=0.02, selection_method="RANKED"):
    # 1. SELECTION:
    retain_length = int(len(pop)*retain)
    parents = []
    if(selection_method == "RANKED"):
        parents = graded_selection(pop, target, retain_length, random_select)
    elif(selection_method == "ROULETTE"):
        parents = roulette_selection(pop, target, retain_length)
    else:
        raise Exception(f"ERROR|Invalid selection method passed to evolve, was '{selection_method}'.")

    # 2. MUTATION: Probabilistically mutate some individuals in the new list we've created
    # 2a. Determine how many elites we want to retain based on elitism cooefficient
    pos_to_mutate = 0
    elite_size = int(len(pop)*elitism)
    for individual in parents[elite_size:]:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual) - 1)
            individual[pos_to_mutate] = str(randint(0, 1))
    # 3. BREEDING: 
    # 3a. We want the new population to be the same length as the previous one at each step, 
    #     so we determine how many children we need to create based on the length of the parent list
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        # 3b. Get two random individuals in the parent list
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        # 3c. Perform single-point crossover
        if male != female:
            male = parents[male]
            female = parents[female]
            half = int(len(male) / 2)
            child = male[:half] + female[half:]
            children.append(child)     
    # 3d. Merge parent and child lists once length of both lists combined is same as starting population
    parents.extend(children)
    return parents

def perform_ga_iterations(target, p_count, i_length, iterations, stagnation_threshold, selection_meth):
    if(target < 0 or target > ((2 ** i_length) - 1)):
        print(f"ERROR|Target {target} not in range representable by chromosomes of length {i_length}\n")
        return
    p = population(p_count, i_length)
    fitness_history = [grade(p, target),]
    for i in range(iterations):
        p = evolve(p, target, selection_method=selection_meth)
        fitness_grade = grade(p, target)
        fitness_history.append(fitness_grade)
        # Check if we've reached optimal fitness, at which point terminate
        if(0.0 in fitness_history):
            print(f"Population reached fitness at iteration {i + 1}, terminating prematurely.")
            break
        # Check for genetic stagnation, at which point terminate
        if(len(set(fitness_history[-stagnation_threshold:])) == 1):
            print(f"Population stagnated at iteration {i + 1}, at population fitness of {fitness_grade}.")
            break
    return fitness_history

def perform_multiple_ga_iterations(count, target, p_count, binary_string_length, iterations, stagnation_threshold):
    results = []
    for i in range(count):
        fitness_history = perform_ga_iterations(target, p_count, binary_string_length, iterations, stagnation_threshold)
        if(fitness_history[-1] == 0.0):
            results.append(len(fitness_history) - 1)
    print(f"Completed. {len(results)}/{count} GA runs completed succesfully.\n")
    print(f"Average number of evolutions to produce solution: {sum(results) / len(results)}\n")


# Create a simple optimisation where the function of the optimiser is to simply find a number specified in the shortest number of iterations
if __name__ == "__main__":
    # Target number
    target = 75

    # Size of population 
    p_count = 100

    binary_string_length = 8
    iterations = 100
    stagnation_thresh = 12
    # perform_multiple_ga_iterations(200, target, p_count, binary_string_length, iterations, stagnation_thresh)
    fitness_history = perform_ga_iterations(target, p_count, binary_string_length, iterations, stagnation_thresh, "ROULETTE")

    for datum in fitness_history:
        print(datum)

    plt.plot(fitness_history)
    plt.xlabel("Iteration")
    plt.ylabel("Fitness evaluation")
    plt.show()