import numpy as np

class Perceptron():
    def __init__(self, weights_list, bias):
        # Convert weights to numpy array
        self.weights = np.array(weights_list)
        self.bias = bias
        
    # Apply perceptron to some list of inputs
    def apply(inputs_list):
        inputs = np.array(inputs_list)

        # Calculate the dot product
        summed = np.dot(inputs, self.weights)

        # Add in the bias
        summed = summed + self.bias

        # Calculate the output
        # N.B. this is a ternary operator
        output = 1 if summed > 0 else 0
        return output

    def __str__():
        for i in range()
        return f""

if __name__ == "__main__":
    