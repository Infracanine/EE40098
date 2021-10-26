import numpy as np
from numpy.core.fromnumeric import repeat
from ann import NeuralNetwork

def repeat_iterations(neural_network, iterations, training_vectors, target_vectors):
    for i in range(iterations):
        for j in range(len(training_vectors)):
            neural_network.train(training_vectors[j], target_vectors[j])

        # Calculate sum of square differences between target vectors and current querying 
        current_output = np.array(neural_network.query_multiple(training_vectors))
        print(f"Iteration {i + 1}/{iterations}: error is {np.sum(np.square(current_output - np.array(target_vectors)))}")
    # Optionally terminate and return when error threshold falls below some arg
    print("Iterations complete")
    return current_output


if __name__ == "__main__":
    # Create a neural network instance with two inputs, two hidden neurons and one output 
    # neuron. Create some test inputs and query the network (without any training), how do 
    # you explain the networks output? 
    test_network = NeuralNetwork(2, 2, 1, 0.1)
    training_vectors = []
    for x1 in range(2):
        for x2 in range(2):
                training_vectors.append([x1, x2])

    and_target_list = [0, 0, 0, 1]
    or_target_list = [0, 1, 1, 1]

    print(repeat_iterations(test_network, 10000, training_vectors, and_target_list))


  

    
