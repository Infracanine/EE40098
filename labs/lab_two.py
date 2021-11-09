# The Perceptron:
# The Perceptron was first described in 1957 by Frank Rosenblatt at Cornell. It is a simle time of linear classifier i.e. the output depends on a linear combination of the inputs. 
# When first introduced, many perceptions were connected to form the first ever artificial neural network. In this lab we will start by considering single Perceptron.
# f(x) = 1, if w.x + b > 0 
# f(x) = 0, otherwise
# WHere w is a vector of real-valued weights, w.x is the dot product and b is  bias term that can be used to scale the effecive threshold. 

# Exercise 2 and 3, Interpreting perceptron outputs as truth tables, what logical functions are being performed:
# Bias of -1 acts as boolean AND

import numpy as np
import matplotlib.pyplot as plt 

# A single perceptron function
def perceptron(inputs_list, weights_list, bias):
    #Convert the inputs list into a np array
    inputs = np.array(inputs_list)

    # Convert the weights list into a np array
    weights = np.array(weights_list)

    # Calculate the dot product
    summed = np.dot(inputs, weights)

    # Add in the bias
    summed = summed + bias

    # Calculate the output
    # N.B. this is a ternary operator
    output = 1 if summed > 0 else 0
    return output

def calculate_intercepts(weights_list, b):
    # Calculate x intercept (i.e. where y = 0)
    x_intercept = -(b / weights_list[0])
    # Calculate y intercept (i.e. where x = 0)
    y_intercept = -(b / weights_list[1])
    return [x_intercept, 0], [0, y_intercept]

    

def simulate_boolean_input_perms(weights_list, bias, input_range, title):
    fig = plt.xkcd() 
    # Set the axis limits 
    plt.xlim(-2, 2) 
    plt.ylim(-2, 2) 
    # Label the plot  
    plt.xlabel("Input 1")
    plt.ylabel("Input 2")
    plt.title("State Space of " + title + " perceptron")

    plot_colour = ""
    print("Weights: ", weights_list)
    print("Bias:    ", bias)
    full_output = []

    # Iterate through all input permutations, calculate and store outputs and generate points on table
    for x1 in range(input_range):
        for x2 in range(input_range):
            input = [x1, x2]
            out = perceptron(input, weights_list, bias)
            plot_colour = "green" if out == 1 else "red"
            plt.scatter(input[0], input[1], s=50, zorder=3, color=plot_colour)
            print("P(" + str(input) + ") = " + str(out))
            full_output.append(out)
    intercepts = calculate_intercepts(weights_list, bias)
    plt.axline(intercepts[0], intercepts[1])
    plt.grid(True, linewidth=1, linestyle=':')
    plt.tight_layout() 
    plt.show()
    return full_output

def simulate_xor():
    print("PERCEPTRON SIMULATING XOR")
    fig = plt.xkcd() 
    # Set the axis limits 
    plt.xlim(-2, 2) 
    plt.ylim(-2, 2) 
    # Label the plot  
    plt.xlabel("Input 1")
    plt.ylabel("Input 2")
    plt.title("State Space of bolean XOR perceptron")
    for x1 in range(2):
        for x2 in range(2):
            input = [x1, x2]
            out = xor_perceptron([x1, x2])
            plot_colour = "green" if out == 1 else "red"
            plt.scatter(input[0], input[1], s=50, zorder=3, color=plot_colour)
            print("P(" + str(input) + ") = " + str(out))

    intercepts_one = calculate_intercepts([2.0, 2.0], -1)
    intercepts_two = calculate_intercepts([-1.0, -1.0], 1.5)
    plt.axline(intercepts_one[0], intercepts_one[1])
    plt.axline(intercepts_two[0], intercepts_two[1])
    plt.grid(True, linewidth=1, linestyle=':')
    plt.tight_layout() 
    plt.show()

def or_perceptron(inputs_list):
    return perceptron(inputs_list, [2.0, 2.0], -1)

def and_perceptron(inputs_list):
    return perceptron(inputs_list, [1.0, 1.0], -1)

def nor_perceptron(inputs_list):
    return perceptron(inputs_list, [-1.0, -1.0], 1)

def nand_perceptron(inputs_list):
    return perceptron(inputs_list, [-1.0, -1.0], 2)

def xor_perceptron(inputs_list):
    return and_perceptron([or_perceptron(inputs_list), nand_perceptron(inputs_list)])

if __name__ == "__main__":
    # Boolean AND (bias of -1)
    print("PERCEPTRON SIMULATING AND")
    print(simulate_boolean_input_perms([1.0, 1.0], bias=-0.5, input_range=2, title="boolean AND"))

    # # Boolean NAND
    print("PERCEPTRON SIMULATING NAND")
    print(simulate_boolean_input_perms([-1.0, -1.0], bias=1.5, input_range=2, title="boolean NAND"))

    # # Boolean OR (bias of 0)
    print("PERCEPTRON SIMULATING OR")
    print(simulate_boolean_input_perms([2.0, 2.0], bias=-1, input_range=2, title="boolean OR"))

    # Boolean XOR
    simulate_xor()


