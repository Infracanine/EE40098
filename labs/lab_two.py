# The Perceptron:
# The Perceptron was first described in 1957 by Frank Rosenblatt at Cornell. It is a simle time of linear classifier i.e. the output depends on a linear combination of the inputs. 
# When first introduced, many perceptions were connected to form the first ever artificial neural network. In this lab we will start by considering single Perceptron.
# f(x) = 1, if w.x + b > 0 
# f(x) = 0, otherwise
# WHere w is a vector of real-valued weights, w.x is the dot product and b is  bias term that can be used to scale the effecive threshold. 

# Exercise 2 and 3, Interpreting perceptron outputs as truth tables, what logical functions are being performed:
# Bias of -1 acts as boolean AND

import numpy as np

# A single perceptron function
def perceptron(inputs_list, weights_list, bias):
    if(inputs_list.len() is not weights_list.len()):
        print("Length of inputs list and weight list did not match.")
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

def simulate_boolean_input_perms(weights_list, bias, input_range):
    full_output = []
    print("Weights: ", weights_list)
    print("Bias:    ", bias)
    for x1 in range(input_range + 1):
        for x2 in range(input_range + 1):
            input = [x1, x2]
            out = perceptron(input, weights_list, bias)
            print("P(" + str(input) + ") = " + str(out))
            full_output.append(out)
    return full_output

def or_perceptron(inputs_list):
    return perceptron(inputs_list, [1.0, 1.0], -1)

def and_perceptron(inputs_list):
    return perceptron(inputs_list, [1.0, 1.0], 0)

# Boolean AND (bias of -1)
print(simulate_boolean_input_perms([1.0, 1.0], bias=-1, input_range=1))

# Boolean OR (bias of 0)
print(simulate_boolean_input_perms([1.0, 1.0], bias=0, input_range=1))

# Boolean 
print(simulate_boolean_input_perms([1.0, 1.0], bias=-1.5, input_range=1))

