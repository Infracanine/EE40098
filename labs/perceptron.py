import numpy as np

class Perceptron():
    def __init__(self, weights_list, bias):
        # Convert weights to numpy array
        self.weights = np.array(weights_list)
        self.bias = bias
        
    # Apply perceptron to some list of inputs
    def apply(self, inputs_list):
        inputs = np.array(inputs_list)

        # Calculate the dot product
        summed = np.dot(inputs, self.weights)

        # Add in the bias
        summed = summed + self.bias

        # Calculate the output
        # N.B. this is a ternary operator
        output = 1 if summed > 0 else 0
        return output

    def __str__(self):
        weights_output = ""
        for i in range(self.weights.size):
            weights_output += f"{self.weights[i]}x_{i} + "
        return weights_output + str(self.bias) + " = y"

if __name__ == "__main__":
    p = Perceptron([1.0, 2.0], -1)
    print(str(p))
