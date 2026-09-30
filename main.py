def neuron(inputs, weights, bias):
    total = 0
    for input, weight in zip(inputs, weights):
        total += input * weight
    return total + bias

def relu(x):
    return max(0, x)

def layer(inputs, weights, bias):
    outputs = []
    for w, b in zip(weights, bias):
        output = neuron(inputs, w, b)
        output = relu(output)
        outputs.append(output)
    return outputs

inputs_1 = [0.8, 0.9]
weights_1 = [
    [0.5, 0.2],
    [0.1, 0.8],
    [0.7, -0.3]
]
bias_1 = [0.1, 0.2, 0.3]

layer_1 = layer(inputs_1, weights_1, bias_1)

inputs_2 = layer_1
weights_2 = [
    [0.2, 0.4, 0.1],
    [0.5, -0.3, 0.7]
]
bias_2 = [0.1, 0.2]

layer_2 = layer(inputs_2, weights_2, bias_2)

print(layer_2)